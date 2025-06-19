x = input("Greeting: ").lower().strip()

if "hello" in x:
    print("$0")
elif x.startswith("h"):
    print("$20")
else:
    print("$100")
