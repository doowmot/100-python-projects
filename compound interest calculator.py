
while True:
    amount_invested = float(input("Enter the amount to invest (£): "))
    if amount_invested <=0:
        print("The amount invested cannot be less than 0.")
    else:https://www.geeksforgeeks.org/how-to-replace-values-in-a-list-in-python/
        break

while True:
    interest_rate = float(input("Enter the interest rate (%): "))
    if interest_rate <=0:
        print("The interest rate cannot be less than 0.")
    else:
        break

while True:
    time_in_years = int(input("Enter how long you'll be investing for (years): "))
    if time_in_years <=0:
        print("The time cannot be less than 0.")
    else:
        break

total = amount_invested * pow((1 + interest_rate / 100), time_in_years)
print(f"Your total after {time_in_years} year(s), will be: £{total:.2f}")