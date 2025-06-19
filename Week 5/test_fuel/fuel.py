def main():
    fraction = input("fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):

    x, y = fraction.split("/")
    value = int(x)/int(y)*100

    if int(x) <= int(y):
        return round(value)
    else:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
