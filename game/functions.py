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
            print("{:^70}".format("Please Choose option 1(PLAY AGAIN), 2(RULES) or 3(EXIT)"))
            

# FIX INFINITE LOOP WITH CHOICE 1 - takes you back to home_screen and starts all over.
# Maybe do best of 5 or something then end game or choose to play again
def play_game():
    """
    Game logic user choice and
    computer choice
    """
    clear_terminal()
    
    # Initialize scores
    user_score = 0
    computer_score = 0
    
    # Game options
    game_choices = [rock, paper, scissors]
    
    # Play until someone reaches 5 points
    while user_score < 5 and computer_score < 5:
        #User Choice logic
        while True:
            try:
                # User Choice
                user_choice = int(input("Type 0 for rock, 1 for paper, 2 for scissor. \n => "))
                
                clear_terminal()
                
                if user_choice not in [0, 1, 2]:
                    print("Invalid integer please choose 0, 1, or 2")
                else:
                    break # Break the loop if the input is valid
            
            except ValueError:
                print("Invalid input. Please choose a number.")
        
        # Computer Choice
        computer_choice = random.randint(0, 2)
        
        # print user choice / computer choice
        print("User Choice: ", game_choices[user_choice])
        print("Computer Choice: ", game_choices[computer_choice])
        
        # Call the hand_choice_text funtion texts 
        choice_text = hand_name_text(user_choice, computer_choice)
        
        # Update scores based on the outcome
        user_score, computer_score = update_scores(user_choice, computer_choice, user_score, computer_score)
        
        # Display scores
        print(f"User Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        
    # Determine and print the winner
    if user_score > computer_score:
        print("You Win!")
    elif user_score < computer_score:
        print("Computer Wins!")
    else:
        print("It's a tie!")        
        

    
def hand_name_text(user_choice, computer_choice):
    """
    Text for hand drawn 
    from both user and computer
    """
    if user_choice >= 0:
        user_text = ""
        if user_choice == 0:
            user_text = "You chose 'Rock'"
        elif user_choice == 1:
            user_text = "You chose 'Paper'"
        else:
            user_text = "You chose 'Scissor'"
        print(user_text) 
        
    if computer_choice >= 0:
        computer_text = ""
        if computer_choice == 0:
            computer_text = "Computer chose 'Rock'"
        elif computer_choice == 1:
            computer_text = "Computer chose 'Paper'"
        else:
            computer_text = "Computer chose 'Scissor'"
        print(computer_text)
        
        
def update_scores(user_choice, computer_choice, user_score, computer_score,):
    """
    Update scores based on the
    outcome of the round
    """
    if user_choice == computer_choice:
        # Draw, no score change
        return user_score, computer_score # Draw no score change
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice ==1):
        # User wins the round, update user's score
        user_score +=1
    else:
        # Computer wins the round, update computer's score
        computer_score +=1
        
    return user_score, computer_score

   
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
    # update_scores()
    

if __name__ == "__main__":
    main()