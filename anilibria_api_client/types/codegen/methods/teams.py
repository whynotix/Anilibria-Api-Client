"""Auto-generated AniLiberty methods."""

from __future__ import annotations

from typing import Any

from ....methods._libria import BaseMethod


class GeneratedTeamsMethod(BaseMethod):
    async def get(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Список команд АниЛибрии

        Возвращает список всех команд
        """
        endpoint = "/teams/"
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def roles(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Список ролей

        Возвращает список всех ролей в командах
        """
        endpoint = "/teams/roles"
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Список анилибрийцов

        Возвращает список всех анилибрийцов с указанием команды и своих ролей
        """
        endpoint = "/teams/users"
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)
