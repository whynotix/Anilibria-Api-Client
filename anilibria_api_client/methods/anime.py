
from anilibria_api_client.models import Release

from ._helper import create_filters_from_release, validate_filters
from ._libria import BaseMethod


class AnimeMethod(BaseMethod):
    async def catalog_releases_get(self, params: Release):
        """
        Возвращает список релизов по заданными параметрам (GET запрос)

        :param params: Тело Release
        """
        body = {
            "page": params.page,
            "limit": params.limit,
            "include": params.include,
            "exclude": params.exclude,
        }
        validated_f_args = await validate_filters(params=params)
        final_body = {**body, **validated_f_args}

        return await self._api.get(
            "/anime/catalog/releases", params=final_body
        )

    async def catalog_releases_post(self, params: Release):
        """
        Возвращает список релизов по заданными параметрам (POST запрос)

        :param params: Тело Release
        """
        body = {
            "page": params.page,
            "limit": params.limit,
            "include": params.include,
            "exclude": params.exclude,
        }
        filters = await create_filters_from_release(params)
        final_body = {**body, **filters}

        return await self._api.post(
            "/anime/catalog/releases", json_data=final_body
        )

    async def catalog_references_age_ratings(self):
        """
        Возвращает список возможных возрастных рейтингов в каталоге
        """
        return await self._api.get("/anime/catalog/references/age-ratings")

    async def catalog_references_genres(self):
        """
        Возвращает список всех жанров в каталоге
        """
        return await self._api.get("/anime/catalog/references/genres")

    async def catalog_references_production_statuses(self):
        """
        Возвращает список возможных статусов озвучки релиза в каталоге
        """
        return await self._api.get(
            "/anime/catalog/references/production-statuses"
        )

    async def catalog_references_publish_statuses(self):
        """
        Возвращает список возможных статусов выхода релиза в каталоге
        """
        return await self._api.get(
            "/anime/catalog/references/publish-statuses"
        )

    async def catalog_references_seasons(self):
        """
        Возвращает список возможных сезонов релизов в каталоге
        """
        return await self._api.get("/anime/catalog/references/seasons")

    async def catalog_references_sorting(self):
        """
        Возвращает список возможных типов сортировок в каталоге
        """
        return await self._api.get("/anime/catalog/references/sorting")

    async def catalog_references_types(self):
        """
        Возвращает список возможных типов релизов в каталоге
        """
        return await self._api.get("/anime/catalog/references/types")

    async def catalog_references_years(self):
        """
        Возвращает список годов в каталоге
        """
        return await self._api.get("/anime/catalog/references/years")

    async def franchises(
        self, include: str | None = None, exclude: str | None = None
    ):
        """
        Возвращает список франшиз

        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}
        return await self._api.get("/anime/franchises", params=params)

    async def franchises_franchiseId(
        self,
        franchiseId: str,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные франшизы по Id

        :param franchiseId: Обязательно. Id франшизы
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        endpoint = self._api.build_endpoint_with_params(
            "/anime/franchises/{franchiseId}", franchiseId=franchiseId
        )
        return await self._api.get(endpoint=endpoint, params=params)

    async def franchises_random(
        self,
        limit: int | None = None,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает список случайных франшиз.

        :param limit: Лимит случайных франшиз
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"limit": limit, "include": include, "exclude": exclude}

        return await self._api.get("/anime/franchises/random", params=params)

    async def franchises_release_releaseId(
        self,
        releaseId: str,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает список франшиз, в которых участвует релиз

        :param releaseId: Обязательно. Id франшизы
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        endpoint = self._api.build_endpoint_with_params(
            "/anime/franchises/release/{releaseId}", releaseId=releaseId
        )
        return await self._api.get(endpoint=endpoint, params=params)

    async def genres(
        self, include: str | None = None, exclude: str | None = None
    ):
        """
        Возвращает список всех жанров

        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        return await self._api.get("/anime/genres", params=params)

    async def genres_genreId(
        self,
        genreId: int,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает список всех жанров

        :param genreId: ID жанра, обязательно
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        endpoint = self._api.build_endpoint_with_params(
            "/anime/genres/{genreId}", genreId=genreId
        )
        return await self._api.get(endpoint, params=params)

    async def genres_random(
        self,
        limit: int | None = None,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает список случайных жанров

        :param limit: Лимит случайных жанров
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"limit": limit, "include": include, "exclude": exclude}

        return await self._api.get("/anime/genres/random", params=params)

    async def genres_genreId_releases(
        self,
        genreId: int,
        page: int | None = None,
        limit: int | None = None,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает список всех релизов жанра

        :param genreId: Обязательно. ID жанра
        :param page: Номер страницы
        :param limit: Лимит на страницу
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {
            "page": page,
            "limit": limit,
            "include": include,
            "exclude": exclude,
        }

        endpoint = self._api.build_endpoint_with_params(
            "/anime/genres/{genreId}/releases", genreId=genreId
        )
        return await self._api.get(endpoint, params=params)

    async def releases_latest(
        self,
        limit: int | None = None,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по последним релизам

        :param limit: Количество последних релизов в выдаче
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"limit": limit, "include": include, "exclude": exclude}

        return await self._api.get("/anime/releases/latest", params=params)

    async def releases_random(
        self,
        limit: int | None = None,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по случайным релизам

        :param limit: Количество случайных релизов
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"limit": limit, "include": include, "exclude": exclude}

        return await self._api.get("/anime/releases/random", params=params)

    async def releases_recommended(
        self,
        limit: int | None = None,
        release_id: int | None = None,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по рекомендованным релизам

        :param limit: Количество рекомендованных релизов
        :param release_id: Идентификатор релиза, для которого рекомендуем
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {
            "limit": limit,
            "release_id": release_id,
            "include": include,
            "exclude": exclude,
        }

        return await self._api.get(
            "/anime/releases/recommended", params=params
        )

    async def releases_list(
        self,
        ids: list[int],
        aliases: list[str],
        page: int | None = None,
        limit: int | None = None,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по списку релизов

        :param ids: Список ID релизов Обязательно
        :param aliases: Список alias релизов Обязательно
        :param page: Номер страницы
        :param limit: Лимит на страницу
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {
            "ids": ids,
            "aliases": aliases,
            "page": page,
            "limit": limit,
            "include": include,
            "exclude": exclude,
        }

        return await self._api.get("/anime/releases/list", params=params)

    async def releases_idOrAlias(
        self,
        idOrAlias: str,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по релизу

        :param idOrAlias: id или alias релиза Обязательно
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        endpoint = self._api.build_endpoint_with_params(
            "/anime/releases/{idOrAlias}", idOrAlias=idOrAlias
        )
        return await self._api.get(endpoint, params)

    async def releases_idOrAlias_members(
        self,
        idOrAlias: str,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по участникам релиза

        :param idOrAlias: id или alias релиза Обязательно
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        endpoint = self._api.build_endpoint_with_params(
            "/anime/releases/{idOrAlias}/members", idOrAlias=idOrAlias
        )
        return await self._api.get(endpoint, params)

    async def releases_idOrAlias_episodes_timecodes(
        self,
        idOrAlias: str,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по всем существующим таймкодам просмотра эпизодов релиза. Имеет 1-2-x минутный кэш.

        :param idOrAlias: id или alias релиза Обязательно
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        endpoint = self._api.build_endpoint_with_params(
            "/anime/releases/{idOrAlias}/episodes/timecodes",
            idOrAlias=idOrAlias,
        )
        return await self._api.get(endpoint, params)

    async def releases_episodes_releaseEpisodeId(
        self,
        releaseEpisodeId: str,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по эпизоду

        :param releaseEpisodeId: Идентификатор эпизода Обязательно
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        endpoint = self._api.build_endpoint_with_params(
            "/anime/releases/episodes/{releaseEpisodeId}",
            releaseEpisodeId=releaseEpisodeId,
        )
        return await self._api.get(endpoint, params)

    async def releases_episodes_releaseEpisodeId_timecode(
        self,
        releaseEpisodeId: str,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по просмотру указанного эпизода авторизованным пользователем. Имеет 1-2-x минутный кэш.

        :param releaseEpisodeId: Идентификатор эпизода Обязательно
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        endpoint = self._api.build_endpoint_with_params(
            "/anime/releases/episodes/{releaseEpisodeId}/timecode",
            releaseEpisodeId=releaseEpisodeId,
        )
        return await self._api.get(endpoint, params)

    async def schedule_now(
        self, include: str | None = None, exclude: str | None = None
    ):
        """
        Возвращает список релизов в расписании на текущую дату

        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        return await self._api.get("/anime/schedule/now", params=params)

    async def schedule_week(
        self, include: str | None = None, exclude: str | None = None
    ):
        """
        Возвращает список релизов в расписании на текущую неделю

        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        return await self._api.get("/anime/schedule/week", params=params)

    async def torrents(
        self,
        page: int | None = None,
        limit: int | None = None,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по последним торрентам

        :param page: Номер страницы
        :param limit: Лимит на страницу
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {
            "page": page,
            "limit": limit,
            "include": include,
            "exclude": exclude,
        }

        return await self._api.get("/anime/torrents", params=params)

    async def torrents_hashOrId(
        self,
        hashOrId: str,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по последним торрентам

        :param hashOrId: Обязательно Хэш или ID торрента
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        endpoint = self._api.build_endpoint_with_params(
            "/anime/torrents/{hashOrId}", hashOrId=hashOrId
        )
        return await self._api.get(endpoint, params)

    async def torrents_hashOrId_file(
        self, hashOrId: str, pk: str | None = None
    ):
        """
        Возвращает данные по последним торрентам

        :param hashOrId: Обязательно Хэш или ID торрента
        :param pk: passkey пользователя. Оставьте пустым для собственного pk (если аутентифицирован)
        """
        params = {"pk": pk}
        headers = {
            "Content-Type": "application/x-bittorrent; utf-8",
            "Accept": "application/x-bittorrent",
        }

        endpoint = self._api.build_endpoint_with_params(
            "/anime/torrents/{hashOrId}/file", hashOrId=hashOrId
        )
        return await self._api.get(endpoint, params, headers)

    async def torrents_release_releaseId(
        self,
        releaseId: int,
        include: str | None = None,
        exclude: str | None = None,
    ):
        """
        Возвращает данные по последним торрентам

        :param releaseId: Обязательно ID релиза
        :param include: Поля для включения
        :param exclude: Поля для исключения
        """
        params = {"include": include, "exclude": exclude}

        endpoint = self._api.build_endpoint_with_params(
            "/anime/torrents/release/{releaseId}", releaseId=releaseId
        )
        return await self._api.get(endpoint, params)

    async def torrents_rss(
        self, limit: int | None = None, pk: str | None = None
    ):
        """
        Возвращает данные по последним торрентам в виде XML документа

        :param limit: Количество торрентов в выдаче. По умолчанию 10
        :param pk: passkey пользователя. Оставьте пустым для собственного pk (если аутентифицирован)
        """
        params = {"limit": limit, "pk": pk}
        headers = {
            "Content-Type": "application/xml",
        }

        return await self._api.get(
            "/anime/torrents/rss", params=params, headers=headers
        )

    async def torrents_rss_release_releaseId(
        self, releaseId: int, pk: str | None = None
    ):
        """
        Возвращает данные по торрентам релиза в виде RSS ленты (xml)

        :param releaseId: Обязательно ID релиза
        :param pk: passkey пользователя. Оставьте пустым для собственного pk (если аутентифицирован)
        """
        params = {"pk": pk}
        headers = {
            "Content-Type": "application/xml",
        }

        endpoint = self._api.build_endpoint_with_params(
            "/anime/torrents/rss/release/{releaseId}", releaseId=releaseId
        )
        return await self._api.get(
            endpoint=endpoint, params=params, headers=headers
        )
