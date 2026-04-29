import pytest

from anilibria_api_client.api_client import AsyncAnilibriaAPI
from anilibria_api_client.models import (
    AgeRating,
    CollectionType,
    ContentType,
    ReleaseCollection,
    UsersMeCollectionsReleasesResponse,
)


@pytest.mark.asyncio
async def test_releases_get_post(
    anilibria_api_client: AsyncAnilibriaAPI,
) -> None:
    releases_get = (
        await anilibria_api_client.accounts.users_me_collections_releases_get(
            release_collection=ReleaseCollection(
                type_of_collection=CollectionType.PLANNED,
                page=1,
                limit=10,
                genres="14,29",
                types=[ContentType.MOVIE],
                years="2017",
                search="Мастера Меча Онлайн: Порядковый ранг",
                age_ratings=[AgeRating.R16_PLUS],
                include="",
            )
        )
    )

    releases_post = (
        await anilibria_api_client.accounts.users_me_collections_releases_post(
            release_collection=ReleaseCollection(
                type_of_collection=CollectionType.PLANNED,
                page=1,
                limit=10,
                genres="14,29",
                types=[ContentType.MOVIE],
                years="2017",
                search="Мастера Меча Онлайн: Порядковый ранг",
                age_ratings=[AgeRating.R16_PLUS],
                include="",
            )
        )
    )

    assert isinstance(releases_get, UsersMeCollectionsReleasesResponse)
    assert isinstance(releases_post, UsersMeCollectionsReleasesResponse)
