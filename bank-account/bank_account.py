from wrapt import synchronized
from enum import Enum
from functools import wraps


class State(Enum):
    CLOSED = 0
    OPENED = 1


def require_state(state: State):
    def require_state_decorator(func):
        @wraps(func)
        def require_state_func(self, *args, **kwargs):
            if not state == self._state:
                raise ValueError(f"Bank account in state {self._state}, but {state} is required.")
            return func(self, *args, **kwargs)
        return require_state_func
    return require_state_decorator


class BankAccount(object):

    def __init__(self):
        self._state = State.CLOSED
        self._balance = 0

    @require_state(State.OPENED)
    def get_balance(self) -> int:
        return self._balance

    @synchronized
    @require_state(State.CLOSED)
    def open(self):
        self._state = State.OPENED

    @synchronized
    @require_state(State.OPENED)
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Can only deposit a postitive amount.")

        self._balance += amount

    @synchronized
    @require_state(State.OPENED)
    def withdraw(self, amount):
        if not 0 < amount <= self._balance:
            raise ValueError(
                "Can only withdraw a positive amount or an amount less or equal than the current balance.")

        self._balance -= amount

    @synchronized
    @require_state(State.OPENED)
    def close(self):
        self.__init__()
