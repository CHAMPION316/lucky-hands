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
    delay_print((input(" " * 17 + "PRESS ENTER TO PLAY")), 1)
    print("\n" * 2)


# (Here I will probably create a def play() section when ready)

def play_game():
    """
    Game logic user choice and
    computer choice
    """
    # Game options
    game_choices = [rock, paper, scissors]
    # User choice
    user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissor. \n => "))
    print("User Choice: ")
    print(game_choices[user_choice])
    
    
def main():
    """
    The main game loop
    """
    home_screen()
    play_game()
    

if __name__ == "__main__":
    main()