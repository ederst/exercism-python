import re


class PhoneNumber:

    number: str

    area_code: str
    exchange_code: str
    subscriber_number: str

    def __init__(self, number: str):
        number = re.sub(r"(^[\+]?1|\D+)", "", number)

        if len(number) != 10:
            raise ValueError("Invalid number")

        if int(number[0]) <= 1:
            raise ValueError("Invalid area code")

        if int(number[3]) <= 1:
            raise ValueError("Invalid exchange code")

        self.number = number
        self.area_code = number[:3]
        self.exchange_code = number[3:6]
        self.subscriber_number = number[6:]

    def pretty(self):
        return f"({self.area_code})-{self.exchange_code}-{self.subscriber_number}"
