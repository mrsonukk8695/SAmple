import random, os
emojis = { 'r': '🪨', 's': '✂️','p': '📃'}
choice = ('r', 'p', 's')

try:
    while True:
        os.system('cls')
        print("Welcome to the Rock, Paper, Scissors Game!")
        user_choice = input ("Rock, paper, scissors? (r/p/s): ").lower()
        computer_choice = random.choice(choice)
        print(f"You chose {emojis[user_choice]}, computer chose {emojis[computer_choice]}.")
        if user_choice == computer_choice:
            print("It's a tie!".upper())
        elif (user_choice== 'r' and computer_choice== 's') or (user_choice== 'p' and computer_choice== 'r') or (user_choice== 's' and computer_choice=='p'):
            print("User Wins!!".upper())
        else:
            print("User loses!".upper())
        options = input("Want to play again??? ([y]es/[n]o): ")
        if options.lower() == 'y':
            continue
        elif options.lower() == 'n':
            break
        else:
            print("Invalid option. Exiting the game.")
            break
except KeyError:
    print("Invalid choice. Please enter your choice [r]ock, [p]aper, [s]cissors")
    