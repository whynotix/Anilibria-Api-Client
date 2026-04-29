import logging
from typing import Any

import aiohttp

from .base_api.api_class import AsyncBaseAPI
from .methods import (
    AccountsMethod,
    AdsMethod,
    AnimeMethod,
    AppMethod,
    MediaMethod,
    TeamsMethod,
)


logging.basicConfig(level=logging.ERROR)


class AsyncAnilibriaAPI(AsyncBaseAPI):
    """
    Асинхронный клиент для работы с AnilibriaAPI, базируется на AsyncBaseAPI (base_api/api_class.py)
    """

    def __init__(
        self,
        base_url: str = "https://anilibria.top/api/v1",
        token: str | None = None,
        proxy: str | None = None,
        proxy_auth: aiohttp.BasicAuth | None = None,
        proxy_headers: dict[str, str] | None = None,
    ) -> None:
        """
        Инициализация асинхронного API клиента.

        :param base_url: Базовый URL API
        :param token: Токен для авторизации (Bearer)

        :param proxy: URL прокси-сервера (http://proxy:port или https://proxy:port)
        :param proxy_auth: Аутентификация для прокси (BasicAuth)
        :param proxy_headers: Заголовки для прокси
        """

        headers = {
            "Content-Type": "application/json",
        }
        if token is not None:
            headers["Authorization"] = f"Bearer {token}"

        super().__init__(
            base_url=base_url,
            headers=headers,
            proxy=proxy,
            proxy_auth=proxy_auth,
            proxy_headers=proxy_headers,
        )

        self.accounts = AccountsMethod(api=self)
        self.ads = AdsMethod(api=self)
        self.anime = AnimeMethod(api=self)
        self.app = AppMethod(api=self)
        self.media = MediaMethod(api=self)
        self.teams = TeamsMethod(api=self)

    async def execute(
        self,
        endpoint: str,
        method: str = "GET",
        data: dict[str, Any] | str | bytes | None = None,
        json_data: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
        **kwargs,
    ) -> dict[str, Any] | str | bytes:
        """
        Создание своего уникального запроса

        :param method: Метод используемый для запроса, например GET (обязательно)
        :param endpoint: Конечная точка API (обязательно)
        :param data: Тело запроса
        :param json_data: JSON тело запроса
        :param headers: Дополнительные заголовки
        :param kwargs: Дополнительные аргументы для aiohttp
        :return: Ответ от API
        """

        return await self._request(
            method,
            endpoint,
            data=data,
            json_data=json_data,
            headers=headers,
            **kwargs,
        )
