"""Auto-generated AniLiberty methods."""

from __future__ import annotations

from typing import Any

from ....methods._libria import BaseMethod


class GeneratedMediaMethod(BaseMethod):
    async def promotions(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Список промо-материалов

        Возвращает список промо-материалов или рекламные кампании в случайном порядке
        """
        endpoint = "/media/promotions"
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def videos(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None
    ) -> Any:
        """Список видео-роликов

        Возвращает список последних видео-роликов
        """
        endpoint = "/media/videos"
        params = {
        "limit": limit,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)
