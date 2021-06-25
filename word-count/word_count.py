from collections import Counter
from typing import Dict
import re


def count_words(sentence: str) -> Dict[str, int]:
    # this exact solution was suggestec by the mentor (bobahop)
    return Counter(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", sentence.lower()))
