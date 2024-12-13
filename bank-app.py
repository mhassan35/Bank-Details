class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        return f"Your current balance is: ${self.balance:.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount:.2f} deposited successfully. {self.check_balance()}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance!"
        if amount <= 0:
            return "Invalid withdrawal amount!"
        self.balance -= amount
        return f"${amount:.2f} withdrawn successfully. {self.check_balance()}"

def main():
    print("Welcome to the Bank App")
    account_number = input("Enter your account number: ")
    account = BankAccount(account_number, balance=500) 

    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            print(account.check_balance())
        elif choice == "2":
            amount = float(input("Enter the amount to deposit: "))
            print(account.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: "))
            print(account.withdraw(amount))
        elif choice == "4":
            print("Thank you for using the Bank App. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
