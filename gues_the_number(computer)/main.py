import random

print("Welcome to the Number Guessing Game!")



high = 15 
low = 1


print(f"Please guess a number between {low} and {high}. and computer will be guess it.")

if low <= high:
    computer_guess = random.randint(low, high)
    print(f"Computer guessed: {computer_guess}")

    while True:
        user_input = input("Is the guess too high (H), too low (L), or correct (C)? ").strip().upper()

        if user_input == 'H':
            high = computer_guess - 1
            computer_guess = random.randint(low, high)
            print(f"Computer guessed: {computer_guess}")
        elif user_input == 'L':
            low = computer_guess + 1
            computer_guess = random.randint(low, high)
            print(f"Computer guessed: {computer_guess}")
        elif user_input == 'C':
            print("Computer guessed your number!")
            break
        else:
            print("Invalid input. Please enter H, L, or C.")

if low > high:
    print("Invalid range. Please ensure that the low number is less than or equal to the high number.")
