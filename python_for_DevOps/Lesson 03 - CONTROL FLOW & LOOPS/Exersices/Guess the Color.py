import random

colors = ["red", "blue", "green", "yellow", "pink"]
while True:
    color = random.choice(colors)
    guess = input("Guess the color: ")
    if guess.lower() == color:
        print("Correct!")
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
    else:
        print(f"Wrong! The color was {color}")
