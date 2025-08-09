import random

DIFFICULTIES = {"easy": 50, "medium": 100, "hard": 500}

FUNNY_LOW = [
    "Too low! Even a limbo champion can't go that low!",
    "Too low! My pet turtle moves faster than your guesses!",
    "Too low! Are you digging for treasure?",
]

FUNNY_HIGH = [
    "Too high! That guess just left the atmosphere!",
    "Too high! Careful, you'll get a nosebleed up there!",
    "Too high! The number isn't on Mars, you know!",
]


def choose_difficulty():
    """Ask the player to choose a difficulty level."""
    while True:
        choice = input("Choose difficulty (easy/medium/hard): ").strip().lower()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Invalid choice. Please select easy, medium, or hard.")


def get_guess(upper_limit):
    """Prompt the player for a guess."""
    while True:
        try:
            return int(input(f"Guess a number between 1 and {upper_limit}: "))
        except ValueError:
            print("Please enter a valid number.")


def provide_feedback(guess, target):
    """Give feedback about a guess.

    Returns True if the guess was correct, otherwise False.
    """
    if guess < target:
        print(random.choice(FUNNY_LOW))
    elif guess > target:
        print(random.choice(FUNNY_HIGH))
    else:
        return True

    print("Warm!" if abs(guess - target) <= 10 else "Cold!")
    return False


def play():
    """Play a round of the number guessing game."""
    print("🎯 Number Guessing Game!")
    upper_limit = choose_difficulty()
    target = random.randint(1, upper_limit)
    attempts = 0

    while True:
        guess = get_guess(upper_limit)
        attempts += 1

        if provide_feedback(guess, target):
            score = max(0, 101 - attempts)
            print(f"Correct! You guessed it in {attempts} tries.")
            print(f"Your score: {score}")
            break


if __name__ == "__main__":
    play()
