try:
    no=int(input("Enter number "))
    print("You have enterd ",no)
    print(12/0)
    print("End of Try")
# except:
#     print("in except block")
# except ValueError as e:
#     print("in value error ",e)
# except ZeroDivisionError as e:
#     print("Divide by zero error ",e)
except (ValueError,ZeroDivisionError) as e:
    print(e)