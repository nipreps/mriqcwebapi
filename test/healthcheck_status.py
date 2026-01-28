import json
import sys
from datetime import datetime, timezone

URLS = {
    "swagger": "https://mriqc.nimh.nih.gov/",
    "t1w": "https://mriqc.nimh.nih.gov/api/v1/T1w",
    "bold": "https://mriqc.nimh.nih.gov/api/v1/bold",
}


def main(raw_path: str, output_path: str) -> None:
    status = "OK"
    endpoints = []

    with open(raw_path, encoding="utf-8") as handle:
        for line in handle:
            name, code, duration = line.strip().split("|")
            code_int = int(code) if code.isdigit() else 0
            endpoints.append(
                {
                    "name": name,
                    "url": URLS[name],
                    "status_code": code_int,
                    "duration_seconds": float(duration),
                    "ok": 200 <= code_int < 400,
                }
            )
            if not (200 <= code_int < 400):
                status = "WARN"

    payload = {
        "status": status,
        "since": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "endpoints": endpoints,
    }

    with open(output_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
