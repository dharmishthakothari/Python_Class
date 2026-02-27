import random
gen_number=random.randint(1,100)
while True:
    guess_nu=int(input("Enter number "))
    if gen_number<guess_nu:
        print("Please enter lesser number ")
    elif gen_number>guess_nu:
        print("Please enter greater number ")
    elif gen_number==guess_nu:
        print("You Win")
        break