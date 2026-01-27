# Agent Instructions

This repository (`nipreps/mriqcwebapi`) is a small, mostly-unattended service that has accrued maintenance debt.
It deploys via Docker Compose, and it exposes a REST API implemented with **Python Eve** (MongoDB-backed).
The current pain points are:

- The Docker-compose deploy appears to work, but the **Eve API is not responsive**.
- The repo has **no consistent linting** and **no meaningful unit/integration tests**.

This file exists to keep code-agents on a safe, high-signal trajectory: reproduce first, then stabilize, then modernize.

## Operating Principles

1. **Always plan first.** Provide a brief plan before any changes and do the hardest thinking during the planning phase.
2. **Highlight critical points.** When proposing tasks, call out steps that could introduce side effects (e.g., migrations, API changes, backward-compatibility concerns).
3. **Ask one question at a time.** If a decision is needed from a user, ask a single, clear question before proceeding.
4. **Prefer minimal, reversible changes.** This repo is production-adjacent; avoid broad rewrites without explicit request.
5. **Reproduce before refactor.** If the API is “unresponsive”, first turn that into a deterministic failure mode with logs and a reproduction recipe.

## “Definition of Done” for Any PR

A PR is not “done” until it includes:

- A short **problem statement** and **scope** (what is fixed / not fixed).
- A clear list of **user-visible behavior changes** (ideally: none unless required).
- **Tests** added or updated (or an explicit rationale why tests are impractical).
- **Lint/format** run (or an explicit limitation + exact commands to retry).
- A **repro / verification** section with exact commands (copy/paste-able).

## Repository Run Commands

- The README documents a local run flow (use this as the first baseline reproduction):
   ```bash
   cd dockereve-master/
   docker-compose build
   docker-compose up -d
   ```
- Smoke-check (expected: HTTP response, not a hang/timeout)
   ```bash
   curl -i -H "Content-Type: application/json" http://localhost/api/v1/T1w
   ```
- Swagger docs are expected at: http://localhost/docs
- Environment variables are expected via dockereve-master/.env (defaults per README):
   ```
   MONGODB_HOST=mongodb
   MONGODB_PORT=27017

   API_TOKEN=<secret_token>
   API_URL=http://localhost/docs/api
   ```
   **Important**: `API_URL` is commonly used by the browser-facing docs UI (Swagger) and therefore must be reachable *from the user’s browser*, not just from within containers. This is a common source of “docs load but API doesn’t work”.

### Runbook: When “Eve Is Unresponsive”

When the API is “unresponsive”, follow this exact order. Do not guess.
1. Establish the failure mode precisely
   Run:
   ```
   # What does "unresponsive" mean?
   curl -v http://localhost/api/v1/
   curl -v http://localhost/api/v1/T1w
   curl -v http://localhost/docs
   ```
   Classify outcomes:
   - Connection refused → Nginx not listening / wrong port mapping.
   - Timeout/hang → upstream service hung, DNS/network issue, or Mongo connection stall.
   - HTTP 502/504 → Nginx up, upstream down/unhealthy.
   - HTTP 401/403 → auth/token mismatch, header requirements changed.
   - HTTP 500 → application exception; proceed to logs.

2. Inspect container status and ports
   ```
   docker compose -f dockereve-master/docker-compose.yml ps
   docker compose -f dockereve-master/docker-compose.yml logs --tail=200 nginx
   docker compose -f dockereve-master/docker-compose.yml logs --tail=200 endpoints
   docker compose -f dockereve-master/docker-compose.yml logs --tail=200 mongodb
   ```
   Goal: extract the first actionable traceback/error message.
3. Verify Mongo connectivity from the API container.
   From the endpoints container, check it can resolve and connect to Mongo:
   ```
   docker compose -f dockereve-master/docker-compose.yml exec endpoints sh -lc '
     python -c "import socket; print(socket.gethostbyname(\"mongodb\"))"'
   ```
   If Python imports are broken or the container lacks tooling, fall back to:
   ```
   docker compose -f dockereve-master/docker-compose.yml exec endpoints sh -lc 'cat /etc/resolv.conf'
   ```

4. Confirm the app actually starts (Gunicorn / Eve).
   Look for:
   - boot messages,
   - bind address/port,
   - worker exits / crash loops,
   - import errors,
   - Mongo timeouts.

   If Gunicorn is used, check whether it is binding to `0.0.0.0` and the correct port for the Nginx upstream.

5. Add an explicit healthcheck (preferred stabilization step).
   If missing, add a health endpoint and/or Docker healthchecks so “unresponsive” becomes “unhealthy” quickly:
   - A lightweight `/healthz` (no DB) and `/readyz` (DB connectivity) is ideal.
   - Update docker-compose to include `healthcheck:` blocks for key services.

   **Keep this backward-compatible**: do not move existing routes.

## Architectural Constraints and Invariants

Codex must treat these as invariants unless the user explicitly requests breaking changes:
1. **API base path** stays stable: `/api/v1/...`
2. **Existing resource names** (e.g., `T1w`, `bold`, etc.) should not be renamed.
3. **Response shapes** should not change casually (Eve’s default pagination fields, `_items`, etc.).
4. **MongoDB is the system of record.** Schema changes require a migration plan or compatibility layer.
5. **Docs UI** under `/docs` is considered part of the user experience; avoid breaking it.

