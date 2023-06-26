""" Imports for game functionality """
import random
import operator
import sys

from .drawings import logo, rock, paper, scissors
from .utils import delay_print, clear_terminal


def home_screen():
    """
    Home screen options and inputs
    for opening game
    """
    clear_terminal()
    logo()
    print("\n" * 2)
    delay_print("{:^50}".format("1: PLAY GAME"), 1)
    delay_print("{:^50}".format("2: RULES"), 1)
    delay_print("{:^50}".format("3: EXIT"), 1)
    print("\n" * 2)
    
    while True:
        home_screen_choice = input(" " * 17 + "Please choose an option : ")
        if home_screen_choice == "1":
            play_game()
        elif home_screen_choice == "2":
            clear_terminal()
            print(game_rules)
            print("\n")
            
            while True:
                if input(" " * 12 + "RETURN TO MAIN MENU? (Y) : ").upper() == "Y":
                    clear_terminal()
                    home_screen()
                else:
                    print("{:^70}".format("Please Try Again"))
        elif home_screen_choice == "3":
            clear_terminal()
            sys.exit()
        else:
            print("{:^70}".format("Please Choose option 1, 2 or 3"))
            

#FIX INFINITE LOOP WITH CHOICE 1 - takes you back to home_screen and starts all over.
# Maybe do best of 5 or something then end game or choose to play again
def play_game():
    """
    Game logic user choice and
    computer choice
    """
    clear_terminal()
    # Game options
    game_choices = [rock, paper, scissors]
    # User choice
    user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor. \n => "))
    print("User Choice: ")
    print(game_choices[user_choice])
    # Computer Choice
    computer_choice = random.randint(0, 2)
    print("Computer Choice: ")
    print(game_choices[computer_choice])


# Game rules explained - option 3 in home_screen()
game_rules = ("The game is simple, you win by drawing the correct hand. \n"
              "You will have three total choices to choose from \n"
              "which are as follows. \n"
              "rock, paper, and scissors \n"
              "Rock beats Scissors \n"
              "Scissors beats Paper \n"
              "Paper beats Rock \n"
              "The user will choose first followed by \n"
              "the computer. Now choose wisely......")

    
def main():
    """
    The main game loop
    """
    home_screen()
    play_game()
    

if __name__ == "__main__":
    main()