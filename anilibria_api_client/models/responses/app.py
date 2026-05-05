from pydantic import AwareDatetime, ConfigDict
from pydantic import BaseModel as PreBaseModel
from typing import List

from anilibria_api_client.models.models import *


class BaseModel(PreBaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class SearchReleasesResponse(BaseModel):
    data: List[ReleaseModel]


class StatusResponse(BaseModel):
    request: RequestModel
    is_alive: bool | None = None
    available_api_endpoints: list[str] | None = None
