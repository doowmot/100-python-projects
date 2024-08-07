def display_invoice(name, amount, due_date):
    return f"Hello {name}. Your bill of £{amount:.2f} is due: {due_date}"

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Get user input
name = input("Enter name: ")
amount = get_valid_float("Enter amount: £")
due_date = input("Enter due date: ")

# Generate and display the invoice
invoice = display_invoice(name, amount, due_date)
print("\nInvoice Details:")
print(invoice)

# Optionally, ask if the user wants to save the invoice
save = input("\nDo you want to save this invoice? (yes/no): ").lower()
if save == 'yes':
    with open('invoice.txt', 'w') as file:
        file.write(invoice)
    print("Invoice saved to invoice.txt")
