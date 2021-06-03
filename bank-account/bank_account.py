from wrapt import synchronized


class State(object):

    def get_balance(self, account) -> int:
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def open(self):
        raise NotImplementedError

    def deposit(self, account, amount):
        raise NotImplementedError

    def withdraw(self, account, amount):
        raise NotImplementedError


class Opened(State):

    def get_balance(self, account) -> int:
        return account._balance

    def close(self) -> State:
        return Closed()

    def open(self):
        raise ValueError("Account is open.")

    def deposit(self, account, amount):
        if amount <= 0:
            raise ValueError("Invalid amount.")

        account._balance += amount

    def withdraw(self, account, amount):
        if not 0 < amount <= account._balance:
            raise ValueError("invalid amount.")

        account._balance -= amount


class Closed(State):

    def _raise_error(self):
        raise ValueError("Account is closed.")

    def get_balance(self, account):
        self._raise_error()

    def close(self) -> State:
        self._raise_error()

    def open(self) -> State:
        return Opened()

    def deposit(self, account, amount):
        self._raise_error()

    def withdraw(self, account, amount):
        self._raise_error()


class BankAccount(object):

    def __init__(self):
        self._state = Closed()
        self._balance = 0

    def get_balance(self) -> int:
        return self._state.get_balance(self)

    def open(self):
        self._state = self._state.open()

    @synchronized
    def deposit(self, amount):
        self._state.deposit(self, amount)

    @synchronized
    def withdraw(self, amount):
        self._state.withdraw(self, amount)

    def close(self):
        self._state = self._state.close()
        self._balance = 0
