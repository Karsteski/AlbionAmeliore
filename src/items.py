from enum import Enum
import datetime

import dataclasses

class City(Enum):
    Brecilien     = 0
    Bridgewatch   = 1
    Caerleon      = 2
    Fort_Sterling = 3
    Lymhurst      = 4
    Martlock      = 5
    Thetford      = 6

class Quality(Enum):
    Non        = 0
    Normal      = 1
    Good        = 2
    Outstanding = 3
    Excellent   = 4
    Masterpiece = 5

@dataclasses.dataclass
class Item:
    """
    Representation of a general item in Albion Online
    """

    # Let's only use English for now
    name: str
    uid: str

    quality: Quality = Quality.Normal

@dataclasses.dataclass
class MarketData:
    item: Item
    city: City

    min_sell_price_datetime: datetime.datetime
    max_sell_price_datetime: datetime.datetime

    min_buy_price_datetime: datetime.datetime
    max_buy_price_datetime: datetime.datetime

    min_sell_price: int = 0
    max_sell_price: int = 0

    min_buy_price: int = 0
    max_buy_price: int = 0



