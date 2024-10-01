from typing import Optional, Union, List
from pydantic import BaseModel, Field
from receiver.models.PassageModel import PassageModel


class SapDataModel(BaseModel):
    transitState: Optional[str]
    changeAllowed: bool


class TransitModel(BaseModel):
    passage: PassageModel
    sapData: SapDataModel


class Ns2ReviewTransit(BaseModel):
    xmlns: str = Field(default='urn:www.softinsa.pt:mz.arteris.MRTServer', alias='@xmlns:ns2')
    transit: TransitModel
