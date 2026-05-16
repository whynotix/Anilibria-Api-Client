from anilibria_api_client.models.responses.app import *

from ._libria import BaseMethod


class AppMethod(BaseMethod):
    async def search_releases(
        self,
        query: str,
        include: str | None = None,
        exclude: str | None = None,
    ) -> "SearchReleasesResponse":
        """
        Возвращает данные по релизам, которые удовлетворяют поисковому запросу

        :param query: Обязательный параметр. Строка поиска
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"query": query, "include": include, "exclude": exclude}

        response = await self._api.get("/app/search/releases", params=params)
        return SearchReleasesResponse(data=response)

    async def status(self) -> "StatusResponse":
        """
        Возвращает информацию о статусе API
        """
        response = await self._api.get("/app/status")
        return StatusResponse(**response)
