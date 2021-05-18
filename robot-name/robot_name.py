import random
import time
from string import ascii_uppercase, digits

class Robot:
    name: str

    def __init__(self):
        self.reset()

    def reset(self):
        random.seed(time.time())

        _chars = ''.join(random.choices(ascii_uppercase, k=2))
        _digits = ''.join(random.choices(digits, k=3))

        self.name = f'{_chars}{_digits}'
