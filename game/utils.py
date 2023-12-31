import time
import os


def delay_print(text, delay):
    """
    Delays the print statment
    Parameters:
        text (string) - text to be printed out
        delay (integer) - the number of second to delay by
    """
    print("", text)
    time.sleep(delay)
    
def clear_terminal():
    """
    Clears the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')