import random

def hot_cold_game():
    """Plays the Hot & Cold game."""
    target_number = random.randint(1, 100)
    guess = 0
    attempts = 0

    while guess != target_number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < target_number:
            print("Too low!")
        elif guess > target_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

hot_cold_game()