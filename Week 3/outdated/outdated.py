months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    date = input("Date: ").strip()

    if date[0].isdigit(): # first case: month/day/year
        try:
            month, day, year = date.split("/")
        except ValueError: # if couldn't split this way then reprompt
            pass
        else: # if worked
            if int(day) <= 31 and int(month) <= 12: # if not it will reprompt
                print(f"{int(year):04}-{int(month):02}-{int(day):02}")
                break

    elif date[0].isalpha(): # second case: month day, year
        try:
            month, temp = date.split(" ", maxsplit=1) # split into month and (day, year) as temp
            day, year = temp.split(", ") # split temp
        except ValueError: # if couldn't split this way go again in the loop
            pass
        else: # if worked
            month = months.index(month) + 1
            if int(day) <= 31: # if not it will reprompt
                # didn't check month <= 12 bc it's already taken from the index
                print(f"{int(year):04}-{month:02}-{int(day):02}")
                break

# reprompt means go again in the loop without breaking
# breaks only if printed the formated date
