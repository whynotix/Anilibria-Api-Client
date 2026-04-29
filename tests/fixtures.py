import os
import typing
import dotenv
import pytest_asyncio

from anilibria_api_client.api_client import AsyncAnilibriaAPI


dotenv.load_dotenv()


@pytest_asyncio.fixture()
async def anilibria_api_client() -> typing.AsyncGenerator[AsyncAnilibriaAPI]:
    token = os.getenv("ANILIBRIA_API_TOKEN")
    if not token:
        raise ValueError("Not ANILIBRIA_API_TOKEN in .env file")

    async with AsyncAnilibriaAPI(token=token) as api:
        yield api
