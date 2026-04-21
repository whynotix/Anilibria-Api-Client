import unittest
import os

from anilibria_api_client.api_client import AsyncAnilibriaAPI
from anilibria_api_client.types import SortType, ProductionStatusesType, PublishStatusesType, ContentType
from anilibria_api_client.models import Release
from anilibria_api_client.exceptions import AnilibriaException
from anilibria_api_client.helper import auto_paginate, async_download, auth, download_torrent_file
from unittest import IsolatedAsyncioTestCase
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor


class Help:
    async def auth(self, api_without_auth: AsyncAnilibriaAPI):
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
        api = AsyncAnilibriaAPI()

        try:
            # Download all series via api
            anime = await api.anime.catalog_releases_get(Release(search="аристократа"))
            anime_id = anime.get("data")[0]['id']
            
            release = await api.anime.releases_idOrAlias(anime_id)

            executor = ThreadPoolExecutor(os.cpu_count() - 2)
            for episode in release.get("episodes"):
                link = episode.get("hls_1080") if episode.get("hls_1080") is not None else (
                    episode.get("hls_720") if episode.get("hls_720") is not None else (
                        episode.get("hls_480") if episode.get("hls_480") is not None else None
                    )
                )
                if link is not None:
                    await async_download(
                        url=link, 
                        filename=episode.get("name") if episode.get("name") is not None else episode.get("ordinal") + ".mp4"
                    )

            # Download torrent file via api
            anime = await api.anime.catalog_releases_get(Release(search="аристократа"))
            anime = anime.get("data")

            anime_id = anime[0]['id']

            torrents = await api.anime.torrents_release_releaseId(anime_id)
            torrent = torrents[0]

            torrent_hash = await api.anime.torrents_hashOrId_file(torrent.get("hash"))
            download_status = await download_torrent_file(torrent_hash, torrent.get("label"))

            pprint(download_status)
            
        except AnilibriaException as e:
            raise e
        
        return True

if __name__ == "__main__":
    unittest.main()