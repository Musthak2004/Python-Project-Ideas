# Number guessing game
import random

# Using functions for readable
def guess_the_number():
    print("I am thinking of a number between 1 and 20...")
    secret_number = random.randint(1, 20)

    for i in range(1, 4):
        guess = int(input("\nEnter your guess: "))

        if guess > secret_number:
            print('Guess: Too High!')
        elif guess < secret_number:
            print('Guess: Too Low!')
        else:
            break # user guess number correct or miss 3 chances

    if guess == secret_number:
        print(f"Good job! You guessed my number in {str(i)} guesses!")
    else:
        print(f"Nope. The number I was thinking of was {str(secret_number)}")
    
guess_the_number()