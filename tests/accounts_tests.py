import unittest

from anilibria_api_client.api_client import AsyncAnilibriaAPI
from anilibria_api_client.exceptions import AnilibriaException
from anilibria_api_client.types import CollectionType, ContentType, AgeRating
from anilibria_api_client.models import TimeCode, ReleaseCollection
from unittest import IsolatedAsyncioTestCase
from pprint import pprint
from datetime import datetime, timezone


class Help:
    async def auth(self, api_without_auth: AsyncAnilibriaAPI = AsyncAnilibriaAPI()):
        try:
            login = str(input("Введите логин: "))
            password = str(input("Введите пароль: "))
            
            res = await api_without_auth.accounts.users_auth_login(login=login, password=password)

            return res.get("token")
        except AnilibriaException as e:
            print("Введены неправильные данные, попробуйте еще раз!")

            return await self.auth(api_without_auth=api_without_auth)

class Test(IsolatedAsyncioTestCase):
    async def test(self):
        token = await Help().auth()
        api_auth = AsyncAnilibriaAPI(authorization=f"Bearer {token}")
        releases = await api_auth.accounts.users_me_collections_releases_post(
            release_collection=ReleaseCollection(
                type_of_collection=CollectionType.PLANNED,
                page=1,
                limit=10,
                genres="14,29",
                types=[ContentType.MOVIE],
                years="2017",
                search="Мастера Меча Онлайн: Порядковый ранг",
                age_ratings=[AgeRating.R16_PLUS],
                include="id,name.main,genres.name"
            )
        )
        releases_get = await api_auth.accounts.users_me_collections_releases_get(
            release_collection=ReleaseCollection(
                type_of_collection=CollectionType.PLANNED,
                page=1,
                limit=10,
                genres="14,29",
                types=[ContentType.MOVIE],
                years="2017",
                search="Мастера Меча Онлайн: Порядковый ранг",
                age_ratings=[AgeRating.R16_PLUS],
                include="id,name.main,genres.name"
            )
        )

        pprint(releases)
        pprint(releases_get)

        """api = AsyncAnilibriaAPI()
        result = await api.accounts.otp_get("123")
        pprint(result)"""
        

if __name__ == "__main__":
    unittest.main()