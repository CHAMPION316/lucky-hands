""" Imports for game functionality """
import random
import operator
import keyboard
import sys


from .utils import delay_print, clear_terminal


def logo():
    """
    Text for the game logo
    """
    delay_print("""
                
   __            _                                  _     
  / / _   _  ___| | ___   _    /\  /\__ _ _ __   __| |___ 
 / / | | | |/ __| |/ / | | |  / /_/ / _` | '_ \ / _` / __|
/ /__| |_| | (__|   <| |_| | / __  / (_| | | | | (_| \__ \
\____/\__,_|\___|_|\_\\__, | \/ /_/ \__,_|_| |_|\__,_|___/
                      |___/                               

         __
 _(\    |@@|
(__/\__ \--/ __
   \___|----|  |   __
       \ }{ /\ )_ / _\
       /\__/\ \__O (__
      (--/\--)    \__/
      _)(  )(_
     `---''---
                """, 2)


def home_screen():
    """
    Home screen options and inputs
    for opening game
    """
    clear_terminal()
    logo()
    print("\n" * 2)
    print()