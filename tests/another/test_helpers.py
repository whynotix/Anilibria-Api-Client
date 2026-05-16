import pytest

from anilibria_api_client import helper
from anilibria_api_client.api_client import AsyncAnilibriaAPI
from anilibria_api_client.models.responses import *


@pytest.mark.asyncio
async def test_auth(
    anilibria_api_client: AsyncAnilibriaAPI,
) -> None:
    response = await helper.auth(
        api=anilibria_api_client, login="test", password="test"
    )

    assert isinstance(response, AsyncAnilibriaAPI)
