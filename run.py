import random

# ASCII Arts for rock, paper, and scissors by Veronica Karlsson
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  

#user choice
user_action = input("Enter a choice (rock, paper, scissors): ")

#possible outcomes
possible_actions = ["rock", "paper", "scissors"]

#computer choice
computer_action = random.choice(possible_actions)

#print statement for results
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")