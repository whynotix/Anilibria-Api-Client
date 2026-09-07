# AGENTS.md

Async API wrapper for the AniLibria Swagger. The upstream repo is **archived** (last release v0.2.4). PRs target `main` and `dev`; the auto-style workflow opens PRs against `dev`.

## Environment

- **Python 3.13 only** (`requires-python = ">=3.13"`). Code targets py313.
- Managed with **Poetry** (`poetry.lock`), even though the build backend is setuptools and `pyproject.toml` mixes PEP 621 `[project]` with legacy `[tool.poetry]`. Use `poetry install --with dev`, and run all tooling via `poetry run ...`.
- A local `.venv/` already exists.

## Commands

```bash
poetry install --with dev          # deps + dev group (pytest, pytest-asyncio, dotenv, ruff)
poetry run pytest -q tests/ -s     # run all tests
poetry run pytest -q tests/methods/test_account.py -s   # single file (note -s)
poetry run pytest -q tests/methods/test_account.py::test_name -s  # single test
poetry run ruff check .            # lint    (auto-fix: ruff check --fix .)
poetry run ruff format .           # format
poetry run mypy .                  # type check
```

## Tests hit the live API (not mocked)

`tests/fixtures.py` loads `.env` and reads `ANILIBRIA_API_TOKEN`, `LOGIN`, `PASSWORD`. Without them the fixtures raise `ValueError` and **every** test errors out immediately. Copy `.env.example`, then get a token via `/accounts/users/auth/login`. CI (`pre-pr.yml`) recreates `.env` from GitHub secrets `ANILIBRIA_API_TOKEN`, `LOGIN`, `PASSWORD`. Tests require the `-s` flag because some use stdout/side effects.

## Base URL gotcha

- Client default in `api_client.py` is `https://aniliberty.top/api/v1/` (patched, with a comment that the previous URL stopped working).
- The `base_api_client` test fixture hardcodes `https://anilibria.top/api/v1`.
- These differ — don't assume one domain; check the context when adding endpoints.

## Lint/type conventions (ruff + mypy)

Ruff config lives in `pyproject.toml`: `select = ["ALL"]` (with a long, deliberate ignore list — refer to the file rather than fighting it), `line-length = 79`, double quotes, Google docstrings, `max-complexity = 10`, isort with 2 blank lines after imports. `mypy` sets `disallow_untyped_defs = true` and `warn_unused_ignores = true`, so **all functions must have parameter/return annotations**. Docstrings are Google-style; `D` (docstring) checks are ignored, so missing docstrings don't fail lint.

## Layout & entrypoints

- `anilibria_api_client/api_client.py` — `AsyncAnilibriaAPI`, the main client (how the README instantiates it). Generic `execute()` calls raw endpoints.
- `anilibria_api_client/base_api/api_class.py` — `API`, the raw aiohttp layer. Returns `dict | str | bytes`, turns HTTP 422 into `AnilibriaValidationException`.
- `anilibria_api_client/exceptions.py` — `AnilibriaException`, `AnilibriaValidationException`.
- `anilibria_api_client/helper.py` — auth helper, torrent/anime downloads (uses `aiofiles`, `m3u8_To_MP4`).
- `anilibria_api_client/methods/` — per-endpoint method classes (`base_method.py` has the common `BaseMethod`).
- `anilibria_api_client/models/` — pydantic input/response models (`models/` subpackage per the committed tree).
- `anilibria_api_client/__init__.py` is intentionally empty (`__all__ = []`); import from submodules, e.g. `from anilibria_api_client.api_client import AsyncAnilibriaAPI`.

## Docs

Sphinx docs in `docs/` (furo theme), configured in `.readthedocs.yaml` + `docs/conf.py`. Install with `pip install -e .[docs]` and build with `make html` inside `docs/`.

## Current working tree note

The tree is mid-refactor: `methods/accounts|ads|anime|app|media|teams.py`, `methods/_helper.py`, `methods/_libria.py`, and `models/*` are deleted (still present in git history), `methods/base_method.py` is new, and the per-endpoint attribute assignments in `AsyncAnilibriaAPI.__init__` are commented out. Until this lands, tests in `tests/methods/` and `tests/another/` that import these modules (`models.responses`, `models.legacy_models`, `AsyncBaseAPI`) won't import/run.
