from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[3]
SCRIPTS_DIR = ROOT_DIR / "anilibria_api_client" / "types" / "scripts"


def run(script_name: str) -> None:
    subprocess.run([sys.executable, str(SCRIPTS_DIR / script_name)], check=True, cwd=str(ROOT_DIR))


def main() -> int:
    run("fetch_openapi.py")
    run("generate_codegen.py")
    print("OpenAPI schema and generated code are up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
