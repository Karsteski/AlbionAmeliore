from enum import Enum
import dataclasses

class Location(Enum):
    Brecilien     = 0
    Bridgewatch   = 1
    Caerleon      = 2
    Fort_Sterling = 3
    Lymhurst      = 4
    Martlock      = 5
    Thetford      = 6

class Quality(Enum):
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

