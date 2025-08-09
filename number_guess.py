import random

print("🎯 Number Guessing Game!")

difficulties = {"easy": 50, "medium": 100, "hard": 500}

while True:
    choice = input("Choose difficulty (easy/medium/hard): ").strip().lower()
    if choice in difficulties:
        upper_limit = difficulties[choice]
        break
    print("Invalid choice. Please select easy, medium, or hard.")

number = random.randint(1, upper_limit)
attempts = 0

while True:
    guess = int(input(f"Guess a number between 1 and {upper_limit}: "))
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

    if abs(guess - number) <= 10:
        print("Warm!")
    else:
        print("Cold!")
