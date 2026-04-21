"""Auto-generated AniLiberty methods."""

from __future__ import annotations

from typing import Any

from ....methods._libria import BaseMethod


class GeneratedAnimeMethod(BaseMethod):
    async def catalog_references_age_ratings(
            self
    ) -> Any:
        """Список возрастных рейтингов в каталоге

        Возвращает список возможных возрастных рейтингов в каталоге
        """
        endpoint = "/anime/catalog/references/age-ratings"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def catalog_references_genres(
            self
    ) -> Any:
        """Список жанров в каталоге

        Возвращает список всех жанров в каталоге
        """
        endpoint = "/anime/catalog/references/genres"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def catalog_references_production_statuses(
            self
    ) -> Any:
        """Список возможных статусов озвучки релиза в каталоге

        Возвращает список возможных статусов озвучки релиза в каталоге
        """
        endpoint = "/anime/catalog/references/production-statuses"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def catalog_references_publish_statuses(
            self
    ) -> Any:
        """Список возможных статусов выхода релиза в каталоге

        Возвращает список возможных статусов выхода релиза в каталоге
        """
        endpoint = "/anime/catalog/references/publish-statuses"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def catalog_references_seasons(
            self
    ) -> Any:
        """Список сезонов релиза в каталоге

        Возвращает список возможных сезонов релизов в каталоге
        """
        endpoint = "/anime/catalog/references/seasons"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def catalog_references_sorting(
            self
    ) -> Any:
        """Список возможных типов сортировок в каталоге

        Возвращает список возможных типов сортировок в каталоге
        """
        endpoint = "/anime/catalog/references/sorting"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def catalog_references_types(
            self
    ) -> Any:
        """Список типов релизов в каталоге

        Возвращает список возможных типов релизов в каталоге
        """
        endpoint = "/anime/catalog/references/types"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def catalog_references_years(
            self
    ) -> Any:
        """Список годов в каталоге

        Возвращает список годов в каталоге
        """
        endpoint = "/anime/catalog/references/years"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def catalog_releases_get(
            self,
            exclude: list[str] | str | None = None,
            f_age_ratings_: list[Any] | None = None,
            f_genres_: Any | None = None,
            f_production_statuses_: list[Any] | None = None,
            f_publish_statuses_: list[Any] | None = None,
            f_search_: Any | None = None,
            f_seasons_: list[Any] | None = None,
            f_sorting_: Any | None = None,
            f_types_: list[Any] | None = None,
            f_years__from_year_: Any | None = None,
            f_years__to_year_: Any | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None,
            page: int | None = None
    ) -> Any:
        """Список релизов в каталоге

        Возвращает список релизов по заданными параметрам
        """
        endpoint = "/anime/catalog/releases"
        params = {
        "page": page,
        "limit": limit,
        "f[genres]": f_genres_,
        "f[types]": f_types_,
        "f[seasons]": f_seasons_,
        "f[years][from_year]": f_years__from_year_,
        "f[years][to_year]": f_years__to_year_,
        "f[search]": f_search_,
        "f[sorting]": f_sorting_,
        "f[age_ratings]": f_age_ratings_,
        "f[publish_statuses]": f_publish_statuses_,
        "f[production_statuses]": f_production_statuses_,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def catalog_releases_post(
            self,
            exclude: str | None = None,
            f: dict[str, Any] | None = None,
            include: str | None = None,
            limit: int | None = None,
            page: int | None = None
    ) -> Any:
        """Список релизов в каталоге

        Возвращает список релизов по заданными параметрам
        """
        endpoint = "/anime/catalog/releases"
        params = None
        json_data = {
        "exclude": exclude,
        "f": f,
        "include": include,
        "limit": limit,
        "page": page,
        }
        return await self._api.post(endpoint, json_data=json_data)

    async def franchises(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Получить список франшиз

        Возвращает список франшиз.
        """
        endpoint = "/anime/franchises"
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def franchises_random(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None
    ) -> Any:
        """Получить список случайных франшиз

        Возвращает список случайных франшиз.
        """
        endpoint = "/anime/franchises/random"
        params = {
        "limit": limit,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def franchises_release_releaseId(
            self,
            releaseId: str,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Получить список франшиз для релиза

        Возвращает список франшиз, в которых участвует релиз
        """
        endpoint = self._api.build_endpoint_with_params("/anime/franchises/release/{releaseId}", releaseId=releaseId)
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def franchises_franchiseId(
            self,
            franchiseId: str,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Получить франшизу

        Возвращает данные франшизы
        """
        endpoint = self._api.build_endpoint_with_params("/anime/franchises/{franchiseId}", franchiseId=franchiseId)
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def genres(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Список всех жанров

        Возвращает список всех жанров
        """
        endpoint = "/anime/genres"
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def genres_random(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None,
            limit: Any | None = None
    ) -> Any:
        """Список случайных жанров

        Возвращает список случайных жанров
        """
        endpoint = "/anime/genres/random"
        params = {
        "limit": limit,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def genres_genreId(
            self,
            genreId: Any,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Данные по жанру

        Возвращает данные по жанру
        """
        endpoint = self._api.build_endpoint_with_params("/anime/genres/{genreId}", genreId=genreId)
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def genres_genreId_releases(
            self,
            genreId: int,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None,
            page: int | None = None
    ) -> Any:
        """Список релизов жанра

        Возвращает список всех релизов жанра
        """
        endpoint = self._api.build_endpoint_with_params("/anime/genres/{genreId}/releases", genreId=genreId)
        params = {
        "page": page,
        "limit": limit,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def releases_episodes_releaseEpisodeId(
            self,
            releaseEpisodeId: Any,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Данные по эпизоду

        Возвращает данные по эпизоду
        """
        endpoint = self._api.build_endpoint_with_params("/anime/releases/episodes/{releaseEpisodeId}", releaseEpisodeId=releaseEpisodeId)
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def releases_episodes_releaseEpisodeId_timecode(
            self,
            releaseEpisodeId: Any,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Данные по просмотру эпизода

        Возвращает данные по просмотру указанного эпизода авторизованным пользователем. Имеет 1-2-x минутный кэш.
        """
        endpoint = self._api.build_endpoint_with_params("/anime/releases/episodes/{releaseEpisodeId}/timecode", releaseEpisodeId=releaseEpisodeId)
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def releases_latest(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None
    ) -> Any:
        """Последние релизы

        Возвращает данные по последним релизам
        """
        endpoint = "/anime/releases/latest"
        params = {
        "limit": limit,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def releases_list(
            self,
            aliases: list[str] | None = None,
            exclude: list[str] | str | None = None,
            ids: list[int] | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None,
            page: int | None = None
    ) -> Any:
        """Данные по списку релизов

        Возвращает данные по списку релизов
        """
        endpoint = "/anime/releases/list"
        params = {
        "ids": ids,
        "aliases": aliases,
        "page": page,
        "limit": limit,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def releases_random(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None
    ) -> Any:
        """Данные по случайным релизам

        Возвращает данные по случайным релизам
        """
        endpoint = "/anime/releases/random"
        params = {
        "limit": limit,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def releases_recommended(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None,
            release_id: int | None = None
    ) -> Any:
        """Данные по рекомендованным релизам

        Возвращает данные по рекомендованным релизам
        """
        endpoint = "/anime/releases/recommended"
        params = {
        "limit": limit,
        "release_id": release_id,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def releases_idOrAlias(
            self,
            idOrAlias: Any,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Данные по релизу

        Возвращает данные по релизу
        """
        endpoint = self._api.build_endpoint_with_params("/anime/releases/{idOrAlias}", idOrAlias=idOrAlias)
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def releases_idOrAlias_episodes_timecodes(
            self,
            idOrAlias: Any,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Данные по таймкодам просмотра эпизодов релиза

        Возвращает данные по всем существующим таймкодам просмотра эпизодов релиза. Имеет 1-2-x минутный кэш.
        """
        endpoint = self._api.build_endpoint_with_params("/anime/releases/{idOrAlias}/episodes/timecodes", idOrAlias=idOrAlias)
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def releases_idOrAlias_members(
            self,
            idOrAlias: Any,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Список участников, которые работали над релизом

        Возвращает данные по участникам релиза
        """
        endpoint = self._api.build_endpoint_with_params("/anime/releases/{idOrAlias}/members", idOrAlias=idOrAlias)
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def schedule_now(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Данные по расписанию релизов на текущую дату

        Возвращает список релизов в расписании на текущую дату
        """
        endpoint = "/anime/schedule/now"
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def schedule_week(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Данные по расписанию релизов на текущую неделю

        Возвращает список релизов в расписании на текущую неделю
        """
        endpoint = "/anime/schedule/week"
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def torrents(
            self,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None,
            limit: int | None = None,
            page: int | None = None
    ) -> Any:
        """Данные по торрентам

        Возвращает данные по последним торрентам
        """
        endpoint = "/anime/torrents"
        params = {
        "page": page,
        "limit": limit,
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def torrents_release_releaseId(
            self,
            releaseId: int,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Данные по торрентам для релиза

        Возвращает данные по торрентам релиза
        """
        endpoint = self._api.build_endpoint_with_params("/anime/torrents/release/{releaseId}", releaseId=releaseId)
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def torrents_rss(
            self,
            limit: int | None = None,
            pk: str | None = None
    ) -> Any:
        """RSS лента последних торрентов

        Возвращает данные по последним торрентам в виде XML документа
        """
        endpoint = "/anime/torrents/rss"
        params = {
        "limit": limit,
        "pk": pk,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def torrents_rss_release_releaseId(
            self,
            releaseId: int,
            pk: str | None = None
    ) -> Any:
        """RSS лента торрентов релиза

        Возвращает данные по торрентам релиза в виде RSS ленты
        """
        endpoint = self._api.build_endpoint_with_params("/anime/torrents/rss/release/{releaseId}", releaseId=releaseId)
        params = {
        "pk": pk,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def torrents_hashOrId(
            self,
            hashOrId: str,
            exclude: list[str] | str | None = None,
            include: list[str] | str | None = None
    ) -> Any:
        """Данные по торренту

        Возвращает данные по торренту
        """
        endpoint = self._api.build_endpoint_with_params("/anime/torrents/{hashOrId}", hashOrId=hashOrId)
        params = {
        "include": include,
        "exclude": exclude,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def torrents_hashOrId_file(
            self,
            hashOrId: str,
            pk: str | None = None
    ) -> Any:
        """Торрент-файл по его hash или id

        Возвращает торрент-файл
        """
        endpoint = self._api.build_endpoint_with_params("/anime/torrents/{hashOrId}/file", hashOrId=hashOrId)
        params = {
        "pk": pk,
        }
        json_data = None
        return await self._api.get(endpoint, params=params)
