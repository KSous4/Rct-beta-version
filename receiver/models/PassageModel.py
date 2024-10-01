from typing import Optional, Union, List
from pydantic import BaseModel, Field


class CollectorTollClassModel(BaseModel):
    tollClass: int
    subClass: int


class CashPaymentModel(BaseModel):
    amountPaid: int
    currencyPaid: str
    changeReturned: str
    changeReturned: str
    currencyReturned: Optional[str] = Field(default=None)


class ExemptModel(BaseModel):
    exemptGroup: str


class VoucherClassModel(BaseModel):
    tollClass: int
    subClass: int


class ChequePaymentModel(BaseModel):
    drawerId: str


class DriverDataModel(BaseModel):
    name: str
    address: str
    city: str
    state: str
    LicenseId: str
    carId: str
    model: str
    color: str


class OperationalExitPaymentModel(BaseModel):
    Type: str
    ReceptId: str


class DescriptionCodeModel(BaseModel):
    description: str
    choiceType: str
    optionCode: str


class CollectorModel(BaseModel):
    collectorCode: int
    collectorTollClass: CollectorTollClassModel
    collectorPlate: str
    exempt: Optional[ExemptModel] = Field(default=None)
    discountByDoc: Optional[int] = Field(default=None)
    discontByKcor: Optional[str] = Field(default=None)
    convoyId: Optional[str] = Field(default=None)
    numConvoy: Optional[int] = Field(default=None)
    voucherCode: Optional[str] = Field(default=None)
    voucherNumber: Optional[int] = Field(default=None)
    voucherAmount: Optional[int] = Field(default=None)
    voucherExpiryDate: Optional[str] = Field(default=None)
    voucherClass: Optional[VoucherClassModel] = Field(default=None)
    cashPayment: Optional[CashPaymentModel] = Field(default=None)
    chequePayment: Optional[ChequePaymentModel] = Field(default=None)
    driverData: Optional[DriverDataModel] = Field(default=None)
    operationalExitPayment: Optional[OperationalExitPaymentModel] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    descriptionCode: Optional[DescriptionCodeModel] = Field(default=None)
    collectorAxlesSusp: Optional[int] = Field(default=None)


class AvcTollClassModel(BaseModel):
    tollClass: int
    subClass: int


class AvcDataModel(BaseModel):
    axlesCount1: int
    axlesCount2: int
    axlesCount3: int
    axlesCount4: int
    doubleWheel: bool
    bus: Optional[bool] = Field(default=None)
    motorcycle: Optional[bool] = Field(default=None)
    trailer: Optional[bool] = Field(default=None)
    height: Optional[int] = Field(default=None)
    height1Axle: Optional[int] = Field(default=None)
    Width: Optional[int] = Field(default=None)
    width1Axle: Optional[int] = Field(default=None)
    axlesSusp: int


class AvcModel(BaseModel):
    avcTollClass: Optional[AvcTollClassModel] = None
    avcAmount: int
    avcInfoComplete: Optional[str] = None
    avcData: Optional[AvcDataModel] = None


class PassageClassModel(BaseModel):
    tollClass: int
    subClass: int


class AbnormalTypeModel(BaseModel):
    abnormalType: Optional[Union[List[Optional[str]], str]] = Field(default=None)


class CategoryModel(BaseModel):
    tollClass: int
    subClass: Optional[int]


class ReviewerModel(BaseModel):
    category: CategoryModel
    plate: Optional[str] = Field(default=None)


class CardPaymentModel(BaseModel):
    cardPAN: str
    cardExpiryDate: str


class TagTollClassModel(BaseModel):
    tollClass: int
    subClass: int


class TagDataModel(BaseModel):
    seqTr: str
    countryCode: int
    issuerId: int
    battery: Optional[int] = Field(default=None)  # Atualmente informa status MDF-e
    violation: Optional[int] = Field(default=None)
    prevCountry: Optional[int] = Field(default=None)
    prevIssuerId: Optional[int] = Field(default=None)
    prevPlaza: Optional[int] = Field(default=None)
    prevLane: Optional[int] = Field(default=None)
    prevTime: Optional[int] = Field(default=None)


class TagAuthenticationModel(BaseModel):
    oRSPKeyRef: int
    oRSPRandomNum: int
    oRSPAuthenticator: int
    pSPKeyRef: int
    pSPRandomNum: int
    pSPAuthenticator: int


class TagPaymentModel(BaseModel):
    tagPAN: str
    statusListExpiryDate: Optional[str] = Field(default=None)
    tagTollClass: TagTollClassModel
    tagExpiryDate: Optional[str] = Field(default=None)
    tagPlate: str
    numTripVVP: Optional[int] = Field(default=None)
    resultTag: str
    tagData: TagDataModel
    tagAuthentication: Optional[TagAuthenticationModel] = None
    otherTags: Optional[Union[List[str], str]] = Field(default=None)


class OCRPlateClasseModel(BaseModel):
    TollClass: int
    SubClass: int


class PassageCdUpdateModel(BaseModel):
    passageCdUpdateModel: int
    plaza: int
    laneNum: int
    laneDirection: int
    laneType: str
    creator: int
    trNumber: str
    trTimestamp: str
    DriverData: DriverDataModel


class PassageModel(BaseModel):
    tollCompany: int
    plaza: int
    laneNum: int
    laneDirection: str
    laneType: str
    trSet: int
    trSetTime: str
    passageTime: str
    laneState: str
    openMode: str
    degradedModes: int
    transactionId: str
    receiptId: str
    paymentType: str
    paymentMean: str
    issuer: Optional[str] = Field(default=None)
    readMode: str
    detectionIncidents: Optional[int] = Field(default=None)
    passageEndTime: str
    exitArea: Optional[str] = Field(default=None)
    collector: CollectorModel
    avc: AvcModel
    cardPayment: Optional[CardPaymentModel] = Field(default=None)
    tagPayment: Optional[TagPaymentModel] = Field(default=None)
    oCRPlate: Optional[str] = Field(default=None)
    oCRPlateClass: Optional[OCRPlateClasseModel] = Field(default=None)
    oCRReliability: Optional[float] = Field(default=None)
    passageClass: Optional[PassageClassModel] = Field(default=None)
    grossAmount: int
    amount: int
    vatPercentage: int
    vatAmount: int
    tapAmount: int
    tapMode: Optional[str] = Field(default=None)
    entrySpeed: Optional[int] = Field(default=None)
    abnormalTypes: Optional[AbnormalTypeModel] = Field(default=None)
    hasPicture: Optional[str] = Field(default=None)
    passageCdUpdate: Optional[PassageCdUpdateModel] = Field(default=None)
    reviewer: ReviewerModel
