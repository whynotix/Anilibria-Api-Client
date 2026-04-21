from __future__ import annotations

from typing import Optional

from ..models import ReleaseCollection, TimeCode
from ..types.codegen.methods import GeneratedAccountsMethod
from ..types.codegen.openapi_models import *
from ._helper import validate_collection, validated_json_collection


class AccountsMethod(GeneratedAccountsMethod):
    async def otp_get(
        self,
        device_id: str,
    ) -> "AccountsOtpGet":
        return await super().otp_get(device_id=device_id)

    async def users_auth_social_login(
        self,
        provider: str,
    ) -> "AccountsUsersAuthSocialLogin":
        return await super().users_auth_social_provider_login(provider=provider)

    async def users_me_collections_releases_get(
        self,
        release_collection: ReleaseCollection,
    ) -> "UserCollectionReleasesResponse":
        coll = await validate_collection(params=release_collection)
        return await super().users_me_collections_releases_get(
            page=release_collection.page,
            limit=release_collection.limit,
            type_of_collection=release_collection.type_of_collection.value,
            f_genres_=coll.get("f[genres]"),
            f_types_=coll.get("f[types]"),
            f_years_=coll.get("f[years]"),
            f_search_=coll.get("f[search]"),
            f_age_ratings_=coll.get("f[age_ratings]"),
            include=release_collection.include,
            exclude=release_collection.exclude,
        )

    async def users_me_collections_releases_post(
        self,
        release_collection: ReleaseCollection,
    ) -> "UserCollectionReleasesResponse":
        coll = await validated_json_collection(release=release_collection)
        return await super().users_me_collections_releases_post(
            page=release_collection.page,
            limit=release_collection.limit,
            type_of_collection=release_collection.type_of_collection.value,
            include=release_collection.include,
            exclude=release_collection.exclude,
            f=coll.get("f"),
        )

    async def users_me_collections_add(
        self,
        release_ids: list[int],
    ) -> "UserCollectionsUpdateResponse":
        body = [{"release_id": release_id} for release_id in release_ids]
        return await super().users_me_favorites_post(body=body)

    async def users_me_collections_delete(
        self,
        release_ids: list[int],
    ) -> "UserCollectionsDeleteResponse":
        body = [{"release_id": release_id} for release_id in release_ids]
        return await super().users_me_favorites_delete(body=body)

    async def users_me_views_timecodes(
        self,
        since: Optional[str],
    ) -> "UserViewTimecodesResponse":
        return await super().users_me_views_timecodes_get(since=since)

    async def users_me_views_timecodes_update(
        self,
        timecode_list: list[TimeCode],
    ) -> "UserViewTimecodesResponse":
        body = [timecode.model_dump(mode="json") for timecode in timecode_list]
        return await super().users_me_views_timecodes_post(body=body)

    async def users_me_views_timecodes_delete(
        self,
        episode_id_list: list[str],
    ) -> "UserCollectionsUpdateResponse":
        body = [{"release_episode_id": episode_id} for episode_id in episode_id_list]
        return await super().users_me_views_timecodes_delete(body=body)
