from string import ascii_lowercase

# source: https://exercism.io/tracks/python/exercises/pangram/solutions/4b7a98e2e756491c9577debae86ac305

def is_pangram(sentence):
    return set(sentence.lower()) >= set(ascii_lowercase)
