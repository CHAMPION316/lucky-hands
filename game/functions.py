""" Imports for game functionality """
import random
import operator
import keyboard
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
    delay_print("{:^70}".format(input("PRESS ENTER TO PLAY")), 1)
    clear_terminal()
    
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