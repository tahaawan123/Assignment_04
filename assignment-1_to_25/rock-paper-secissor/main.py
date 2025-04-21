import random
print("Welcome to the Rock Paper Scissors game!")


choices = ["rock", "paper", "scissors"]
user_score = computer_score = 0
print("Lets play!")

while True:
    user_input = input("Type rock, paper, scissors or Q to quit: ").lower()
    if user_input == "q":
        print(f"Final score - You: {user_score},  Computer {computer_score}")
        print("Thanks for playing!")
        break
    if user_input not in choices:
        print("Invalid input, please try again.")
        continue
    computer_chose = random.choice(choices)
    print(f"Computer chose { computer_chose}. ")
    if user_input == computer_chose:
        print("It's a tie!")
    elif (user_input == "rock" and computer_chose == "scissors") or \
         (user_input == "paper" and computer_chose == "rock") or \
         (user_input == "scissors" and computer_chose == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1
    print(f"Score - You: {user_score}, Computer: {computer_score}")


