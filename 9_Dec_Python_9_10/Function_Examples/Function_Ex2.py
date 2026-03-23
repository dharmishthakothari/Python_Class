#function to calculate Simple interest
def findSI(principle_amount,rate,no_of_years):
    interest=principle_amount*rate*no_of_years/100
    return interest

for _ in range(5):
    p_amount=int(input("Enter amount "))
    rate=int(input("Enter rate "))
    years=int(input("Enter years "))
    ans=findSI(p_amount,rate,years)
    print(ans)
    # if ans>=500:
    #     print(p_amount,rate,years,ans)

