from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from anilibria_api_client.api_client import AsyncAnilibriaAPI


class BaseMethod:
    def __init__(self, api: "AsyncAnilibriaAPI") -> None:
        self._api = api
