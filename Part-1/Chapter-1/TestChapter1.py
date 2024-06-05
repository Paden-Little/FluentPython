import pytest


class TestPythonicDeckTestClass:
    def test_LenOfFrenchDeckIsEqualTo52(self):
        from PythonicDeckOfCards import FrenchDeck
        deck = FrenchDeck()
        assert len(deck) == 52
        # The len() function properly returns the number of cards in the deck due to our implementation of
        # __len__(self): method in the class

    def test_BracketOperatorProperlyReturnsCardFromFrenchDeck(self):
        from PythonicDeckOfCards import FrenchDeck, Card
        deck = FrenchDeck()
        firstCard = Card(rank='2', suit='spades')
        lastCard = Card(rank='A', suit='hearts')

        assert deck[0] == firstCard
        assert deck[-1] == lastCard
        # Because we implemented the __getitem__(self, pos): method, we gain access to the [] operator

    def test_DunderGetItemProperlyAllowsForDeckSlicing(self):
        from PythonicDeckOfCards import FrenchDeck
        deck = FrenchDeck()
        aces = deck[12::13]
        assert len(aces) == 4
        print(aces)
        # __getitem__(self, pos): also gives us the ability to slice the deck because of the exposing of the [] operator

    def test_CanChooseRandomCardFromFrenchDeck(self):
        from PythonicDeckOfCards import FrenchDeck
        from random import choice
        deck = FrenchDeck()
        assert choice(deck) is not None
        print(choice(deck))
        # The __getitem__(self, pos): method also allows us to pass the deck to get random cards from it, without
        # needing to generate our own method.

    def test_FrenchDeckIsIteratble(self):
        from PythonicDeckOfCards import FrenchDeck
        deck = FrenchDeck()
        for card in deck[10::13]:
            print(card)
        # __getitem__(self, pos): also gives us the ability to iterate over deck

    def test_FrenchDeckCanBeSorted(self):
        from PythonicDeckOfCards import FrenchDeck
        deck = FrenchDeck()
        sorted_deck = []
        for card in sorted(deck, key=deck.spades_high):
            sorted_deck.append(card)

        for card in sorted_deck[3::4]:
            assert card.suit == 'spades'
        # __getitem__(self, pos): also allows us to use sorted() like the class was a list


class TestVector:
    def test_AdditionOfVectors(self):
        from Vector import Vector
        v1 = Vector(2, 4)
        v2 = Vector(2, 1)

        act = v1 + v2
        assert act == Vector(4, 5)

    def test_SubtractionOfVectors(self):
        from Vector import Vector
        v1 = Vector(2, 4)
        v2 = Vector(2, 1)

        act = v1 - v2
        assert act == Vector(0, 3)

    def test_MagnitudeOfVectors(self):
        from Vector import Vector
        v1 = Vector(3, 4)
        assert abs(v1) == 5.0

    def test_MultiplicationOfVectorByScalar(self):
        from Vector import Vector
        v1 = Vector(2, 4)

        act = v1 * 2
        assert act == Vector(4, 8)