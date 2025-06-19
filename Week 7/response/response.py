from validator_collection import validators, errors

email = input("What's your email address? ")

try:
    validators.email(email)
    print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
