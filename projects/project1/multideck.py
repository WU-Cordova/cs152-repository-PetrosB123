from datastructures.bag import Bag
from projects.project1.card import Card, CardSuit, CardRank
from random import randint


class MultiDeck(Bag):

    def __init__(self, num: int) -> None:
        """
        initializes as a Bag and creates 1 deck, then adds 'num' - 1 decks
        """
        Bag.__init__(self)
        for suit in list(CardSuit):
            for rank in list(CardRank):
                self.add(Card(rank.value, suit.value))
        num -= 1
        if num > 0:
            self.add_deck(num)
        

    def add_deck(self, num: int) -> None:
        """
        adds 'num' amount of decks to the Bag
        """
        for i in range(num):
            for item in self._Bag__bag:
                self.add(item)

    def rand_card(self) -> Card:
        """
        returns and removes a random card from the deck
        """
        random_card = randint(1, len(self.distinct_items()))
        num = 0
        while num < random_card:
            for key in self._Bag__bag:
                num += 1
                if num == random_card:
                    card = key   
        self.remove(card)
        return card