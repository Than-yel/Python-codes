from datetime import datetime

class Bank_account:
    """
    A real-world simulation of a simple bank account system with PIN protection,
    transaction history, transfers, and account status.
    """

    def __init__(self, account_number, account_name, balance, pin):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
        self.pin = pin
        self.created_on = datetime.now()
        self.is_active = True
        self.transaction_history = []

    def verify_pin(self, pin):
        """
        Verify that the provided PIN matches the account PIN.
        """
        return self.pin == pin

    def deposit(self, amount, pin):
        """
        Deposits money into the account after PIN verification.
        """
        if not self.is_active:
            return {'balance': self.balance, 'message': 'Account is frozen'}

        if not self.verify_pin(pin):
            return {'balance': self.balance, 'message': 'Invalid PIN'}

        if amount <= 0:
            return {'balance': self.balance, 'message': 'Invalid Deposit'}

        self.balance += amount
        self.transaction_history.append({
            'type': 'Deposit',
            'amount': amount,
            'balance': self.balance,
            'timestamp': datetime.now()
        })

        return {'balance': self.balance, 'message': 'Deposit successful'}

    def withdraw(self, amount, pin):
        """
        Withdraws money from the account after verifying PIN and account status.
        """
        if not self.is_active:
            return {'balance': self.balance, 'message': 'Account is frozen'}

        if not self.verify_pin(pin):
            return {'balance': self.balance, 'message': 'Invalid PIN'}

        if amount <= 0:
            return {'balance': self.balance, 'message': 'Invalid Withdrawal'}

        if amount > self.balance:
            return {'balance': self.balance, 'message': 'Insufficient Funds'}

        self.balance -= amount
        self.transaction_history.append({
            'type': 'Withdrawal',
            'amount': amount,
            'balance': self.balance,
            'timestamp': datetime.now()
        })

        return {'balance': self.balance, 'message': 'Withdrawal successful'}

    def transfer(self, amount, recipient_account, pin):
        """
        Transfers money from this account to another, after PIN verification.
        """
        if not self.is_active:
            return {'balance': self.balance, 'message': 'Account is frozen'}

        if not self.verify_pin(pin):
            return {'balance': self.balance, 'message': 'Invalid PIN'}

        if amount <= 0:
            return {'balance': self.balance, 'message': 'Invalid Transfer'}

        if amount > self.balance:
            return {'balance': self.balance, 'message': 'Insufficient Funds'}

        # Proceed with withdrawal and deposit
        self.balance -= amount
        recipient_account.balance += amount

        now = datetime.now()

        self.transaction_history.append({
            'type': 'Transfer Out',
            'to': recipient_account.account_number,
            'amount': amount,
            'balance': self.balance,
            'timestamp': now
        })

        recipient_account.transaction_history.append({
            'type': 'Transfer In',
            'from': self.account_number,
            'amount': amount,
            'balance': recipient_account.balance,
            'timestamp': now
        })

        return {'balance': self.balance, 'message': f'Transferred ₦{amount} to {recipient_account.account_name}'}

    def get_balance(self, pin):
        """
        Returns the current balance after PIN verification.
        """
        if not self.verify_pin(pin):
            return {'message': 'Invalid PIN'}

        return {'balance': self.balance, 'message': "Current account balance"}

    def freeze_account(self):
        """
        Freezes the account (no transactions allowed).
        """
        self.is_active = False
        return {'message': 'Account has been frozen'}

    def unfreeze_account(self):
        """
        Unfreezes the account (transactions allowed).
        """
        self.is_active = True
        return {'message': 'Account has been unfrozen'}

    def print_transaction_history(self):
        """
        Prints all recorded transactions.
        """
        if not self.transaction_history:
            print("No transactions found.")
            return

        for tx in self.transaction_history:
            print(f"{tx['timestamp']}: {tx['type']} - ₦{tx['amount']} | Balance: ₦{tx['balance']}")

# TESTING

# Create two accounts
daniel_account = Bank_account(3100562134, 'Daniel', 10000, pin=2578)
jane_account = Bank_account(3100562135, 'Jane', 5000, pin=6789)

# Deposit
print(daniel_account.deposit(5000, pin=2578))

# Withdraw
print(daniel_account.withdraw(2000, pin=2578))

# Transfer to Person
print(daniel_account.transfer(3000, jane_account, pin=2578))

# Print Daniel’s transaction history
print("\n--- Daniel's Transactions ---")
daniel_account.print_transaction_history()

# Print Jane’s transaction history
print("\n--- Jane's Transactions ---")
jane_account.print_transaction_history()

# Freeze and test
daniel_account.freeze_account()
print(daniel_account.withdraw(1000, pin=2578))  # Should fail due to freeze
