import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        trials = 0
        x, y = generate_integer(level), generate_integer(level)
        for j in range(3):
            try:
                print(f"{x} + {y} = ", end="")
                answer = int(input())
            except ValueError:
                print("EEE")
                trials += 1
            else:
                if answer == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    trials += 1
        if trials == 3:
            print(f"{x} + {y} = {x+y}")
    print(f"Score: {score}")




def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                return level


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
