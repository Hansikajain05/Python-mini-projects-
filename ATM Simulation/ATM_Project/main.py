from services import atm_operation


def main_menu():
    while True:
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            atm_operation.check_balance()
        elif choice == '2':
            atm_operation.deposit()
        elif choice == '3':
            atm_operation.withdraw()
        elif choice == '4':
            atm_operation.show_statement()
        elif choice == '5':
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main_menu()