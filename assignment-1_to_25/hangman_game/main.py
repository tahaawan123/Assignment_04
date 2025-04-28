import random

stages =['''
    --------
    |        |
    |
    |
    |
    |
    --------
'''
    ,
'''
    --------
    |      |
    |      O
    |     /|
    |
    |
    |
    --------
''',    

'''
--------
|      |
|      O
|     /|\\
|     /
|
--------
''',
'''
--------
|      |
|      O
|     /|\\
|     / \\
|
--------
''']

words = ["apple", "banana", "grape", "orange", "kiwi", "mango", "peach", "pear", "plum", "berry"]

chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word] 
guess_letters = []
lives = 5

print("Welcome to the Hangman game!")
print("Guess the fruits word.")

while True:
    print(" ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid letter.\n")
        continue
    if guess in guess_letters:
        print("You already guessed that letter. Try again.\n")
        continue
    guess_letters.append(guess)

    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word. You lose a life.")
        
        print(stages[len(stages) - lives - 1])
        lives -= 1
        print("Lives left:", lives)


        if lives == 0:
            print(stages[lives])
            print("You lose! The word was:", chosen_word)
            break
