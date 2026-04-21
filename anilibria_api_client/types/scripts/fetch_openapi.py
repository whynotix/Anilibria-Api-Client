from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


OPENAPI_URL = "https://anilibria.top/storage/api/docs/v1?aniliberty-api-v1-docs.json"
ROOT_DIR = Path(__file__).resolve().parents[3]
OUTPUT_PATH = ROOT_DIR / "anilibria_api_client" / "types" / "schema" / "anilibria-v1.openapi.json"


def fetch_schema() -> object:
    try:
        with urlopen(OPENAPI_URL, timeout=60) as response:
            status = getattr(response, "status", 200)
            if status != 200:
                raise RuntimeError(f"Unexpected HTTP status: {status}")
            return json.load(response)
    except HTTPError as exc:
        raise RuntimeError(f"Failed to download OpenAPI schema: HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"Failed to download OpenAPI schema: {exc.reason}") from exc


def write_schema(schema: object) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(schema, ensure_ascii=False, indent=2, sort_keys=True)
    fd, temp_name = tempfile.mkstemp(
        prefix="anilibria-openapi-",
        suffix=".json",
        dir=str(OUTPUT_PATH.parent),
        text=True,
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as file:
            file.write(payload)
            file.write("\n")
        os.replace(temp_name, OUTPUT_PATH)
    except Exception:
        if os.path.exists(temp_name):
            os.unlink(temp_name)
        raise


def main() -> int:
    try:
        schema = fetch_schema()
        write_schema(schema)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(f"Saved schema to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
