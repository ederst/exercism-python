from string import ascii_lowercase

def is_pangram(sentence):
    return bool(min(sentence.lower().count(c) for c in ascii_lowercase))
