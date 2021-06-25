import re


def abbreviate(words: str) -> str:
    return "".join(word[0] for word in re.findall(r"[a-zA-Z]+(?:'[a-z])?", words)).upper()
