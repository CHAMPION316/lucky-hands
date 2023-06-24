""" Imports for game functionality """
import random
import operator
import keyboard
import sys

from .drawings import logo, game_images
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
    game_choices = game_images
    for choice in game_choices:
        print(choice)
    
# (Here I will probably create a def play() section when ready)
    
def main():
    """
    The main game loop
    """
    home_screen()
    

if __name__ == "__main__":
    main()