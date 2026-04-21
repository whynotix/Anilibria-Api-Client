from __future__ import annotations

from ..models import Release
from ..types.codegen.methods import GeneratedAnimeMethod
from ._helper import create_filters_from_release, validate_filters


class AnimeMethod(GeneratedAnimeMethod):
    async def catalog_releases_get(
        self,
        params: Release,
    ):
        filters = await validate_filters(params=params)
        return await super().catalog_releases_get(
            page=params.page,
            limit=params.limit,
            f_genres_=filters.get("f[genres]"),
            f_types_=filters.get("f[types]"),
            f_seasons_=filters.get("f[seasons]"),
            f_search_=filters.get("f[search]"),
            f_sorting_=filters.get("f[sorting]"),
            f_age_ratings_=filters.get("f[age_ratings]"),
            f_publish_statuses_=filters.get("f[publish_statuses]"),
            f_production_statuses_=filters.get("f[production_statuses]"),
            f_years__from_year_=filters.get("f[from_year]"),
            f_years__to_year_=filters.get("f[to_year]"),
            include=params.include,
            exclude=params.exclude,
        )

    async def catalog_releases_post(
        self,
        params: Release,
    ):
        filters = await create_filters_from_release(params)
        return await super().catalog_releases_post(
            page=params.page,
            limit=params.limit,
            include=params.include,
            exclude=params.exclude,
            f=filters.get("f"),
        )

    async def torrents_hashOrId_file(
        self,
        hashOrId: str,
        pk: str | None = None,
    ):
        params = {"pk": pk}
        headers = {
            "Content-Type": "application/x-bittorrent; utf-8",
            "Accept": "application/x-bittorrent",
        }
        endpoint = self._api.build_endpoint_with_params("/anime/torrents/{hashOrId}/file", hashOrId=hashOrId)
        return await self._api.get(endpoint, params=params, headers=headers)

    async def torrents_rss(
        self,
        limit: int | None = None,
        pk: str | None = None,
    ):
        params = {"limit": limit, "pk": pk}
        headers = {"Content-Type": "application/xml"}
        return await self._api.get("/anime/torrents/rss", params=params, headers=headers)

    async def torrents_rss_release_releaseId(
        self,
        releaseId: int,
        pk: str | None = None,
    ):
        params = {"pk": pk}
        headers = {"Content-Type": "application/xml"}
        endpoint = self._api.build_endpoint_with_params("/anime/torrents/rss/release/{releaseId}", releaseId=releaseId)
        return await self._api.get(endpoint=endpoint, params=params, headers=headers)
