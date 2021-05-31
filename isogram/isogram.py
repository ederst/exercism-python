import re


def is_isogram(string: str) -> bool:
    string = re.sub(r"\W", "", string).lower()

    return len(set(string)) == len(string)
