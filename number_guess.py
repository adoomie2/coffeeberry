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

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"

BANNER = r"""
 _   _                 _                       ____
| \ | | _____      __| | ___  _ __ ___   ___ |  _ \ __ _ _ __ ___  ___
|  \| |/ _ \ \ /\ / /|/ _ \| '_ ` _ \ / _ \| |_) / _` | '__/ _ \/ __|
| |\  |  __/\ V  V /| | (_) | | | | | |  __/|  __/ (_| | | |  __/\__ \
|_| \_|\___| \_/\_/ |_|\___/|_| |_| |_|\___||_|   \__,_|_|  \___||___/
""".strip("\n")


def choose_difficulty():
    """Ask the player to choose a difficulty level."""
    while True:
        choice = input(f"{CYAN}Choose difficulty (easy/medium/hard): {RESET}").strip().lower()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print(f"{YELLOW}Invalid choice. Please select easy, medium, or hard.{RESET}")


def get_guess(upper_limit):
    """Prompt the player for a guess."""
    while True:
        try:
            guess = int(
                input(f"{CYAN}Guess a number between 1 and {upper_limit}: {RESET}")
            )
            if 1 <= guess <= upper_limit:
                return guess
            print(
                f"{RED}Please enter a number between 1 and {upper_limit}.{RESET}"
            )
        except ValueError:
            print(f"{RED}Please enter a valid number.{RESET}")


def provide_feedback(guess, target):
    """Give feedback about a guess.

    Returns True if the guess was correct, otherwise False.
    """
    if guess < target:
        print(f"{BLUE}{random.choice(FUNNY_LOW)}{RESET}")
    elif guess > target:
        print(f"{RED}{random.choice(FUNNY_HIGH)}{RESET}")
    else:
        return True

    close = abs(guess - target) <= 10
    if close:
        direction = "higher" if guess < target else "lower"
        print(f"{YELLOW}Hint: Try a bit {direction}!{RESET}")

    print(f"{YELLOW}Warm!{RESET}" if close else f"{CYAN}Cold!{RESET}")
    return False


def play():
    """Play a round of the number guessing game."""
    print(f"{CYAN}{BANNER}{RESET}")
    print(f"{GREEN}Welcome to the Number Guessing Game!{RESET}")
    upper_limit = choose_difficulty()
    target = random.randint(1, upper_limit)
    attempts = 0

    while True:
        guess = get_guess(upper_limit)
        attempts += 1

        if provide_feedback(guess, target):
            score = max(0, 101 - attempts)
            print(f"{GREEN}Correct! You guessed it in {attempts} tries.{RESET}")
            print(f"{GREEN}Your score: {score}{RESET}")
            break


if __name__ == "__main__":
    play()
