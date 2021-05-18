from string import ascii_lowercase

# best solution imho, source:
# * https://exercism.io/tracks/python/exercises/pangram/solutions/66c0c33fd2774c6d9d032b16fae5034d

def is_pangram(string):
    return set(ascii_lowercase).issubset(string.lower())
