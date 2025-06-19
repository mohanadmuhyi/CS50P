import random
import sys

def main():
    level = get_int("Level: ")
    answer = random.randint(1, level)

    while True:
        guess = get_int("Guess: ")
        if guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            sys.exit()




def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            pass
        else:
            if number > 0:
                return number

main()
