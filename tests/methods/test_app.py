import pytest

from anilibria_api_client.api_client import AsyncAnilibriaAPI
from anilibria_api_client.models.responses import *


@pytest.mark.asyncio
async def test_search(
    anilibria_api_client: AsyncAnilibriaAPI,
) -> None:
    search = await anilibria_api_client.app.search_releases("Бездомный бог")
    status = await anilibria_api_client.app.status()

    assert isinstance(search, SearchReleasesResponse)
    assert isinstance(status, StatusResponse)
