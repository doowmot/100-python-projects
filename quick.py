def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

def main():
    while True:
        principal = get_positive_float("Enter the amount to invest (£): ")
        annual_rate = get_positive_float("Enter the annual interest rate (%): ")
        years = get_positive_int("Enter the investment duration (years): ")

        total = calculate_compound_interest(principal, annual_rate, years)
        
        print(f"\nInvestment Summary:")
        print(f"Principal  Amount: £{principal:.2f}")
        print(f"Annual Interest Rate: {annual_rate:.2f}%")
        print(f"Investment Duration: {years} years")
        print(f"Total after {years} year(s): £{total:.2f}")
        print(f"Total Interest Earned: £{total - principal:.2f}")

        again = input("\nWould you like to make another calculation? (yes/no): ").lower()
        if again != 'yes':
            break

    print("Thank you for using the compound interest calculator!")

if __name__ == "__main__":
    main()
