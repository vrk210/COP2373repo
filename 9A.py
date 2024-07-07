class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def withdraw(self, amount):
        if amount > self.amount:
            raise ValueError("Insufficient funds")
        self.amount -= amount

    def deposit(self, amount):
        self.amount += amount

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        return self.amount * (self.interest_rate / 100) * (days / 365)

    def __str__(self):
        return f"Account holder: {self.name}\nAccount number: {self.account_number}\nBalance: ${self.amount:.2f}\nInterest rate: {self.interest_rate:.2f}%"

# Test function to test the BankAcct class
def test_bank_acct():
    # Create a bank account
    account = BankAcct("John Doe", "123456789", 1000.0, 3.5)

    # Display account information
    print(account)

    # Adjust interest rate
    account.adjust_interest_rate(4.0)
    print("\nAdjusted Interest Rate:")
    print(account)

    # Deposit money
    account.deposit(500.0)
    print("\nAfter Deposit of $500:")
    print(account)

    # Withdraw money
    try:
        account.withdraw(200.0)
        print("\nAfter Withdrawal of $200:")
        print(account)
    except ValueError as e:
        print(e)

    # Get balance
    balance = account.get_balance()
    print(f"\nCurrent Balance: ${balance:.2f}")

    # Calculate interest for a number of days
    interest = account.calculate_interest(30)
    print(f"\nInterest for 30 days: ${interest:.2f}")

# Run the test function
test_bank_acct()




