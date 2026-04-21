"""Auto-generated AniLiberty methods."""

from __future__ import annotations

from typing import Any

from ....methods._libria import BaseMethod


class GeneratedAdsMethod(BaseMethod):
    async def vasts_manifest_xml(
            self
    ) -> Any:
        """VAST XML с цепочкой реклам

        Возвращает XML страницу со всеми доступными для использования VAST кампаниями. Можно просто отдавать этот URL в любой VAST плеер, который поддерживает загрузку vast XML по url
        """
        endpoint = "/media/manifest.xml"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)

    async def vasts(
            self
    ) -> Any:
        """Список возможных VAST реклам

        Возвращает список со всеми доступными для использования VAST кампаниями
        """
        endpoint = "/media/vasts"
        params = None
        json_data = None
        return await self._api.get(endpoint, params=params)
