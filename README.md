# Anilibria-Api-Client

[![pypi](https://img.shields.io/badge/anilibria_api_client_on_PyPi-blue)](https://pypi.org/project/anilibria-api-client)
![version](https://img.shields.io/badge/Version-0.2.3-blue)
![licence](https://img.shields.io/badge/License-MIT-green)
![python](https://img.shields.io/badge/Python-3.13%2B-blue)

> [!CAUTION]  
> **It is not an official wrapper.** [Official AniLibria's Swagger](https://anilibria.top/api/docs/v1)

Anilibria-API-Client - this a async client to work with Anilibria API, use a aiohttp. Full writed at python

## Installing

Developed and tested with Python 3.13. While it may work with other versions (oldest and newest), they are not officially supported.

### pip

```bash
$ pip install anilibria-api-client
```

## Usage

```python
from anilibria_api_client.api_client import AsyncAnilibriaAPI # Client
from anilibria_api_client.exceptions import AnilibriaException, AnilibriaValidationException # Errors
from anilibria_api_client.types import * # Types for some methods
from anilibria_api_client.models import * # Input models for some methods
from anilibria_api_client.responses import * # Response models generated from OpenAPI
from anilibria_api_client.helper import * # Download anime, save torrents files and more

async def main():
    async with AsyncAnilibriaAPI() as api:
        await api.teams.users(include="nickname")

    api = AsyncAnilibriaAPI() # like js support
    await api.teams.users(include="nickname")
```

## OpenAPI generation

AniLiberty schema source:

- docs: [https://anilibria.top/api/docs/v1#/](https://anilibria.top/api/docs/v1#/)
- schema: [https://anilibria.top/storage/api/docs/v1?aniliberty-api-v1-docs.json](https://anilibria.top/storage/api/docs/v1?aniliberty-api-v1-docs.json)

Generated artifacts are split from the hand-written client:

- `anilibria_api_client/types/schema/anilibria-v1.openapi.json` - locally cached OpenAPI schema
- `anilibria_api_client/types/codegen/openapi_models.py` - generated Pydantic v2 models and enums
- `anilibria_api_client/types/codegen/methods/` - generated low-level methods split by category
- `anilibria_api_client/types/models.py` - public input/request models
- `anilibria_api_client/types/responses.py` - public response models
- `anilibria_api_client/types/__init__.py` - public enums

Compatibility shims remain at:

- `anilibria_api_client/models.py`
- `anilibria_api_client/responses.py`
- `anilibria_api_client/response_models.py`

Do not edit these files manually:

- `anilibria_api_client/types/codegen/**`
- `anilibria_api_client/types/models.py`
- `anilibria_api_client/types/responses.py`
- `anilibria_api_client/types/__init__.py`

The async client now uses a two-layer method scheme:

- `anilibria_api_client/types/codegen/methods/*.py` - generated low-level endpoint methods grouped by category
- `anilibria_api_client/methods/*.py` - manual compatibility/override layer on top of generated methods

### Local update

Single command to refresh schema and generated files:

```bash
python scripts/update_openapi_models.py
```

Individual steps:

```bash
python scripts/fetch_openapi.py
python scripts/generate_models.py
```

### Drift check

To verify that schema-backed artifacts are up to date:

```bash
python scripts/check_schema_drift.py
```

The check regenerates the schema-backed files and fails if `git status` shows changes in:

- `anilibria_api_client/types/schema/anilibria-v1.openapi.json`
- `anilibria_api_client/types/codegen/`
- `anilibria_api_client/types/models.py`
- `anilibria_api_client/types/responses.py`
- `anilibria_api_client/types/__init__.py`
- `anilibria_api_client/models.py`
- `anilibria_api_client/responses.py`
- `anilibria_api_client/response_models.py`

### CI

The repository includes a dedicated workflow:

- on `pull_request` and `push` to `main`, it runs the drift check and smoke tests
- on weekly schedule and manual dispatch, it refreshes the schema and generated files, runs smoke tests, and opens a PR when a diff is detected

## Documentation 📃

[Docs](https://anilibria-api-client.readthedocs.io/stable/)

## Issues/Contributing

### Issues

Report for any issues [here](https://github.com/semen-bol/Anilibria-Api-Client/issues)

### Contributing

We allow contributing! Read the [CODE_OF_CONDUCT.md](https://github.com/semen-bol/Anilibria-Api-Client/blob/main/CODE_OF_CONDUCT.md)

## License 📄

Anilibria-Api-Client is [MIT](https://github.com/semen-bol/Anilibria-Api-Client/blob/main/LICENSE) licenced.
