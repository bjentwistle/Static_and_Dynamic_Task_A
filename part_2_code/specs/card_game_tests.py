import unittest
from src.card import Card
from src.card_game import CardGame

    # self.suit = suit
    # self.value = value

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("Hearts", 1)
        self.card1 = Card("Spades", 8)
        self.card2 = Card("Clubs", 10)
        self.cards = [self.card, self.card1, self.card2]

    def test_check_for_ace(self):
        result = CardGame.check_for_ace(self, self.card)
        self.assertEqual(True, result)

    def test_highest_card(self):
        result = CardGame.highest_card(self, self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_cards_total(self):
        result = CardGame.cards_total(self, self.cards)
        self.assertEqual(("You have a total of ", 19), result)


