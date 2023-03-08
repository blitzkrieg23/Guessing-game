import random
import sys

while True:
    level_str = input("Level: ")
    try:
        level = int(level_str)
        if level < 1:
            continue
        break
    except ValueError:
        continue

guess = random.randint(1, level)

while True:
    guess_str = input("Guess: ")
    try:
        guess_num = int(guess_str)
        if guess_num < 1:
            continue
    except ValueError:
        continue
    if guess_num < guess:
        print("Too small!")

    elif guess_num > guess:
        print("Too large!")

    else:
        print("Just right!")
        sys.exit()