## Change Management: Schema, DB, and Backward Compatibility

Eve APIs are often “schema-driven”:
- Resource schemas live in config (commonly `settings.py`), and they define validation, allowed fields, and query filters.
- Mongo documents in the wild may not match a newly “tightened” schema.

Rules:
- **Never tighten validation** (e.g., making optional fields required) without:
   - a compatibility strategy (accept old + new),
   - a migration script, and
   - tests proving old data still serves.
- **Any DB migration** must be:
  - idempotent,
  - safe to rerun,
  - documented with rollback/backout steps.

## Testing Strategy (Incremental, Not Aspirational)

This project currently lacks reliable tests. Build them in layers:

### Layer 0: Smoke tests (fastest win)
- A test that the app imports and starts (even if using a test config).
- A test that `/api/v1/` returns *some* HTTP response.

### Layer 1: Unit tests (no Docker, minimal dependencies)
Target:
- config loading,
- schema validity (domain definitions),
- auth/token helper behavior,
- utility functions.

Use:
- `pytest`
- `mongomock` (or a minimal in-memory substitute) where feasible.

### Layer 2: Integration tests (Docker Compose + real Mongo)
Target:
- bring up `mongodb` + `endpoints`,
- seed a tiny fixture dataset,
- run a few `curl`/`requests` assertions (HTTP 200, pagination fields present, query filters behave).

**Key requirement**: tests must be deterministic and runnable in CI.

### Test command conventions
- Prefer: `pytest -q`
- If dockerized: document exactly which compose file and which service runs tests.

## Linting, Formatting, and Pre-Change Validation
### Formatting (required)
- **Always run formatting before proposing changes.**
- Standard command (CI-friendly diff mode):
  ```
  pipx run ruff format --diff .
  ```
  Locally, to apply formatting:
  ```
  pipx run ruff format .
  ```
### Linting (strongly preferred)
If a `ruff` check configuration exists (or once added), run:
```
pipx run ruff check .
```
If the repository is not yet ready for full lint enforcement, introduce linting in phases:
- start with low-noise rules (syntax errors, unused imports),
- then expand.

**If linting cannot run**
- State the limitation and provide exact retry steps (commands + required environment).

## Dependency and Runtime Upgrades

This repo likely includes aging dependencies and may run on an EOL Python base image.

Rules:
1. *No “drive-by” dependency upgrades* in bugfix PRs unless needed to fix the bug.
2. *Upgrade in small PRs*:
   - runtime Python,
   - framework dependencies (Eve/Flask/Gunicorn),
   - Nginx image,
   - Mongo image.
3. For any upgrade PR:
   - include explicit “before/after” behavior checks,
   - add/extend tests first where possible,
   - call out compatibility risks.

## Security and Secrets
- Never commit real secrets:
   - `API_TOKEN` must not be committed in `.env`.
- Prefer adding a checked-in template:
   - `.env.example` (safe defaults + placeholders).
- Any auth change must preserve existing clients or be clearly versioned and documented.

## Branch Naming
- Format: <type>/<short-description>
- Examples:
  - `fix/one-off-bug-gh134`
  - `enh/add-bids-validator`
  - `doc/update-readme`

If working from a tracked issue, include the issue number in the branch name (e.g., `fix/segfault-gh134`).

## Commit Messages (Conventional Commits)
- Must strictly follow Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/
- Examples:
   - `fix(parser): handle empty token stream`
   - `docs(readme): add quickstart example`
   - `chore(ci): pin action versions`

## Pull Request Titles & Descriptions
- **PR Title format**: `TYPE: Short summary`
  - Type is all caps, from a conventional-commit-like set (e.g., FIX, ENH, MNT, DOC, CI, CHORE).
  - No scope parenthetical in PR titles.
- Examples:
  - `FIX: Address one-off bug in traversing list`
  - `DOC: Complete docstring with missing arguments`
- PR Description should include:
  - Summary of changes
  - Motivation / context
  - Testing performed (exact commands)
  - Risk assessment / rollout notes (especially for Docker/DB changes)

## How Codex Should Approach Work Items

For any issue/feature request:

1. Reproduce (or explain precisely why reproduction is not possible).
2. Diagnose with logs and minimal instrumentation.
3. Add/extend tests that capture the bug.
4. Fix with minimal surface area.
5. Refactor only if it reduces future risk and is covered by tests.
6. Document:
   - README troubleshooting updates if relevant,
   - operational notes if deployment is impacted.

## Suggested First Milestones (Recommended Trajectory)

The goal is to pay down maintenance debt while restoring service health, prioritize:

1. Reliability / Responsiveness
  - add healthchecks + better logging,
  - fix the immediate “Eve unresponsive” root cause.
2. Minimal CI
  - ruff format check,
  - pytest smoke tests.
3. Integration test harness
  - docker-compose test job that starts Mongo + API and exercises 2–3 endpoints.
4. Modernization (only after tests exist)
  - update runtime Python,
  - upgrade core dependencies in small steps.

## Notes on Communication
- If you must ask for user input, ask exactly one targeted question.
- Prefer proposing 2–3 crisp options with trade-offs (risk, time, compatibility).
    If you must ask for user input, ask exactly one targeted question.

    Prefer proposing 2–3 crisp options with trade-offs (risk, time, compatibility).
