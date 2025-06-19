names = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        break
    else:
        names.append(name)

print()
print("Adieu, adieu, to ", end="")

if len(names) == 1:
    print(names[0])
elif len(names) == 2:
    print(f"{names[0]} and {names[1]}")
else:
    for name in names[:-1]:
        print(f"{name}, ", end="")
    print(f"and {names[len(names) - 1]}")
