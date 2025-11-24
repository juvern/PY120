'''
Keeping score
- a state of a Human object
- instance variable that increments?

Add a class Move
- single Move class and central rules table - fewer classes, but move is more generic
- class per move - logic is distributed by adding a new move will mean a new class

Keep track of a history of moves
- move should be an attribute in the Player class

'''

import random

RULES = {
    "rock":     {"beats": {"scissors", "lizard"}},
    "paper":    {"beats": {"rock", "spock"}},
    "scissors": {"beats": {"paper", "lizard"}},
    "lizard":   {"beats": {"spock", "paper"}},
    "spock":    {"beats": {"scissors", "rock"}},
}

class Player:
# responsible for choosing a move

    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')

    def __init__(self):
        self.move = None
        self.history = []


class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        choice = random.choice(Player.CHOICES)
        self.move = Move(choice)
        self.history.append(self.move.name)

class Human(Player):
    def __init__(self):
        super().__init__() # inherits from the superclass
        self.score = 0 # triggers the setter


    def choose(self):
        # choose human's move
        prompt = "Choose your move - rock, paper, scissors, lizard, spock: "
        
        while True:
            choice = input(prompt).lower()
            if choice in Player.CHOICES:
                self.move = Move(choice)
                self.history.append(self.move.name)  # append Move object
                break
            print(f"Sorry, {choice} is not valid")

        self.move = Move(choice)        

class Move:
    def __init__(self, name):
        self.name = name

    def compare(self, other):
        if self.name == other.name:
            return "tie"

        if other.name in RULES[self.name]["beats"]:
            return "win"

        return "lose"


class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print("Welcome to Rock Paper Scissors!")

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_winner(self):
        human_move = self._human.move # Move object
        computer_move = self._computer.move # Move object
        
        print(f"You chose: {human_move.name}")
        print(f"The computer chose: {computer_move.name}")

        result = Move.compare(human_move, computer_move)

        if result == "tie":
            print("It's a tie")
        elif result == "win":
            self._human.score += 1
            print("You win!")
        elif result == "lose":
            print('Computer wins!')

    def _display_history(self):
        print(f"Previously, you have chosen {self._human.history}")
        print(f"Previously, the computer has chosen {self._computer.history}")


    def _play_again(self):
        answer = input("Would you like to play again - y or n: ")
        return answer.lower().startswith('y') # return true if yes

    def play(self):
        self._display_welcome_message()


        while True:
            if self._human.history:
                self._display_history()

            self._human.choose()
            self._computer.choose()
            self._display_winner()
            print(f"You have won {self._human.score} times")
            if not self._play_again():
                break
        
        self._display_goodbye_message()



RPSGame().play()