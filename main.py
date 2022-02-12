from art import logo
import random
from mechanics import Mechanics

run = Mechanics()

def game():
    print(logo)
    print("Welcome to Tic Tac Toe! You will be using 'x' while the computer uses 'o'. The spaces in the board are:\n"
          "1, 2, 3,\n"
          "4, 5, 6,\n"
          "7, 8, 9 ")
    run.show_board()
    first_player = random.choice(["player", "computer"])
    print(f"The {first_player} will go first.")
    game_over = False
    while not game_over:
        if first_player == "player":
            run.player_turn()
            if run.check_for_win():
                game_over = True
            else:
                run.computer_turn()
                if run.check_for_win():
                    game_over = True
        else:
            run.computer_turn()
            if run.check_for_win():
                game_over = True
            else:
                run.player_turn()
                if run.check_for_win():
                    game_over = True
        if game_over:
            select = False
            while not select:
                new_game = input("Would you like to play again? Type 'Y' or 'N': ").lower()
                if new_game == "n":
                    print("Thank you for playing! Have a great day.")
                    select = True
                elif new_game == "y":
                    select = True
                    run.values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    run.computer_moves = []
                    run.player_moves = []
                    run.board_spaces = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                    game()
                else:
                    print("That's not a valid input. Please type only 'Y' or 'N'.")

game()
