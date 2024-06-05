import collections

# Named tuple to create named keys and values without attributes. Think like SQL rows. the table is named Card,
# with 2 rows suit and value
Card = collections.namedtuple('Card', ['rank', 'suit'])


# The FrenchDeck class is a simple implmenetation of a deck of cards, however instead of reinventing the wheel
# we implement both the __len__(self): and __getitem__(self, pos): dunder methods to treat the class as if it was just
# a list. This allows us to use many built-in tools for working on lists on deck as if it was a simple list. However,
# can also define additional functionality that would be lost in a simple list as seen in the spades_high(card): method
class FrenchDeck:
    # Defines a list of all ranks of cards
    ranks = [str(n) for n in range(2, 11)] + list(
        'JQKA')  # This is a sysinc way to define ranks as 2-11 jack queen king ace.
    suits = 'spades diamonds clubs hearts'.split()  # Same thing as above, but for suits

    # Initializes a list called cards, which contains all 52 cards of a deck
    def __init__(self):
        # Nested for loop to generate all combinations of cards, Create a card object for all ranks in rank and all
        # suits in suits and define as such. 13 x 4 = 52
        self.cards = [Card(rank, suit) for suit in self.suits
                      for rank in self.ranks]

    # Returns the length of the cards list.
    def __len__(self):
        # len() is a method
        return len(self.cards)

    # Gets an item from the cards list
    def __getitem__(self, pos):
        # operator overloading!!. Since self.cards is a list [pos] works on it, but if we want to get a card from out
        # deck object, without this method we would have to call Deck.cards[pos]. because of this we can call just
        # Deck[pos]
        return self.cards[pos]

    @staticmethod
    def spades_high(card):
        suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]
