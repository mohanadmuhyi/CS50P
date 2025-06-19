camel = input("camelCase: ")

print("snake_case: ", end="")

for i in range(len(camel)):
    if camel[i].isupper():
        print(f"_{camel[i].lower()}", end="")
    else:
        print(camel[i], end="")
print()
