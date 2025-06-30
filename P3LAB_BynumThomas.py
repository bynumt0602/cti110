# Thomas Bynum
# 06/30/2025
# P3LAB
# Assignment tests student's knowledge of how to write code that displays information to users



amount = float(input("Enter the amount of money as a float: $"))

cents = int(amount * 100)

if cents == 0:
    print("No change")
else:
    dollars = cents // 100
    cents = cents - (dollars * 100)

    quarters = cents // 25
    cents = cents - (quarters * 25)

    dimes = cents // 10
    cents = cents - (dimes * 10)

    nickels = cents // 5
    cents = cents - (nickels * 5)

    pennies = cents

    if dollars == 1:
        print("1 Dollar")
    elif dollars > 1:
        print(f"{dollars} Dollars")

    if quarters == 1:
        print("1 Quarter")
    elif quarters > 1:
        print(f"{quarters} Quarters")

    if dimes == 1:
        print("1 Dime")
    elif dimes > 1:
        print(f"{dimes} Dimes")

    if nickels == 1:
        print("1 Nickel")
    elif nickels > 1:
        print(f"{nickels} Nickels")

    if pennies == 1:
        print("1 Penny")
    elif pennies > 1:
        print(f"{pennies} Pennies")
