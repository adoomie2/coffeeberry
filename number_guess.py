import random

print("🎯 Number Guessing Game!")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        score = max(0, 101 - attempts)
        print(f"Correct! You guessed it in {attempts} tries.")
        print(f"Your score: {score}")
        break
