from data import storage

# Display Balance
def check_balance():
    print(f"\nCurrent Balance: ₹{storage.balance:.2f}")


# Deposit Money
def deposit():
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount! Must be greater than 0.")
        else:
            storage.balance += amount
            storage.transactions.append(f"Deposited ₹{amount:.2f}")
            print("Deposit successful!")
    except ValueError:
        print("Invalid input! Enter numeric value.")


# Withdraw Money
def withdraw():
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount! Must be greater than 0.")
        elif amount > storage.balance:
            print("Insufficient balance!")
        else:
            storage.balance -= amount
            storage.transactions.append(f"Withdrawn ₹{amount:.2f}")
            print("Withdrawal successful!")
    except ValueError:
        print("Invalid input! Enter numeric value.")


# Statement (Transaction History)
def show_statement():
    print("\n====== TRANSACTION HISTORY ======")
    if not storage.transactions:
        print("No transactions yet.")
    else:
        for i, t in enumerate(storage.transactions, start=1):
            print(f"{i}. {t}")