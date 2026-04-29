
from ._libria import BaseMethod


class AppMethod(BaseMethod):
    async def search_releases(
        self,
        query: str,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по релизам, которые удовлетворяют поисковому запросу

        :param query: Обязательный параметр. Строка поиска
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"query": query, "include": include, "exclude": exclude}

        return await self._api.get("/app/search/releases", params=params)

    async def status(self):
        """
        Возвращает информацию о статусе API
        """
        return await self._api.get("/app/status")
