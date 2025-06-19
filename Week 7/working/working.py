import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.fullmatch("([0-1]?[0-9])(:[0-5][0-9])? (AM|PM) to ([0-1]?[0-9])(:[0-5][0-9])? (AM|PM)", s):
        return f"{fix(matches.group(1), matches.group(2), matches.group(3))} to {fix(matches.group(4), matches.group(5), matches.group(6))}"
    else:
        raise ValueError

def fix(hour, min, meridiem):
    if min == None:
        min = "00"
    else:
        min = str(min).replace(":", "")

    if meridiem == "PM" and hour != "12":
        return f"{int(hour)+12}:{min}"
    elif meridiem == "AM" and hour == "12":
        return f"00:{min}"
    else:
        return f"{int(hour):02}:{min}"

if __name__ == "__main__":
    main()
