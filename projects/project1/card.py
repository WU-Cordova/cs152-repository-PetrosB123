

from dataclasses import dataclass
from enum import Enum


class CardSuit(Enum):
    HEARTS = "♥️"
    DIAMONDS = "♦️"
    SPADES = "♠️"
    CLUBS = "♣️"

class CardRank(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

@dataclass(frozen=True)
class Card:
    card_rank: CardRank
    card_suit: CardSuit
    