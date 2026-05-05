from typing import NoReturn

from anilibria_api_client.models import ReleaseCollection, TimeCode
from anilibria_api_client.models.responses.accounts import *

from ._helper import validate_collection, validated_json_collection
from ._libria import BaseMethod


class AccountsMethod(BaseMethod):
    async def otp_get(self, device_id: str) -> "OtpGetResponse":
        """
        Запрашиваем новый одноразовый пароль

        :param device_id: ID девайса (необходим)
        """

        data = {"device_id": device_id}

        response = await self._api.post("/accounts/otp/get", json_data=data)
        return OtpGetResponse(**response)

    async def otp_accept(self, code: int) -> NoReturn:
        """
        Присоединяем пользователя к выданному одноразовому паролю

        :param code: Код девайса (необходим)
        """

        data = {"code": code}

        await self._api.post("/accounts/otp/accept", json_data=data)
        return NoReturn

    async def otp_login(self, code: int, device_id: str) -> "OtpLoginResponse":
        """
        Авторизуемся по выданному одноразовому паролю

        :param code: Код девайса (необходим)
        :param device_id: ID девайса (необходим)
        """

        data = {"code": code, "device_id": device_id}

        response = await self._api.post("/accounts/otp/login", json_data=data)
        return OtpLoginResponse(**response)

    async def users_auth_login(
        self,
        login: str,
        password: str,
    ) -> "UsersAuthLoginResponse":
        """
        Авторизация пользователя по логину и паролю. Создание сессии пользователя, выдача токена авторизации для использования в cookies или в Bearer Token

        :param login: Логин аккаунта (необходим)
        :param password: Пароль аккаунта (необходим)
        """

        data = {"login": login, "password": password}

        response = await self._api.post(
            "/accounts/users/auth/login", json_data=data
        )
        return UsersAuthLoginResponse(**response)

    async def users_auth_logout(self) -> "UsersAuthLogoutResponse":
        """
        Деавторизовать пользователя
        """
        response = await self._api.post("/accounts/users/auth/login")
        return UsersAuthLogoutResponse(**response)

    async def users_auth_social_login(
        self,
        provider: str,
    ) -> "UsersAuthSocialProviderLoginResponse":
        """
        Позволяет авторизовать пользователя через некоторые социальные сети

        :param provider: Провайдер социальной сети vk, google, patreon, discord (необходим)
        """
        response = await self._api.get(
            f"/accounts/users/auth/social/{provider}/login"
        )
        return UsersAuthSocialProviderLoginResponse(**response)

    async def users_auth_social_authenticate(
        self, state: str
    ) -> "UsersAuthSocialAuthenticateResponse":
        """
        Позволяет аутентифицировать авторизованного через социальную сеть пользователя

        :param state: Ключ аутентификации users_auth_social_login (необходим)
        """
        query = {"state": state}

        response = await self._api.get(
            "/accounts/users/auth/social/authenticate", params=query
        )
        return UsersAuthSocialAuthenticateResponse(**response)

    async def users_auth_password_forget(self, email: str) -> NoReturn:
        """
        Отправление ссылки на восстановление забытого пароля

        :param email: Email аккаунта
        """

        data = {"email": email}

        return await self._api.post(
            "/accounts/users/auth/password/forget", json_data=data
        )

    async def users_auth_password_reset(
        self, token: str, password: str, password_confirmation: str
    ) -> NoReturn:
        """
        Сброс и установка нового пароля

        :param token: Токен с email
        :param password: Пароль
        :param password_confirmation: Подтверждение пароля
        """

        data = {
            "token": token,
            "password": password,
            "password_confirmation": password_confirmation,
        }

        return await self._api.post(
            "/accounts/users/auth/password/reset", json_data=data
        )

    async def users_me_collections_references_age_ratings(
        self,
    ) -> "UsersMeCollectionsReferencesAgeRatingsResponse":
        """
        Возвращает список возрастных рейтингов в коллекциях текущего пользователя (auth need)
        """

        response = await self._api.get(
            "/accounts/users/me/collections/references/age-ratings"
        )
        return UsersMeCollectionsReferencesAgeRatingsResponse(data=response)

    async def users_me_collections_references_genres(
        self,
    ) -> "UsersMeCollectionsReferencesGenresResponse":
        """
        Возвращает список жанров в коллекциях текущего пользователя (auth need)
        """

        response = await self._api.get(
            "/accounts/users/me/collections/references/genres"
        )
        return UsersMeCollectionsReferencesGenresResponse(data=response)

    async def users_me_collections_references_types(
        self,
    ) -> "UsersMeCollectionsReferencesTypesResponse":
        """
        Возвращает список типов в коллекциях текущего пользователя (auth need)
        """

        response = await self._api.get(
            "/accounts/users/me/collections/references/types"
        )
        return UsersMeCollectionsReferencesTypesResponse(data=response)

    async def users_me_collections_references_years(
        self,
    ) -> "UsersMeCollectionsReferencesYearsResponse":
        """
        Возвращает список годов в коллекциях текущего пользователя (auth need)
        """
        response = await self._api.get(
            "/accounts/users/me/collections/references/years"
        )
        return UsersMeCollectionsReferencesYearsResponse(data=response)

    async def users_me_collections_ids(
        self,
    ) -> "UsersMeCollectionsIdsResponse":
        """
        Возвращает данные по идентификаторам релизов и типов коллекций авторизованного пользователя
        """
        response = await self._api.get("/accounts/users/me/collections/ids")
        return UsersMeCollectionsIdsResponse(data=response)

    async def users_me_collections_releases_get(
        self, release_collection: ReleaseCollection
    ) -> "UsersMeCollectionsReleasesResponse":
        """
        Возвращает данные по релизам из определенной коллекции авторизованного пользователя

        :param release_collection: тело ReleaseCollection
        """
        params = {
            "page": release_collection.page,
            "limit": release_collection.limit,
            "type_of_collection": release_collection.type_of_collection.value,
            "include": release_collection.include,
            "exclude": release_collection.exclude,
        }

        coll = await validate_collection(params=release_collection)
        final_params = {**params, **coll}

        result = await self._api.get(
            "/accounts/users/me/collections/releases", params=final_params
        )
        return UsersMeCollectionsReleasesResponse(**result)

    async def users_me_collections_releases_post(
        self, release_collection: ReleaseCollection
    ) -> "UsersMeCollectionsReleasesResponse":
        """
        Возвращает данные по релизам из определенной коллекции авторизованного пользователя

        :param release_collection: тело ReleaseCollection
        """
        json = {
            "page": release_collection.page,
            "limit": release_collection.limit,
            "type_of_collection": release_collection.type_of_collection.value,
            "include": release_collection.include,
            "exclude": release_collection.exclude,
        }

        coll = await validated_json_collection(release=release_collection)
        final_json = {**json, **coll}

        result = await self._api.post(
            "/accounts/users/me/collections/releases", json_data=final_json
        )
        return UsersMeCollectionsReleasesResponse(**result)

    async def users_me_collections_add(
        self, release_ids: list[int]
    ) -> "UsersMeCollectionsResponse":
        """
        Добавляет релизы в соответствующие коллекции авторизованного пользователя

        :param release_id: ID релиза
        """
        params = [{"release_id": a} for a in release_ids]

        response = await self._api.post(
            "/accounts/users/me/collections", json_data=params
        )
        return UsersMeCollectionsResponse(**response)

    async def users_me_collections_delete(
        self, release_ids: list[int]
    ) -> "UsersMeCollectionsResponse":
        """
        Удаляет релизы из соответствующих коллекций авторизованного пользователя

        :param release_id: ID релиза
        """
        params = [{"release_id": a} for a in release_ids]

        response = await self._api.delete(
            "/accounts/users/me/collections", json_data=params
        )
        return UsersMeCollectionsResponse(**response)

    async def users_me_favorites_references_age_ratings(
        self,
    ) -> "UsersMeFavoritesReferencesAgeRatingsResponse":
        """
        Возвращает список возрастных рейтингов в избранном текущего пользователя
        """
        result = await self._api.get(
            "/accounts/users/me/favorites/references/age-ratings"
        )
        return UsersMeFavoritesReferencesAgeRatingsResponse(data=result)

    async def users_me_favorites_references_genres(
        self,
    ) -> "UsersMeFavoritesReferencesGenresResponse":
        """
        Возвращает список жанров в избранном текущего пользователя
        """
        result = await self._api.get(
            "/accounts/users/me/favorites/references/genres"
        )
        return UsersMeFavoritesReferencesGenresResponse(data=result)

    async def users_me_favorites_references_sorting(
        self,
    ) -> "UsersMeFavoritesReferencesSortingResponse":
        """
        Возвращает список опций сортировки в избранном текущего пользователя
        """
        result = await self._api.get(
            "/accounts/users/me/favorites/references/sorting"
        )
        return UsersMeFavoritesReferencesSortingResponse(data=result)

    async def users_me_favorites_references_types(
        self,
    ) -> "UsersMeFavoritesReferencesTypesResponse":
        """
        Возвращает список типов релизов в избранном текущего пользователя
        """
        result = await self._api.get(
            "/accounts/users/me/favorites/references/types"
        )
        return UsersMeFavoritesReferencesTypesResponse(data=result)

    async def users_me_favorites_references_years(
        self,
    ) -> "UsersMeFavoritesReferencesYearsResponse":
        """
        Возвращает список годов выхода релизов в избранном текущего пользователя
        """
        result = await self._api.get(
            "/accounts/users/me/favorites/references/years"
        )
        return UsersMeFavoritesReferencesYearsResponse(data=result)

    async def users_me_favorites_ids(self) -> "UsersMeFavoritesIdsResponse":
        """
        Возвращает данные по идентификаторам релизов из избранного авторизованного пользователя
        """
        result = await self._api.get("/accounts/users/me/favorites/ids")
        return UsersMeFavoritesIdsResponse(data=result)

    async def users_me_favorites_releases_get(
        self, release_collection: ReleaseCollection
    ) -> "UsersMeFavoritesReleasesResponse":
        """
        Возвращает данные по релизам из избранного текущего пользователя

        :param release_collection: тело ReleaseCollection
        """
        params = {
            "page": release_collection.page,
            "limit": release_collection.limit,
            "type_of_collection": release_collection.type_of_collection.value,
            "include": release_collection.include,
            "exclude": release_collection.exclude,
        }

        coll = await validate_collection(params=release_collection)
        final_params = {**params, **coll}

        result = await self._api.get(
            "/accounts/users/me/favorites/releases", params=final_params
        )
        return UsersMeFavoritesReleasesResponse(**result)

    async def users_me_favorites_releases_post(
        self, release_collection: ReleaseCollection
    ) -> "UsersMeFavoritesReleasesResponse":
        """
        Возвращает данные по релизам из определенной коллекции авторизованного пользователя

        :param release_collection: тело ReleaseCollection
        """
        json = {
            "page": release_collection.page,
            "limit": release_collection.limit,
            "type_of_collection": release_collection.type_of_collection.value,
            "include": release_collection.include,
            "exclude": release_collection.exclude,
        }

        coll = await validated_json_collection(release=release_collection)
        final_json = {**json, **coll}

        result = await self._api.post(
            "/accounts/users/me/favorites/releases", json_data=final_json
        )
        return UsersMeFavoritesReleasesResponse(**result)

    async def users_me_favorites_add(
        self, release_ids: list[int]
    ) -> "UsersMeFavoritesResponse":
        """
        Добавляет релизы в избранное авторизованного пользователя

        :param release_id: ID релиза
        """
        params = [{"release_id": a} for a in release_ids]

        response = await self._api.post(
            "/accounts/users/me/favorites", json_data=params
        )
        return UsersMeFavoritesResponse(data=response)

    async def users_me_favorites_delete(
        self, release_ids: list[int]
    ) -> "UsersMeFavoritesResponse":
        """
        Удаляет релизы из избранного авторизованного пользователя

        :param release_id: ID релиза
        """
        params = [{"release_id": a} for a in release_ids]

        response = await self._api.delete(
            "/accounts/users/me/collections", json_data=params
        )
        return UsersMeFavoritesResponse(data=response)

    async def users_me_profile(
        self, include: str | None = None, exclude: str | None = None
    ) -> "UsersMeProfileResponse":
        """
        Возвращает данные профиля авторизованного пользователя (auth need)

        :param include: Опционально. Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Example : id,type.genres
        :param exclude: Опционально. Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include Example : poster,description
        """

        query = {"include": include, "exclude": exclude}

        response = await self._api.get(
            "/accounts/users/me/profile", params=query
        )
        return UsersMeProfileResponse(**response)

    async def users_me_views_history(
        self,
        page: int | None = None,
        limit: int | None = None,
        include: str | None = None,
        exclude: str | None = None,
    ) -> "UsersMeViewsHistoryResponse":
        """
        Возвращает историю просмотров эпизодов авторизованного пользователя

        :param page: Опционально. Номер страницы
        :param limit: Опционально. Лимит на страницу
        :param include: Опционально. Список включаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку.
        :param exclude: Опционально. Список исключаемых полей. Через запятую или множественные параметры. Поддерживается вложенность через точку. Приоритет над include
        """
        params = {
            "page": page,
            "limit": limit,
            "include": include,
            "exclude": exclude,
        }
        response = await self._api.get(
            "/accounts/users/me/views/history", params=params
        )
        return UsersMeViewsHistoryResponse(**response)

    async def users_me_views_timecodes(
        self, since: str | None = None
    ) -> "UsersMeViewsTimecodesResponse":
        """
        Возвращает таймкоды по прогрессу просмотренных эпизодов

        :param since: Опционально. Возвращает только таймкоды, которые были добавлены после указанного времени (в iso формате). Example: 2025-05-12T07:20:50.52Z
        """
        params = {"since": since}
        response = await self._api.get(
            "/accounts/users/me/views/timecodes", params=params
        )
        return UsersMeViewsTimecodesResponse(data=response)

    async def users_me_views_timecodes_update(
        self, timecode_list: list[TimeCode]
    ) -> NoReturn:
        """
        Обновляет таймкоды просмотренных эпизодов

        :param timecode_list: Лист из обьектов TimeCode. Example: [TimeCode(...)]
        """
        json = [timecode.model_dump(mode="json") for timecode in timecode_list]

        return await self._api.post(
            "/accounts/users/me/views/timecodes", json_data=json
        )

    async def users_me_views_timecodes_delete(
        self, episode_id_list: list[str]
    ) -> NoReturn:
        """
        Удаляет данные по таймкодам просмотров для указанных эпизодов

        :param episode_id_list: Лист из episode_id. Example: ["id", "id"]
        """
        list_ = []
        for episode in episode_id_list:
            list_.append({"release_episode_id": episode})

        return await self._api.delete(
            "/accounts/users/me/views/timecodes", json_data=list_
        )
