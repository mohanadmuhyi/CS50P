def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        first, second, third, fourth = ip.strip().split(".")
    except ValueError:
        return False
    else:
        if int(first) in range(256) and int(second) in range(256) and int(third) in range(256) and int(fourth) in range(256):
            return True
        else:
            return False
if __name__ == "__main__":
    main()
