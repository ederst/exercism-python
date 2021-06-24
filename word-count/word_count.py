from collections import Counter
from string import ascii_lowercase, digits
from typing import Dict
import re


_quotes = '"\''
_exceptions = ascii_lowercase + digits + _quotes


def count_words(sentence: str) -> Dict[str, int]:
    # lowercase the sentence and substitute everything except letters, digits and quotes with a whitespace
    sentence = re.sub(f'[^{_exceptions}]', ' ', sentence.casefold())

    # create a list of words out of the sentence and strip quotes from words (ignoring the contractions)
    words = [word.strip(_quotes) for word in sentence.split()]

    # count the words and return it as dict
    return dict(Counter(words))
