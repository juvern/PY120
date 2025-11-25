'''
- write a textual description of problem
- extract nouns and verbs
- organise and associate verbs with nouns
- write scaffolding and spike code

'''
import random

class Card:
    SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    @property
    def points(self):
        try:
            return int(self.rank)
        except ValueError:
            if self.rank == "Ace":
                return 11
            else:
                return 10

'''
Deck holds all the cards available for play.
'''
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.SUITS
                    for rank in Card.RANKS] 

    def shuffle_cards(self):
        random.shuffle(self.cards)

    # deal one card at at a time and remove from deck
    def deal(self):
        return self.cards.pop()

class Participant:
    def __init__(self):
        self.hand = [] # start with an empty hand
    
    def score(self):
        total = sum(card.points for card in self.hand)
        count_aces = self.count_aces()
        if count_aces:
            return total - count_aces * 10

        return total

    def count_aces(self):
        return len([card.rank for card in self.hand if card.rank == "Ace"])

    def is_busted(self):
        return self.score() > 21
    
    def display_score(self):
        print(f"Total points is {self.score()}")

    def display_cards(self):
        print(f"{self.intro} {[f"{card}" for card in self.hand]}")                

class Player(Participant):
    def __init__(self):
        super().__init__()
        self.intro = "Your card is:"
        self.balance = 5 # Player has $5 initially to bet
        

class Dealer(Participant):
    def __init__(self):
        super().__init__()
        self.intro = "The dealer's hand is:"    

    def display_with_hidden_card(self):
        print(f"{self.intro} {['X'] + [f"{card}" for card in self.hand[1:]]}")


class TwentyOneGame:
    def __init__(self):
        # STUB
        # What attributes does the game need? A deck? Two
        #   participants?
        self.player = Player()
        self.dealer = Dealer()
        

    # keep looping until the game is over
    # game is over when either player goes bust

    @staticmethod
    def divider():
        print('==============')

    def start(self):

        self.display_welcome_message()

        while True:
            self.play_one_game()

            if self.player.balance == 0:
                break
            
            if not self.play_again():
                break
        
        self.display_goodbye_message()

    def play_one_game(self):
        self.deck = Deck() # new deck for each game
        self.deck.shuffle_cards()

        # fresh hands each game
        self.player.hand = []
        self.dealer.hand = []

        # deal two cards to player and dealer
        for _ in range(2):
            self.player.hand.append(self.deck.deal())
            self.dealer.hand.append(self.deck.deal())

        # display player's hand including points
        self.player.display_cards()
        self.player.display_score()
        TwentyOneGame.divider()

        # computer's hand with one card hidden
        self.dealer.display_with_hidden_card()
        TwentyOneGame.divider()        

        outcome = self.player_turn()
        if outcome == 'bust':
            self.display_result()
            return

        # Dealer only plays after player choose to 'stay' or if player didn't bust
        self.dealer_turn()
        self.display_result()

        


    # plays gets to hit until they choose to stay or is busted
    def player_turn(self):
        print("Your turn...")

        while True:
            
            prompt = "Do you want to hit or stay? h or s: "
            
            # keep looping until answer is valid
            while True:
                answer = input(prompt).lower()
                if answer in ('h', 's'):
                    break
                print(f"Invalid input. {prompt}")

            # if player chooses 'stay', break out of loop
            if answer == 's':
                print("You've chosen to stay")
                return 'stay'

            if answer == 'h':
                print("You've chosen to hit")
                self.player.hand.append(self.deck.deal())
                self.player.display_cards()
                self.player.display_score()
                TwentyOneGame.divider()
                if self.player.is_busted():
                    print('You busted!')
                    return 'bust'

    def dealer_turn(self):
        print("Dealer's turn...")
        self.dealer.display_cards()
        self.dealer.display_score()

        while self.dealer.score() < 17: # must hit
            print("Dealer hits!")
            self.dealer.hand.append(self.deck.deal())
            self.dealer.display_cards()
            self.dealer.display_score()
        
        if self.dealer.is_busted():
            print("The dealer has busted!")
        else:
            print("Dealer stays")


    def play_again(self):
        prompt = "Would you like to play again? y or n: "
        
        while True: 
            answer = input(prompt).lower()
            if answer in ('y', 'n'):
                break
            print(f"Invalid input. {prompt}")

        print(answer)
        return answer == 'y'


    def display_welcome_message(self):
        print("Welcome. Let's play Twenty One.")
        print(f"Your starting balance is ${self.player.balance}")
        print()

    def display_goodbye_message(self):
        print("Goodbye. See you again!")

    def decide_winner(self):
        if self.player.is_busted():
            print("Dealer has won")
            self.player.balance -= 1
        elif self.dealer.is_busted():
            print("You have won")
            self.player.balance += 1
        elif self.player.score() > self.dealer.score():
            print("Player has won")
            self.player.balance += 1
        elif self.player.score() < self.dealer.score():
            print("Dealer has won")
            self.player.balance -= 1
        else:
            print("It's a tie")


    def display_result(self):
        TwentyOneGame.divider()
        print("These are the final results.")
        self.player.display_cards()
        self.player.display_score()
        self.dealer.display_cards()
        self.dealer.display_score()
        TwentyOneGame.divider()
        self.decide_winner()
        print(f"Your balance is ${self.player.balance}.")
        print()


game = TwentyOneGame()
game.start()