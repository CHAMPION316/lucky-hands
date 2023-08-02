""" Imports for game functionality """
from .functions import play_game
from .utils import delay_print, clear_terminal


def update_scores(user_choice, computer_choice, user_score, computer_score,):
    """
    Update scores based on the
    outcome of the round
    """
    # Game rules to determine the winner
    if user_choice == computer_choice:
        return user_score, computer_score # Draw no score change
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice ==1):
        user_choice +=1
    else:
        computer_choice +=1
        
    return user_choice, computer_choice