from datetime import datetime, timezone
from pydantic import BaseModel, Field
from typing import Optional
from receiver.models.PassageModel import PassageModel


class RevisionModel(BaseModel):
    reviewerId: str
    reviewTS: datetime = Field(default=datetime.now(tz=timezone.utc).isoformat())
    supervisiorId: Optional[str] = Field(default=None)
    approvalTS: datetime = Field(default=datetime.now(tz=timezone.utc).isoformat())


class OptionChoiceModel(BaseModel):
    selectionType: Optional[str] = Field(default=None)
    options: Optional[str] = Field(default=None)


class JustificationModel(BaseModel):
    freeText: Optional[str] = Field(default=None)
    optionChoice: Optional[OptionChoiceModel]


class RelatedTransitsModel(BaseModel):
    transactionId: str = Field(default=None)


class TransitModel(BaseModel):
    passage: Optional[PassageModel]
    revision: Optional[RevisionModel]
    justification: Optional[JustificationModel] = Field(default=None)
    relatedTransits: Optional[RelatedTransitsModel] = Field(default=None)
