with open("File1.txt","r") as file:
    file.seek(10)
    print(f"Current position {file.tell()}")
    print(f"Data are {file.readline()}")
    print(f"After reading single line Current position {file.tell()}")
    print(f"Data are {file.readline()}")
    print(f"After reading another line Current position {file.tell()}")
