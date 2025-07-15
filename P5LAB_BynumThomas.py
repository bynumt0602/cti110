# Thomas Bynum
# 07/15/2025
# P5LAB
# Use of loops, functions and module import to complete assignments


import random

def disperse_change(change):
    cents = round(change * 100)

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    print()
    print(dollars, "Dollars")
    print(quarters, "Quarters")
    print(dimes, "Dimes")
    print(nickels, "Nickels")
    print(pennies, "Pennies")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print("You owe $" + str(amount_owed))

    cash_input = float(input("How much cash will you put in the self-checkout? "))
  
    change = round(cash_input - amount_owed, 2)

    if change < 0:
        print("That's not enough money. You still owe $" + str(-change))
    else:
        print("Change is: $" + str(change))
        disperse_change(change)
        
main()
