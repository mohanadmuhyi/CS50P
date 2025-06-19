def main():
    text = input("Enter a string: ")
    print(convert(text))

def convert(text):
    new = text.replace(":)", "🙂").replace(":(", "🙁")
    return new

main()
