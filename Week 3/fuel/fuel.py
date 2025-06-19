while True:
    try:
        fraction = input("fraction: ")
        x, y = fraction.split("/")
        value = int(x)/int(y)*100
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        if int(x) <= int(y):
            break

if value <= 1:
    print("E")
elif value >= 99:
    print("F")
else:
    print(f"{int(round(value))}%")
