import pyfiglet as f
import sys


if len(sys.argv) == 1:
    text = input("input: ")
    print(f.figlet_format(text))
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    try:
        f.Figlet(font=sys.argv[2])
    except:
        sys.exit("Invalid usage")
    else:
        text = input("input: ")
        print(f.figlet_format(text, font=sys.argv[2]))
else:
    sys.exit("Invalid usage")
