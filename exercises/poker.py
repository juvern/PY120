import random

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    def __init__(self):        
        self.new_deck()
        
    def new_deck(self):
        self.deck_of_cards = []
        
        for suit in Deck.SUITS:
            for rank in Deck.RANKS:
                self.deck_of_cards.append(Card(rank, suit))
                
        random.shuffle(self.deck_of_cards)
        
    def draw(self):
         
        if not self.deck_of_cards: # if empty deck
            self.new_deck()
            
        return self.deck_of_cards.pop()


class Card:
    VALUES = {
        'Jack': 11,
        'Queen': 12,
        'King': 13, 
        'Ace': 14,
    }
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    @property        
    def value(self):
        return Card.VALUES.get(self.rank, self.rank) # accessing a class level constant
        
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    
    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.value < other.value
    
    # not needed
    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.value > other.value
            
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.rank == other.rank and self.suit == other.suit       
    

class PokerHand:
    def __init__(self, deck): # accepts a Deck object
        self.drawn = []
        
        for _ in range(5):
            self.drawn.append(deck.draw())

    def print(self):
        for card in self.drawn:
            print(card)

    def evaluate(self):



        
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    # ace, king, queen, jack, and ten, all of the same suit
    def _is_royal_flush(self):
        royal_flush_ranks = ['Jack', 'Queen', 'King', 'Ace', 10]

        suits = [card.suit for card in self.drawn]
        ranks = [card.rank for card in self.drawn if card.rank in royal_flush_ranks]

        if len(set(suits)) == 1 and len(set(ranks)) == 5:
            return True

        return False

    # sequential ranks, all of the same suit
    def _is_straight_flush(self):

        suits = [card.suit for card in self.drawn]

        if len(set(suits)) == 1:
            values = [card.value for card in self.drawn]
            values.sort()
            
            for idx in range(1, 5):
                if values[idx] - values[idx - 1] != 1:
                    return False
        else:
            return False

        return True


    def _is_four_of_a_kind(self):
        ranks = [card.rank for card in self.drawn]
        
        for rank in ranks:
            if ranks.count(rank) == 4:
                return True

        return False

    # three of a kind and a pair
    def _is_full_house(self):
        ranks = [card.rank for card in self.drawn]
        return all([ranks.count(rank) == 3 or ranks.count(rank) == 2  for rank in ranks])

    # same suits
    def _is_flush(self):
        suits = [card.suit for card in self.drawn]

        if len(set(suits)) == 1:
            return True

        return False

    # sequential
    def _is_straight(self):
        values = [card.value for card in self.drawn]
        values.sort()
        
        for idx in range(1, 5):
            if values[idx] - values[idx - 1] != 1:
                return False

        return True

    def _is_three_of_a_kind(self):
        ranks = [card.rank for card in self.drawn]
        
        for rank in ranks:
            if ranks.count(rank) == 3:
                return True

        return False

    def _is_two_pair(self):
        ranks = [card.rank for card in self.drawn]
        return set(ranks) == 3

    def _is_pair(self):
        ranks = [card.rank for card in self.drawn]
        
        for rank in ranks:
            if ranks.count(rank) == 2:
                return True

        return False

# hand = PokerHand(Deck())
# hand.print()
# print(hand.evaluate())
# print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self.deck_of_cards = list(cards)

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print("Royal flush")
print(hand.evaluate() == "Royal flush")
print("----")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print("Straight flush")
print(hand.evaluate() == "Straight flush")
print("----")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print("Four of a kind")
print(hand.evaluate() == "Four of a kind")
print("----")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print("Full house - Three of a kind and a pair")
print(hand.evaluate() == "Full house")
print("----")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print("Flush - same suit")
print(hand.evaluate() == "Flush")
print("----")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print("Straight")
print(hand.evaluate() == "Straight")
print("----")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print("Straight")
print(hand.evaluate() == "Straight")
print("----")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print("Three of a kind")
print(hand.evaluate() == "Three of a kind")
print("----")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print("Two pair")
print(hand.evaluate() == "Two pair")
print("----")


hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print("Pair")
print(hand.evaluate() == "Pair")
print("----")


hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print("High card")
print(hand.evaluate() == "High card")
print("----")

