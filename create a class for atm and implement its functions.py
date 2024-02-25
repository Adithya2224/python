import random

class Account:
    def __init__(self, id, checking_balance=0, savings_balance=0, annual_interest_rate_savings=3.4):
        self.id = id
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        self.annual_interest_rate_savings = annual_interest_rate_savings

    def get_id(self):
        return self.id

    def checking_account_balance(self):
        return self.checking_balance

    def withdraw_checking_account(self, amount):
        self.checking_balance -= amount

    def deposit_checking_account(self, amount):
        self.checking_balance += amount

    def transfer_checking_account(self, amount):
        self.checking_balance += amount
        self.savings_balance -= amount

    def savings_account_balance(self):
        return self.savings_balance

    def withdraw_savings_account(self, amount):
        self.savings_balance -= amount

    def deposit_savings_account(self, amount):
        self.savings_balance += amount

    def transfer_savings_account(self, amount):
        self.savings_balance += amount
        self.checking_balance -= amount

    def savings_account_monthly_interest(self):
        return self.savings_balance * (self.annual_interest_rate_savings / 12)

    def savings_account_annual_interest_rate(self):
        return self.annual_interest_rate_savings

    def savings_account_monthly_interest_rate(self):
        return self.annual_interest_rate_savings / 12

def main():
    # Creating accounts
    accounts = [Account(i, 0) for i in range(1000, 9999)]

    while True:
        # Reading id from user
        print("Welcome to International Bank.")
        id = int(input("\nEnter 4-digit account pin: "))
        
        # Loop till id is valid
        while id < 1000 or id > 9999:
            id = int(input("\nInvalid Id.. Re-enter: "))

        # Iterating over interface
        while True:
            # Printing menu
            print("\nHow can we help you today?")
            print("""\n1 - View Checking Balance \t\t2 - Withdraw Checking 
3 - Deposit Checking \t\t\t4 - Transfer Checking
5 - View Savings Balance \t\t6 - Withdraw Savings 
7 - Deposit Savings \t\t\t8 - Transfer Savings
9 - Exit """)

            # Reading selection
            selection = int(input("\nEnter your numerical selection: "))

            # Getting account object
            accountObj = next((acc for acc in accounts if acc.get_id() == id), None)

            if not accountObj:
                print("\nAccount not found.")
                break

            # View Checking Balance
            if selection == 1:
                # Printing balance
                print(f"\nChecking account balance: ${accountObj.checking_account_balance():.2f}")
                
            # Checking Withdraw
            elif selection == 2:
                # Reading amount
                amt = float(input("\nEnter amount to withdraw from checking: "))
                ver_checking_withdraw = input(f"Is ${amt:.2f} the correct amount to withdraw, Yes or No ? ").upper()
                
                if ver_checking_withdraw == "YES":
                    print("\nVerified checking account withdraw.")
                else:
                    break

                if amt < accountObj.checking_account_balance():
                    # Calling withdraw method
                    accountObj.withdraw_checking_account(amt)
                    # Printing updated balance
                    print(f"Updated checking account balance: ${accountObj.checking_account_balance():.2f}")
                else:
                    print(f"\nYour checking account balance is less than withdrawal amount: ${accountObj.checking_account_balance():.2f}")

            # Deposit
            elif selection == 3:
                # Reading amount
                amt = float(input("\nEnter amount to deposit in checking: "))
                ver_checking_deposit = input(f"Is ${amt:.2f} the correct amount to deposit, Yes or No ? ").upper()
                
                if ver_checking_deposit == "YES":
                    # Calling deposit method
                    print("\nVerified checking account deposit.")
                    accountObj.deposit_checking_account(amt)
                    # Printing updated balance
                    print(f"\nUpdated checking account balance: ${accountObj.checking_account_balance():.2f}")
                else:
                    break

            # (Rest of the code remains the same)

# Main function
if __name__ == "__main__":
    main()
