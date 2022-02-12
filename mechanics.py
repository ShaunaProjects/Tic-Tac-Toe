import random

class Mechanics():
    def __init__(self):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.board_spaces = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.player_moves = []
        self.computer_moves = []

    def show_board(self):
        print(f"  {self.board_spaces[0]}  |  {self.board_spaces[1]}  |  {self.board_spaces[2]}")
        print("_____|_____|_____")
        print(f"  {self.board_spaces[3]}  |  {self.board_spaces[4]}  |  {self.board_spaces[5]}")
        print("_____|_____|_____")
        print(f"  {self.board_spaces[6]}  |  {self.board_spaces[7]}  |  {self.board_spaces[8]}")
        print("     |     |     ")

    def check_for_win(self):
        win_values = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for win_combo in win_values:
            if all(value in self.player_moves for value in win_combo):
                print("Congratulations, you win!")
                return True
            elif all(value in self.computer_moves for value in win_combo):
                print("Sorry, you lose.")
                return True
        if len(self.player_moves) + len(self.computer_moves) == 9:
            print("It's a draw.")
            return True
        else:
            return False

    def player_turn(self):
        turn = True
        while turn:
            try:
                player_choice = int(input("What's your move? "))
                if player_choice not in self.player_moves and player_choice not in self.computer_moves:
                    self.player_moves.append(player_choice)
                    self.values[player_choice - 1] = "x"
                    self.board_spaces[player_choice - 1] = "x"
                    self.show_board()
                    turn = False
                else:
                    print("Sorry, that space is already taken. Please pick another space.")
            except ValueError:
                print("Sorry, that's not a valid input. Please type the numbers 1-9.")

    def computer_turn(self):
        turn = True
        while turn:
            computer_choice = random.choice(self.values)
            if computer_choice != "x" and computer_choice != "o":
                self.computer_moves.append(computer_choice)
                self.values[computer_choice - 1] = "o"
                self.board_spaces[computer_choice - 1] = "o"
                turn = False
                print(f"The computer chose {computer_choice}")
                self.show_board()