from threading import Lock


class BankAccount:

    def _reset(self):
        self._opened = False
        self._balance = 0
        self._lock = Lock()

    def __init__(self):
        self._reset()

    def get_balance(self):
        with self._lock:
            if not self._opened:
                raise ValueError("Account is closed.")

            return self._balance

    def open(self):
        if self._opened:
            raise ValueError("Account is already opened.")

        self._opened = True

    def deposit(self, amount):
        with self._lock:
            if not self._opened:
                raise ValueError("Account is closed.")

            if amount < 0:
                raise ValueError("Amount cannot be negative.")

            self._balance += amount

    def withdraw(self, amount):
        with self._lock:
            if not self._opened:
                raise ValueError("Account is closed.")

            if amount < 0:
                raise ValueError("Amount cannot be negative.")

            if amount > self._balance:
                raise ValueError("Cannot withdraw more than deposited.")

            self._balance -= amount

    def close(self):
        if not self._opened:
            raise ValueError("Account is already closed.")
        self._reset()
