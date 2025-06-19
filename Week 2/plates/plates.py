def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # 0 1 2 3 4 5
    # x x x x x x

    if len(s) > 6 or len(s) < 2: # to eliminate lengths not between 2 and 6
        return False

    if s[0].isdigit() or s[1].isdigit(): # to eliminate if first char or second char is a number
        return False

    total = 0 # gonna be used in calculating weights

    for i in range(len(s)):

        if not s[i].isdigit() and not s[i].isalpha(): # to eliminate spaces, punc and periods
            return False

        if s[i].isdigit():

            if total == 0 and s[i] == "0": # to eliminate if first number is 0
                return False

            total += i # calculate weight

    if len(s) == 4 and total not in [0, 3, 5]: # checks if __xx or ___x or ____
        return False
    if len(s) == 5 and total not in [0, 4, 7, 9]: # checks if __xxx or ___xx or ____x or _____
        return False
    if len(s) == 6 and total not in [0, 5, 9, 12, 14]: # checks if __xxxx or ___xxx or ____xx or _____x or ______
        return False

    return True

main()
