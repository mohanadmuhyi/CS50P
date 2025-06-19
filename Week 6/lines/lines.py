import sys
complexity = 0
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        for line in file:
            if not line.strip().startswith("#") and not line.isspace() and line != "":
                complexity += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(complexity)
