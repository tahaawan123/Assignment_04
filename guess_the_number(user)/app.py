import random 


print("Welcome to the Number Guessing Game!")

guessed_number =   random.randint(1, 10)
print("Guess a number between 1 and 10")


while True:
    try:
        user_input = int(input("Enter your guess: "))
        if user_input < guessed_number:
            print("Too low! Try again.")
        elif user_input > guessed_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
    
        
        

 