from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[3]
SCRIPTS_DIR = ROOT_DIR / "anilibria_api_client" / "types" / "scripts"
TRACKED_PATHS = [
    "anilibria_api_client/types/schema/anilibria-v1.openapi.json",
    "anilibria_api_client/types/codegen",
    "anilibria_api_client/types/__init__.py",
    "anilibria_api_client/types/models.py",
    "anilibria_api_client/types/responses.py",
    "anilibria_api_client/models.py",
    "anilibria_api_client/responses.py",
    "anilibria_api_client/response_models.py",
]


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=str(ROOT_DIR),
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    update_result = run([sys.executable, str(SCRIPTS_DIR / "update_codegen.py")])
    if update_result.returncode != 0:
        sys.stderr.write(update_result.stdout)
        sys.stderr.write(update_result.stderr)
        return update_result.returncode

    status_result = run(["git", "status", "--porcelain", "--", *TRACKED_PATHS])
    if status_result.returncode != 0:
        sys.stderr.write(status_result.stderr)
        return status_result.returncode

    if status_result.stdout.strip():
        sys.stderr.write("Generated OpenAPI artifacts are out of date.\n")
        sys.stderr.write(status_result.stdout)
        return 1

    print("Generated OpenAPI artifacts are up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
