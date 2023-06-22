import operator
import sys

from .utils import delay_print

def logo():
    """
    Text for the game logo
    """
    delay_print(r"""
   __            _                                  _     
  / / _   _  ___| | ___   _    /\  /\__ _ _ __   __| |___ 
 / / | | | |/ __| |/ / | | |  / /_/ / _` | '_ \ / _` / __|
/ /__| |_| | (__|   <| |_| | / __  / (_| | | | | (_| \__ \
\____/\__,_|\___|_|\_\\__, | \/ /_/ \__,_|_| |_|\__,_|___/
                      |___/                               
""", 2)