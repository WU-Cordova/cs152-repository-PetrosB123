

from dataclasses import dataclass
from enum import Enum
from projects.project3.text_fix import text_fix


class DrinkList(Enum):
    """drinks on the menu"""
    #I don't know what the bistro sells but
    WATER = 1
    BLACK_DRIP = 2
    GREEN_TEA = 3
    FRAPPE = 4
    OVERPRICED_STARBUCKS_DRINK = 5
    PUP_CUP = 6

class Prices(Enum):
    """Prices for each drink"""
    WATER = 0.99
    BLACK_DRIP = 1.49
    GREEN_TEA = 2.49
    FRAPPE = 2.99
    OVERPRICED_STARBUCKS_DRINK = 6.99
    PUP_CUP = 0.00

class SizeMult(Enum):
    """Price mult for size"""
    S = 0.75
    M = 1.0
    L = 1.25

class Drink:
    """Drink item. Contains size, name, and price"""
    def __init__(self, drink_id: int, size: str = "M") -> None:
        if size.strip().upper() not in ("S", "M", "L"):
            size = "M"
        self._size = size.strip().upper()
        if drink_id <= len(DrinkList):
            self._drink = DrinkList(drink_id)
        else:
            raise IndexError("Invalid drink")
        self._price = round(Prices[self._drink.name].value * SizeMult[self._size].value, 2)

    @property
    def value(self) -> float:
        return self._price
    
    @property
    def name(self) -> str:
        return text_fix(self._drink.name)


    def __repr__(self) -> str:
        return f"{text_fix(self._drink.name)}, {self._size}, ${self._price}"