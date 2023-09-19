import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("Spade", 5)
        self.card2 = Card("Diamond", 8)
        self.cards = [self.card1, self.card2]


    def test_card1_is_not_an_ace(self):
        self.assertEquals(False, CardGame.check_for_ace(self.card1))

    def test_card2_is_higher_value_than_card1(self):
        result = CardGame().highest_card(self.card1, self.card2)
        self.assertEquals(self.card2, result)
    
    def test_cards_total_value_equals_13(self):
        cards = self.cards
        result = str(CardGame().cards_total(cards))
        self.assertEquals("You have a total of 13", result)