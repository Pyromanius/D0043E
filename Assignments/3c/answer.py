import random

secret_no = random.randint(1, 20)
no_guesses = 0

print("I am thinking of a number between 1 and 20")

while True:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Please enter digits only")
        continue
    guess_int = int(guess)
    if guess_int < 1 or guess_int > 20:
        print("Out of range! Guess again.")
        continue
    no_guesses += 1
    if guess_int < secret_no:
        print("Too low!")
    elif guess_int > secret_no:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {no_guesses} attempts.")
        break
    if no_guesses == 5:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_no}.")
        break
