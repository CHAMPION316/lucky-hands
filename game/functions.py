""" Imports for game functionality """
import random
import operator
import keyboard
import sys

from .drawings import logo
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
    print("LOOKING GOOD")
    
def main():
    """
    The main game loop
    """
    home_screen()
    

if __name__ == "__main__":
    main()