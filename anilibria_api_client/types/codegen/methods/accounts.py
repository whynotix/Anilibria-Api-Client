"""Auto-generated AniLiberty methods."""

from __future__ import annotations

from typing import Any

from ....methods._libria import BaseMethod


class GeneratedAccountsMethod(BaseMethod):
    async def otp_accept(
            self,
            code: int
    ) -> Any:
        """Присоединяем пользователя к выданному OTP

        Присоединяем пользователя к выданному одноразовому паролю
        """
        endpoint = "/accounts/otp/accept"
        params = None
        json_data = {
        "code": code,
        }
        return await self._api.post(endpoint, json_data=json_data)

    async def otp_get(
            self,
            device_id: str
    ) -> Any:
        """Запрашивает OTP

        Запрашиваем новый одноразовый пароль
        """
        endpoint = "/accounts/otp/get"
        params = None
        json_data = {
        "device_id": device_id,
        }
        return await self._api.post(endpoint, json_data=json_data)

    async def otp_login(
            self,
            code: int,
            device_id: str
    ) -> Any:
        """Авторизуемся по OTP

        Авторизуемся по выданному одноразовому паролю
        """
        endpoint = "/accounts/otp/login"
        params = None
        json_data = {
        "code": code,
        "device_id": device_id,
        }
        return await self._api.post(endpoint, json_data=json_data)

    async def users_auth_login(
            self,
            login: str,
            password: str
    ) -> Any:
        """Авторизация пользователя

        Авторизация пользователя по логину и паролю. Создание сессии пользователя, выдача токена авторизации для использования в cookies или в Bearer Token
        """
        endpoint = "/accounts/users/auth/login"
        params = None
        json_data = {
        "login": login,
        "password": password,
        }
        return await self._api.post(endpoint, json_data=json_data)

    async def users_auth_logout(
            self
    ) -> Any:
        """Деавторизация пользователя

        Деавторизовать пользователя
        """
        endpoint = "/accounts/users/auth/logout"
        params = None
        json_data = None
        return await self._api.post(endpoint)

    async def users_auth_password_forget(
            self,
            email: str
    ) -> Any:
        """Восстановление пароля

        Отправление ссылки на восстановление забытого пароля
        """
        endpoint = "/accounts/users/auth/password/forget"
        params = None
        json_data = {
        "email": email,
        }
        return await self._api.post(endpoint, json_data=json_data)

    async def users_auth_password_reset(
            self,
            password: str,
            password_confirmation: str,
            token: str
    ) -> Any:
        """Сброс и установка нового пароля

        Сброс и установка нового пароля
        """
        endpoint = "/accounts/users/auth/password/reset"
        params = None
        json_data = {
        "password": password,
        "password_confirmation": password_confirmation,
        "token": token,
        }
        return await self._api.post(endpoint, json_data=json_data)

    async def users_auth_social_authenticate(
            self,
            state: str
    ) -> Any:
        """Аутентифицировать пользователя через социальные сети

        Позволяет аутентифицировать авторизованного через социальную сеть пользователя
        """
        endpoint = "/accounts/users/auth/social/authenticate"
        params = {
        "state": state,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_auth_social_provider_login(
            self,
            provider: Any
    ) -> Any:
        """Авторизация пользователя через социальные сети

        Позволяет авторизовать пользователя через некоторые социальные сети
        """
        endpoint = self._api.build_endpoint_with_params("/accounts/users/auth/social/{provider}/login", provider=provider)
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_collections_delete(
            self,
            body: list[dict[str, Any]]
    ) -> Any:
        """Удалить релизы из коллекций

        Удаляет релизы из соответствующих коллекций авторизованного пользователя
        """
        endpoint = "/accounts/users/me/collections"
        params = None
        return await self._api.delete(endpoint, json_data=body)

    async def users_me_collections_post(
            self,
            body: list[dict[str, Any]]
    ) -> Any:
        """Добавить релизы в коллекции

        Добавляет релизы в соответствующие коллекции авторизованного пользователя
        """
        endpoint = "/accounts/users/me/collections"
        params = None
        return await self._api.post(endpoint, json_data=body)

    async def users_me_collections_ids(
            self
    ) -> Any:
        """Список идентификаторов релизов добавленных в коллекции

        Возвращает данные по идентификаторам релизов и типов коллекций авторизованного пользователя
        """
        endpoint = "/accounts/users/me/collections/ids"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_collections_references_age_ratings(
            self
    ) -> Any:
        """Список возрастных рейтингов в коллекциях пользователя

        Возвращает список возрастных рейтингов в коллекциях текущего пользователя
        """
        endpoint = "/accounts/users/me/collections/references/age-ratings"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_collections_references_genres(
            self
    ) -> Any:
        """Список жанров в коллекциях пользователя

        Возвращает список жанров в коллекциях текущего пользователя
        """
        endpoint = "/accounts/users/me/collections/references/genres"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_collections_references_types(
            self
    ) -> Any:
        """Список типов в коллекциях пользователя

        Возвращает список типов в коллекциях текущего пользователя
        """
        endpoint = "/accounts/users/me/collections/references/types"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_collections_references_years(
            self
    ) -> Any:
        """Список годов в коллекциях пользователя

        Возвращает список годов в коллекциях текущего пользователя
        """
        endpoint = "/accounts/users/me/collections/references/years"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_collections_releases_get(
            self,
            type_of_collection: Any,
            exclude: list[str] | str | None = None,
            f_age_ratings_: list[Any] | None = None,
            f_genres_: Any | None = None,
            f_search_: Any | None = None,
            f_types_: list[Any] | None = None,
            f_years_: Any | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None,
            page: int | None = None
    ) -> Any:
        """Список релизов добавленных в коллекцию [GET]

        Возвращает данные по релизам из определенной коллекции авторизованного пользователя
        """
        endpoint = "/accounts/users/me/collections/releases"
        params = {
        "page": page,
        "limit": limit,
        "type_of_collection": type_of_collection,
        "f[genres]": f_genres_,
        "f[types]": f_types_,
        "f[years]": f_years_,
        "f[search]": f_search_,
        "f[age_ratings]": f_age_ratings_,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_collections_releases_post(
            self,
            exclude: str | None = None,
            f: dict[str, Any] | None = None,
            include: str | None = None,
            limit: int | None = None,
            page: int | None = None,
            type_of_collection: Any | None = None
    ) -> Any:
        """Список релизов добавленных в коллекцию [POST]

        Возвращает данные по релизам из определенной коллекции авторизованного пользователя
        """
        endpoint = "/accounts/users/me/collections/releases"
        params = None
        json_data = {
        "exclude": exclude,
        "f": f,
        "include": include,
        "limit": limit,
        "page": page,
        "type_of_collection": type_of_collection,
        }
        return await self._api.post(endpoint, json_data=json_data)

    async def users_me_favorites_delete(
            self,
            body: list[dict[str, Any]]
    ) -> Any:
        """Удалить релизы из избранного

        Удаляет релизы из избранного авторизованного пользователя
        """
        endpoint = "/accounts/users/me/favorites"
        params = None
        return await self._api.delete(endpoint, json_data=body)

    async def users_me_favorites_post(
            self,
            body: list[dict[str, Any]]
    ) -> Any:
        """Добавить релизы в избранное

        Добавляет релизы в избранное авторизованного пользователя
        """
        endpoint = "/accounts/users/me/favorites"
        params = None
        return await self._api.post(endpoint, json_data=body)

    async def users_me_favorites_ids(
            self
    ) -> Any:
        """Список идентификаторов релизов добавленных в избранное

        Возвращает данные по идентификаторам релизов из избранного авторизованного пользователя
        """
        endpoint = "/accounts/users/me/favorites/ids"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_favorites_references_age_ratings(
            self
    ) -> Any:
        """Список возрастных рейтингов в избранном пользователя

        Возвращает список возрастных рейтингов в избранном текущего пользователя
        """
        endpoint = "/accounts/users/me/favorites/references/age-ratings"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_favorites_references_genres(
            self
    ) -> Any:
        """Список жанров в избранном пользователя

        Возвращает список жанров в избранном текущего пользователя
        """
        endpoint = "/accounts/users/me/favorites/references/genres"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_favorites_references_sorting(
            self
    ) -> Any:
        """Список опций сортировки в избранном пользователя

        Возвращает список опций сортировки в избранном текущего пользователя
        """
        endpoint = "/accounts/users/me/favorites/references/sorting"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_favorites_references_types(
            self
    ) -> Any:
        """Список типов релизов в избранном пользователя

        Возвращает список типов релизов в избранном текущего пользователя
        """
        endpoint = "/accounts/users/me/favorites/references/types"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_favorites_references_years(
            self
    ) -> Any:
        """Список годов выхода релизов в избранном пользователя

        Возвращает список годов выхода релизов в избранном текущего пользователя
        """
        endpoint = "/accounts/users/me/favorites/references/years"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_favorites_releases_get(
            self,
            exclude: list[str] | str | None = None,
            f_age_ratings_: list[Any] | None = None,
            f_genres_: Any | None = None,
            f_search_: Any | None = None,
            f_sorting_: Any | None = None,
            f_types_: list[Any] | None = None,
            f_years_: Any | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None,
            page: int | None = None
    ) -> Any:
        """Список релизов в избранном пользователя

        Возвращает данные по релизам из избранного текущего пользователя
        """
        endpoint = "/accounts/users/me/favorites/releases"
        params = {
        "page": page,
        "limit": limit,
        "f[years]": f_years_,
        "f[types]": f_types_,
        "f[genres]": f_genres_,
        "f[search]": f_search_,
        "f[sorting]": f_sorting_,
        "f[age_ratings]": f_age_ratings_,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_favorites_releases_post(
            self,
            exclude: str | None = None,
            f: dict[str, Any] | None = None,
            include: str | None = None,
            limit: int | None = None,
            page: int | None = None
    ) -> Any:
        """Список релизов в избранном пользователя

        Возвращает данные по релизам из избранного текущего пользователя
        """
        endpoint = "/accounts/users/me/favorites/releases"
        params = None
        json_data = {
        "exclude": exclude,
        "f": f,
        "include": include,
        "limit": limit,
        "page": page,
        }
        return await self._api.post(endpoint, json_data=json_data)

    async def users_me_profile(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Профиль авторизованного пользователя

        Возвращает данные профиля авторизованного пользователя
        """
        endpoint = "/accounts/users/me/profile"
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_views_history(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None,
            page: int | None = None
    ) -> Any:
        """История просмотренных эпизодов

        Возвращает историю просмотров эпизодов авторизованного пользователя
        """
        endpoint = "/accounts/users/me/views/history"
        params = {
        "page": page,
        "limit": limit,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_views_timecodes_delete(
            self,
            body: list[dict[str, Any]]
    ) -> Any:
        """Удаление таймкодов просмотра эпизодов

        Удаляет данные по таймкодам просмотров для указанных эпизодов
        """
        endpoint = "/accounts/users/me/views/timecodes"
        params = None
        return await self._api.delete(endpoint, json_data=body)

    async def users_me_views_timecodes_get(
            self,
            since: str | None = None
    ) -> Any:
        """Таймкоды просмотренных эпизодов

        Возвращает таймкоды по прогрессу просмотренных эпизодов
        """
        endpoint = "/accounts/users/me/views/timecodes"
        params = {
        "since": since,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def users_me_views_timecodes_post(
            self,
            body: list[dict[str, Any]]
    ) -> Any:
        """Обновление таймкодов прогресса просмотренного эпизода

        Обновляет таймкоды просмотренных эпизодов
        """
        endpoint = "/accounts/users/me/views/timecodes"
        params = None
        return await self._api.post(endpoint, json_data=body)
