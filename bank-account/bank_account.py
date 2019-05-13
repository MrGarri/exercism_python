from threading import Lock


class BankAccount(object):

    lock = Lock()

    def __init__(self):
        self.is_open = False
        self.balance = 0

    def get_balance(self):
        if not self.is_open:
            raise ValueError("Cannot perform operations over a closed account")

        return self.balance

    def open(self):
        if self.is_open:
            raise ValueError("Cannot open an already opened account")

        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError("Cannot perform operations over a closed account")
        if amount < 0:
            raise ValueError("Amount to deposit must be a positive value")

        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError("Cannot perform operations over a closed account")
        if amount < 0:
            raise ValueError("Amount to withdraw must be a positive value")

        with self.lock:
            if amount > self.balance:
                raise ValueError("Amount to withdraw must be less than current balance")

            self.balance -= amount

    def close(self):
        if not self.is_open:
            raise ValueError("Cannot close an already closed account")

        self.is_open = False
        self.balance = 0
