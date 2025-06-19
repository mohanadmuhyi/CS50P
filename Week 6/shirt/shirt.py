from PIL import Image, ImageOps
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
file1, file2 = sys.argv[1].lower(), sys.argv[2].lower()
try:
    temp, ext1 = file1.split(".")
    temp, ext2 = file2.split(".")
except:
    sys.exit("Invalid input")
else:
    if ext1 not in ["jpg", "jpeg", "png"] or ext2 not in ["jpg", "jpeg", "png"]:
        sys.exit("Invalid input")
if ext1 != ext2:
    sys.exit("Input and output have different extensions")

try:
    image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File not found")
shirt = Image.open("shirt.png")
size = shirt.size

image = ImageOps.fit(image=image, size= size)

image.paste(shirt, shirt)

image.save(sys.argv[2])
