class Checkbook:
    """
    Function Description:
        A simple checkbook class to handle deposits, withdrawals, and balance inquiry.

    Attributes:
        balance (float): Current balance of the checkbook.
    """

    def __init__(self):
        """Initialize the checkbook with a balance of 0.0"""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
            Adds a given amount to the balance.

        Parameters:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
            Subtracts a given amount from the balance if sufficient funds exist.

        Parameters:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Prints the current balance"""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Function Description:
        Provides a command-line interface for the Checkbook.
        Users can deposit, withdraw, check balance, or exit.

    Parameters:
        None

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
