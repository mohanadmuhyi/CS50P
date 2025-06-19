import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        values = re.search(r'<iframe.*src="(.+)"', s)
        url = values.group(1)
    except AttributeError:
        return None
    if matches := re.fullmatch(r"https?://(?:www\.)?youtube\.com/embed/(.+)", url):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
