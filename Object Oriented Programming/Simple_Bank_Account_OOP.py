class Bank_account:
    """
    A class to simulate a simple bank account.

    Attributes:
    -----------
    account_number : int
        The unique account number assigned to the customer.
    account_name : str
        The name of the account holder.
    balance : float
        The current balance in the account.

    Methods:
    --------
    deposit(amount):
        Adds a valid amount to the account balance.
    withdraw(amount):
        Deducts a valid amount from the account balance if sufficient funds exist.
    get_balance():
        Returns the current balance of the account.
    """

    def __init__(self, account_number, account_name, balance):
        """
        Initializes a new bank account with account number, name, and balance.
        """
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits a positive amount into the account.

        Parameters:
        -----------
        amount : float
            The amount to be deposited.

        Returns:
        --------
        dict: A message with updated balance or an error message.
        """
        if amount <= 0:
            return {'balance': self.balance, 'message': 'Invalid Deposit'}
        self.balance += amount
        return {'balance': self.balance, 'message': 'Deposit successful'}

    def withdraw(self, amount):
        """
        Withdraws a positive amount from the account if funds are sufficient.

        Parameters:
        -----------
        amount : float
            The amount to be withdrawn.

        Returns:
        --------
        dict: A message with updated balance or an error message.
        """
        if amount <= 0:
            return {'balance': self.balance, "message": 'Invalid Withdrawal'}
        if amount > self.balance:
            return {'balance': self.balance, 'message': 'Insufficient Funds'}
        self.balance -= amount
        return {'balance': self.balance, 'message': 'Withdrawal Successful'}

    def get_balance(self):
        """
        Returns the current account balance.

        Returns:
        --------
        dict: A message with the current balance.
        """
        return {'balance': self.balance, 'message': "Current account balance"}


# Create a bank account instance for user "Daniel"
my_bank = Bank_account(3100562134, 'Daniel', 10000)

# Deposit 10,000 into the account
print(my_bank.deposit(10000))

# Withdraw 5,000 from the account
print(my_bank.withdraw(5000))
