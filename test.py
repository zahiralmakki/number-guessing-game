# 100 Days of code
# Day 12 Project: Guess the number
# 1/2/2025

import random


print("Welcome to the Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
game_over = False
easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard' :")
if easy_or_hard == "easy":
    attempts = 10
else:
    attempts = 5
    
while not game_over:    
    print(f"You have {attempts} remaining to guess the number.")

    guess = int(input("Make a guess: "))
    
    if guess > secret_number:
        attempts -= 1
        print("Too high.")
    elif guess < secret_number:
        attempts -= 1
        print("Too low.")
    else:
        print(f"You got it, the answer was {secret_number}.")
        game_over = True
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        game_over = True


