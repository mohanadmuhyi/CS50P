text = input("input: ")
print("Output: ", end="")

for i in range(len(text)):
    if text[i] in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
        continue
    else:
        print(text[i], end="")

print()
