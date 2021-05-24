import re


class PhoneNumber:

    # Note: Use 'private' members and use @property to expose them, to make it as hard as possible [1] to set an
    # unvalidated value from the outside.
    #
    # So this will throw and error:
    #
    # ```python
    # pn = PhoneNumber("1 234 567 8900")
    # pn.area_code = "Oh no!"
    # ```
    #
    # But this will still work:
    #
    # ```python
    # pn = PhoneNumber("1 234 567 8900")
    # pn._PhoneNumber__area_code = "Ha ha!"
    # ```
    #
    # [1]: https://docs.python.org/3/tutorial/classes.html#private-variables
    __area_code: str
    __exchange_code: str
    __subscriber_number: str

    # Inspiration: https://exercism.io/tracks/python/exercises/phone-number/solutions/5d851e650c05492e8bcfbe80e7ddc308
    __pattern = re.compile(r"""
        ^1?             # (optional) country code
        ([2-9]\d{2})    # area code
        ([2-9]\d{2})    # exchange code
        (\d{4})$        # subscriber number
    """, re.VERBOSE)

    def __init__(self, number: str):
        # Cleanup number to make for easier parsing
        number = re.sub(r"\D+", "", number)

        try:
            self.__area_code, self.__exchange_code, self.__subscriber_number = self.__pattern.search(number).groups()
        except AttributeError:
            raise ValueError("Provided an invalid number")

    @property
    def area_code(self):
        return self.__area_code

    @property
    def exchange_code(self):
        return self.__exchange_code

    @property
    def subscriber_number(self):
        return self.__subscriber_number

    @property
    def number(self):
        return f"{self.area_code}{self.exchange_code}{self.subscriber_number}"

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
