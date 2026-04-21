"""Auto-generated public input model facade for AniLiberty OpenAPI.

DO NOT EDIT MANUALLY.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from . import (
    AgeRating,
    CollectionType,
    ContentType,
    ProductionStatusesType,
    PublishStatusesType,
    Seasons,
    SortType,
)


class TimeCode(BaseModel):
    """Legacy request DTO for accounts.users_me_views_timecodes_update."""

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    time: int
    is_watched: bool
    release_episode_id: str


class Release(BaseModel):
    """Legacy request DTO for anime.catalog_releases_get and anime.catalog_releases_post."""

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    page: int | None = None
    limit: int | None = None
    genres: str | None = None
    types: list[ContentType] | None = None
    seasons: list[Seasons] | None = None
    from_year: int | None = None
    to_year: int | None = None
    search: str | None = None
    sorting: SortType | None = None
    age_ratings: list[AgeRating] | None = None
    publish_statuses: list[PublishStatusesType] | None = None
    production_statuses: list[ProductionStatusesType] | None = None
    include: str | None = None
    exclude: str | None = None


class ReleaseCollection(BaseModel):
    """Legacy request DTO for accounts.users_me_collections_releases_get and post."""

    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    type_of_collection: CollectionType
    page: int | None = None
    limit: int | None = None
    genres: str | None = None
    types: list[ContentType] | None = None
    years: str | None = None
    search: str | None = None
    age_ratings: list[AgeRating] | None = None
    include: str | None = None
    exclude: str | None = None


__all__ = [
    "TimeCode",
    "Release",
    "ReleaseCollection",
]
