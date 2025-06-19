import sys
import csv
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

names = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        names.append({"fname": "first", "lname" : "last", "house": "house"})
        for row in reader:
            lname, fname = row["name"].split(", ")
            names.append({"fname": fname, "lname" : lname, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["fname", "lname", "house"])
    for row in names:
        writer.writerow(row)
