# Refactoring : Changing the structure of the code without changing its functionality.
# Modularization : Breaking down a large program into smaller reusable parts called modules or functions.
# DRY (Don't Repeat Yourself)  # Most important that should take care
import random, os

ROCK = 'r'
PAPER = "p"
SCISSOR = "s"
emojis = {ROCK: '🪨', SCISSOR: '✂️', PAPER: '📃'}
def clearing_terminal():
    return os.system('cls')

def get_input():
    choice = tuple(emojis.keys())                                     # A tuple containing the name of the characters which are used in the game.
    user_choice = input ("Rock, paper, scissors? (r/p/s): ").lower()  # taking input from the user
    computer_choice = random.choice(choice)                           # taking input from the computer using random module
    return user_choice, computer_choice                               # return the choice which are gerenrated by the user and computer.

def display_choice(user_choice, computer_choice):
                           # Dictionary containing letter and emojis for each character.
    return (f"Yous choice: {emojis[user_choice]}, and Computer's choice: {emojis[computer_choice]}.")       # Converting characters into emojis adn displaying that to user.

def play_game(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!".upper())
    elif (user_choice==ROCK and computer_choice== SCISSOR) or (user_choice== PAPER and computer_choice==ROCK) or (user_choice== SCISSOR and computer_choice==PAPER):
        print("User Wins!!".upper())
    else:
        print("User loses!".upper())
# Main program start's from here: 
try:
    while True:
        clearing_terminal()
        user_choice, computer_choice = get_input()
        print(display_choice(user_choice, computer_choice))
        play_game(user_choice, computer_choice)
        options = input("Want to play again??? ([y]es/[n]o): ")
        if options.lower() == 'y':
            continue
        elif options.lower() == 'n':
            break
        else:
            print("Invalid option. Exiting the game.")
            break
except KeyError:
    print("Invalid choice.")
    