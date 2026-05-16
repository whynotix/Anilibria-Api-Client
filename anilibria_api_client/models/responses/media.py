from pydantic import BaseModel as PreBaseModel
from pydantic import ConfigDict

from anilibria_api_client.models.models import *


class BaseModel(PreBaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class PromotionsResponse(BaseModel):
    data: list[PromotionsModel]


class VideosResponse(BaseModel):
    data: list[VideosModel]
