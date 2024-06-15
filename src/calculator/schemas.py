from typing import List, Optional

from pydantic import BaseModel


# Schemas for Zakat on Property
class ZakatOnProperty(BaseModel):
    cash: Optional[int]
    cash_on_bank_cards: Optional[int]
    silver_jewelry: Optional[int]
    gold_jewelry: Optional[int]
    purchased_product_for_resaling: Optional[int]
    unfinished_product: Optional[int]
    produced_product_for_resaling: Optional[int]
    purchased_not_for_resaling: Optional[int]
    used_after_nisab: Optional[int]
    rent_money: Optional[int]
    stocks_for_resaling: Optional[int]
    income_from_stocks: Optional[int]

    class Config:
        orm_mode = True


class ZakatOnProperyCalculated(BaseModel):
    zakat_value: float
    currency: Optional[str] = "RUB"


# Schemas for Zakat Livestock
class ZakatOnLivestock(BaseModel):
    camels: Optional[int]
    cows: Optional[int]
    buffaloes: Optional[int]
    sheep: Optional[int]
    goats: Optional[int]
    horses: Optional[int]


class ZakatOnLivestockResponse(BaseModel):
    camels: Optional[int]
    cows: Optional[int]
    buffaloes: Optional[int]
    sheep: Optional[int]
    goats: Optional[int]
    horses: Optional[float]
    nisab_status: bool
    currency: Optional[str] = "RUB"


# Schemas for Zakat Ushr

class Crop(BaseModel):
    type: str
    quantity: int
    is_ushr_land: bool
    is_irrigated: bool


class ZakatUshrRequest(BaseModel):
    crops: List[Crop]


class ZakatUshrItem(BaseModel):
    type: str
    quantity: float


class ZakatUshrResponse(BaseModel):
    zakat_ushr_value: List[ZakatUshrItem]

class NisabValue(BaseModel):
    nisab_value: int
    currency: Optional[str] = "RUB"