import time
# Use os import below at a later time
# import os


def delay_print(text, delay):
    """
    Delays the print statment
    Parameters:
        text (string) - text to be printed out
        delay (integer) - the number of second to delay by
    """
    print("", text, delay)
    time.sleep(delay)