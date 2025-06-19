from datetime import date
import sys
import inflect

def main():
    e = inflect.engine()
    text = input("Date of Birth: ")
    try:
        year, month, day = text.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
    except ValueError:
        sys.exit("Invalid Date")
    date1 = date(year, month, day)
    date2 = date.today()
    time = date2 - date1
    days = time.days
    print(f"{e.number_to_words(get_mins(days)).capitalize().replace("and ", "")} minutes")



def get_mins(days):
    return days*24*60

if __name__ == "__main__":
    main()
