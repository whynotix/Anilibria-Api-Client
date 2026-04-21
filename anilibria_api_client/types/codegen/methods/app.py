"""Auto-generated AniLiberty methods."""

from __future__ import annotations

from typing import Any

from ....methods._libria import BaseMethod


class GeneratedAppMethod(BaseMethod):
    async def search_releases(
            self,
            query: str,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Поиск релизов

        Возвращает данные по релизам, которые удовлетворяют поисковому запросу
        """
        endpoint = "/app/search/releases"
        params = {
        "query": query,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def status(
            self
    ) -> Any:
        """Статус API

        Возвращает информацию о статусе API
        """
        endpoint = "/app/status"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)
