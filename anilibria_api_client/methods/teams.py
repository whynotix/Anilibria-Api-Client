
from ._libria import BaseMethod


class TeamsMethod(BaseMethod):
    async def get(
        self, include: str | None = None, exclude: str | None = None
    ):
        """
        Возвращает список всех команд

        Args:
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        return await self._api.get("/teams/", params=params)

    async def roles(
        self, include: str | None = None, exclude: str | None = None
    ):
        """
        Возвращает список всех ролей в командах

        Args:
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        return await self._api.get("/teams/roles", params=params)

    async def users(
        self, include: str | None = None, exclude: str | None = None
    ):
        """
        Возвращает список всех анилибрийцов с указанием команды и своих ролей

        Args:
            include: Поля для включения
            exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        return await self._api.get("/teams/users", params=params)
