from random import randint


while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice =='y':
        dice_1 = randint(1, 6)
        dice_2 = randint(1, 6)
        total_roll = dice_1 + dice_2
        print(f"You rolled {dice_1} and {dice_2}.")
    elif choice == 'n':
        print("Thanks for playing! ")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")