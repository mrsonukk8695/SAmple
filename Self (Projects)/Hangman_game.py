from random import choice
import os
words = ['python', 'java', 'javascript', 'kotlin', 'ruby', 'swift', 'mysql', 'bash']

# Randomly choose a word from the list
choose_word = choice(words)
print(choose_word)

attempts = 8  # Number of allowed attempts
def welcome_message():
    print("Welcome to Hangman!!")
    print("You have guess the correct word within 8 attempts...")

def run_game(attempts):
    welcome_message()
    word_display = [ "_" for _ in choose_word]  # Create a list of underscores
    while attempts > 0 and '_' in word_display:
        print(' '.join(word_display))
        guess = input("Guess a letter: ").lower()
        if guess in choose_word:
            for index, letter in enumerate(choose_word):
                if letter == guess:
                    word_display[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1
        clear_terminal()
    if '_' not in word_display:
        return attempts

def clear_terminal():
    os.system('cls')


# Main Hangman Game starts from here:
attempt = run_game(attempts = 8)
print("You guess correctly,".upper(), f"The word was '{choose_word}', and remaining attempts were {attempt} out of {attempts}.")
