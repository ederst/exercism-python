from string import ascii_lowercase

def is_pangram(sentence):
    return bool(min(map(sentence.lower().count, ascii_lowercase)))
