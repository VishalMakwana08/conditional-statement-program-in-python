# Hardcoded ATM PIN and initial balance
correct_pin = "1234"
balance = 5000.0  # starting balance

# Ask for PIN
entered_pin = input("Enter your 4-digit PIN: ")

if entered_pin == correct_pin:
    print("\nLogin Successful! Welcome to Python Bank ATM\n")

    while True:
        # ATM Menu
        print("----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"\nYour current balance is: ₹{balance:.2f}\n")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount:.2f} deposited successfully!\n")
            else:
                print("Invalid deposit amount!\n")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount > 0 and amount <= balance:
                balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully!\n")
            elif amount > balance:
                print("Insufficient funds!\n")
            else:
                print("Invalid withdrawal amount!\n")

        elif choice == "4":
            print("Thank you for using Python Bank ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1-4.\n")

else:
    print("Incorrect PIN. Access Denied!")
