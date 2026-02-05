#year=int(input("Enter year "))
for year in range(1990,2026):
    if year%4==0 and year%100!=0 or year%400==0:
        print(f"{year} Year is leap year")
    # else:
    #     print(f"{year} Year is not leap year")