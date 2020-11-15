import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("spades", 1)
        self.card2 = Card("clubs", 5)
        self.cardgame1 = CardGame()
        self.cards = [self.card1, self.card2]

    def test_for_ace(self):
        self.assertEqual(True, self.cardgame1.check_for_ace(self.card1))

    def test_for_not_ace(self):
        self.assertEqual(False, self.cardgame1.check_for_ace(self.card2))

    def test_for_highest_card(self):
        self.assertEqual(self.card2, self.cardgame1.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 6", self.cardgame1.cards_total(self.cards)) 