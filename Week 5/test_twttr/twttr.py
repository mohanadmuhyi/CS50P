import string
def main():
    text = input("input: ")
    print(f"Output: {shorten(text)}")


def shorten(word):
    for i in word:
        if i in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"] or i.isdigit() or i in string.punctuation:
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()
