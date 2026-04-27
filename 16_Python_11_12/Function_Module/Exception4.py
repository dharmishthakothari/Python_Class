class InvalidLengthError(Exception):
    pass
try:
    name=input("Enter name ")
    if len(name)<4:
        raise InvalidLengthError("Length must be more then 4 letters ")
    if name.isdigit():
        raise InvalidLengthError("Must contains letters")
except InvalidLengthError as e:
    print(e)