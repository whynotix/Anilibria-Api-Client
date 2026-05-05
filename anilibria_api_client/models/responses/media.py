from pydantic import AwareDatetime, ConfigDict
from pydantic import BaseModel as PreBaseModel
from typing import List

from anilibria_api_client.models.models import *


class BaseModel(PreBaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class PromotionsResponse(BaseModel):
    data: List[PromotionsModel]


class VideosResponse(BaseModel):
    data: List[VideosModel]
