from sqlmodel import SQLModel, Field, create_engine, Session, Relationship
from typing import List, Optional


class ReviewerCategory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    toll_class: str
    sub_class: str


class Reviewer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    category_id: int = Field(foreign_key="reviewercategory.id")
    category: ReviewerCategory = Relationship()


class PassageClass(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    toll_class: str
    sub_class: str


class AVC(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    avc_amount: int


class CashPayment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    amount_paid: int
    currency_paid: str
    change_returned: int
    currency_returned: str


class CollectorTollClass(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    toll_class: str
    sub_class: str


class Collector(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    collector_code: str
    collector_toll_class_id: int = Field(foreign_key="collectortollclass.id")
    collector_plate: str
    discount_by_doc: int
    voucher_amount: int
    cash_payment_id: int = Field(foreign_key="cashpayment.id")
    comment: str
    cash_payment: CashPayment = Relationship()
    collector_toll_class: CollectorTollClass = Relationship()


class Passage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    toll_company: str
    plaza: str
    lane_num: int
    lane_direction: str
    lane_type: str
    tr_set: str
    tr_set_time: str
    passage_time: str
    lane_state: str
    open_mode: str
    degraded_modes: str
    transaction_id: str
    receipt_id: str
    payment_type: str
    payment_mean: str
    read_mode: str
    detection_incidents: int
    passage_end_time: str
    collector_id: int = Field(foreign_key="collector.id")
    avc_id: int = Field(foreign_key="avc.id")
    passage_class_id: int = Field(foreign_key="passageclass.id")
    gross_amount: int
    amount: int
    vat_percentage: int
    vat_amount: int
    tap_amount: int
    abnormal_types: str
    has_picture: str
    reviewer_id: int = Field(foreign_key="reviewer.id")
    collector: Collector = Relationship()
    avc: AVC = Relationship()
    passage_class: PassageClass = Relationship()
    reviewer: Reviewer = Relationship()


class SapData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    transit_state: Optional[str] = None
    change_allowed: bool


class Transit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    passage_id: int = Field(foreign_key="passage.id")
    sap_data_id: int = Field(foreign_key="sapdata.id")
    passage: Passage = Relationship()
    sap_data: SapData = Relationship()


class ReviewTransit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    transit_id: int = Field(foreign_key="transit.id")
    transit: Transit = Relationship()
