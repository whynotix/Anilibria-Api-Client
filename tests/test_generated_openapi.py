from __future__ import annotations

from enum import Enum
from importlib import import_module

from pydantic import BaseModel


def test_generated_module_imports() -> None:
    module = import_module("anilibria_api_client.types.codegen.openapi_models")
    assert module is not None


def test_public_facades_import() -> None:
    models_module = import_module("anilibria_api_client.models")
    responses_module = import_module("anilibria_api_client.responses")
    response_models_module = import_module("anilibria_api_client.response_models")
    types_module = import_module("anilibria_api_client.types")
    assert models_module is not None
    assert responses_module is not None
    assert response_models_module is not None
    assert types_module is not None


def test_known_generated_exports_are_available() -> None:
    generated = import_module("anilibria_api_client.types.codegen.openapi_models")
    public_models = import_module("anilibria_api_client.models")
    public_responses = import_module("anilibria_api_client.responses")
    public_response_models = import_module("anilibria_api_client.response_models")
    public_types = import_module("anilibria_api_client.types")

    assert issubclass(generated.AnimeRelease, BaseModel)
    assert issubclass(generated.AnimeCatalogReleasesResponse, BaseModel)
    assert issubclass(public_types.CollectionType, Enum)
    assert issubclass(public_types.ContentType, Enum)
    assert hasattr(public_responses, "AnimeRelease")
    assert hasattr(public_response_models, "AnimeRelease")
    assert hasattr(public_response_models, "AnimeCatalogReleasesResponse")
    assert not hasattr(public_models, "AnimeRelease")


def test_legacy_public_api_is_preserved() -> None:
    public_models = import_module("anilibria_api_client.models")
    public_types = import_module("anilibria_api_client.types")

    release = public_models.Release(search="test", types=[public_types.ContentType.MOVIE])
    collection = public_models.ReleaseCollection(type_of_collection=public_types.CollectionType.PLANNED)
    timecode = public_models.TimeCode(time=1, is_watched=True, release_episode_id="episode-id")

    assert release.search == "test"
    assert release.types == [public_types.ContentType.MOVIE]
    assert collection.type_of_collection is public_types.CollectionType.PLANNED
    assert timecode.model_dump()["release_episode_id"] == "episode-id"


def test_public_exports_include_known_names() -> None:
    public_models = import_module("anilibria_api_client.models")
    public_responses = import_module("anilibria_api_client.responses")
    public_response_models = import_module("anilibria_api_client.response_models")
    public_types = import_module("anilibria_api_client.types")

    assert "Release" in public_models.__all__
    assert "ReleaseCollection" in public_models.__all__
    assert "AnimeRelease" in public_responses.__all__
    assert "AnimeRelease" in public_response_models.__all__
    assert "CollectionType" in public_types.__all__
    assert "ContentType" in public_types.__all__
