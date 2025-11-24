import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

'''
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
'''
class Board:
    def __init__(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()            

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker
        # self.squares[key] get the Square object at chosen position
        # .marker calls the marker property setter

    def unused_squares(self):
        return [key for key, square in self.squares.items() if square.is_unused()]

    def is_unused_square(self, key):
        return self.squares[key].is_unused()

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

    def get_square(self, keys):

        square =  [key for key in keys
                    if self.squares[key].marker == Square.INITIAL_MARKER]
        return square[0] if square else None




class Player:
    def __init__(self, marker):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
         super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )

    def __init__(self, first_player):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.computer_wins_count = 0
        self.human_wins_count = 0
        self.first_player = first_player


    def play(self):
        self.display_welcome_message()
        while True:
            self.play_one_game()
            print(f"Total human wins - {self.human_wins_count}")
            print(f"Total computer wins - {self.computer_wins_count}") 
            if self.computer_wins_count >= 3 or self.human_wins_count >= 3:
                break
            if not self.play_again():
                break

        self.display_goodbye_message()

    def play_one_game(self):       
        self.board = Board() # instantiate a new board
        self.board.display()

        current_player = self.first_player
        
        while True:
            self.player_moves(current_player)         
            if self.is_game_over():
                break

            self.board.display_with_clear()
            current_player = self.toggle_player(current_player)           
        
        self.board.display_with_clear()
        self.display_results()

    def player_moves(self, current_player):
        if current_player == 'human':
            self.human_moves()
        elif current_player == 'computer':
            self.computer_moves()

    def toggle_player(self, current_player):
        if current_player == "human":
            return "computer"
        elif current_player == "computer":
            return "human"
    
    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing. Goodbye!")

    def display_results(self):
        if self.is_winner(self.human):
            self.human_wins_count += 1
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            self.computer_wins_count += 1
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    def play_again(self):
        prompt = "Do you want to play again? Y or N: "
        while True:
            answer = input(prompt).lower()
            if answer in ("y", "n"):
                break
            print("That's not a valid option.\n")
        
        return answer == 'y'

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    @staticmethod
    def _join_or(choices, delimiter=", ", word="or"):
        if len(choices) == 1:
            return str(choices[0])
        if len(choices) == 2:
            return f"{choices[0]} {word} {choices[1]}"

        return f"{delimiter.join(choices[:-1])}{delimiter}{word} {choices[-1]}"

    def human_moves(self):
        choice = None
        valid_choices = self.board.unused_squares()
        choices_list = [str(choice) for choice in valid_choices]
        choics_str = TTTGame._join_or(choices_list)

        while True:
            prompt = f"Choose a square ({choics_str}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry that's not a valid choice.")
            print() # prints another line

        self.board.mark_square_at(choice, self.human.marker)

    def get_row(self, strategy):
        if strategy == 'defensive':
            player = self.human
        elif strategy == "offensive":
            player = self.computer

        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.board.count_markers_for(player, row) == 2:
                if any(self.board.is_unused_square(k) for k in row):
                    return row
        return None


    def computer_moves(self):
        threatened_row = self.get_row("defensive")
        winning_row = self.get_row("offensive")
        valid_choices = self.board.unused_squares()

        if 5 in valid_choices:
            choice = 5
        elif winning_row:
            choice = self.board.get_square(winning_row)
        elif threatened_row:
            choice = self.board.get_square(threatened_row)
        else:
            choice = random.choice(valid_choices)
        
        self.board.mark_square_at(choice, self.computer.marker)

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or self.is_winner(self.computer))


game = TTTGame('computer')
game.play()