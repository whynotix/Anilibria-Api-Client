
from ._libria import BaseMethod


class MediaMethod(BaseMethod):
    async def promotions(
        self, include: str | None = None, exclude: str | None = None
    ):
        """
        Возвращает список промо-материалов или рекламные кампании в случайном порядке

        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        return await self._api.get("/media/promotions", params=params)

    async def videos(
        self,
        limit: int | None = None,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает список последних видео-роликов

        :param limit: Лимит возвращаемых полей
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"limit": limit, "include": include, "exclude": exclude}

        return await self._api.get("/media/videos", params=params)
