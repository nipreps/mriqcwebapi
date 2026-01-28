import json
import sys
from datetime import datetime, timezone


def main(status_path: str, output_path: str) -> None:
    with open(status_path, encoding="utf-8") as handle:
        payload = json.load(handle)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    status = payload["status"]

    rows = "\n".join(
        """<tr>
        <td>{name}</td>
        <td><a href=\"{url}\">{url}</a></td>
        <td>{code}</td>
        <td>{duration:.3f}s</td>
        <td>{ok}</td>
      </tr>""".format(
            name=item["name"],
            url=item["url"],
            code=item["status_code"],
            duration=item["duration_seconds"],
            ok="OK" if item["ok"] else "WARN",
        )
        for item in payload["endpoints"]
    )

    html = f"""<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
    <title>MRIQC Healthcheck</title>
    <style>
      body {{ font-family: sans-serif; margin: 2rem; }}
      .status {{ font-weight: bold; }}
      table {{ border-collapse: collapse; width: 100%; margin-top: 1rem; }}
      th, td {{ border: 1px solid #ddd; padding: 0.5rem; text-align: left; }}
      th {{ background: #f5f5f5; }}
    </style>
  </head>
  <body>
    <h1>MRIQC API Health</h1>
    <p class=\"status\">Overall status: {status}</p>
    <p>Since: {payload["since"]}</p>
    <p>Updated: {now}</p>
    <table>
      <thead>
        <tr>
          <th>Endpoint</th>
          <th>URL</th>
          <th>Status Code</th>
          <th>Duration</th>
          <th>Result</th>
        </tr>
      </thead>
      <tbody>
        {rows}
      </tbody>
    </table>
  </body>
</html>
"""

    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(html)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
