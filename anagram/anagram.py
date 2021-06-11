def find_anagrams(word, candidates):
    caseless_word = word.casefold()
    sorted_caseless_word = sorted(caseless_word)

    return [c for c in candidates if not caseless_word == c.casefold() and sorted(c.casefold()) == sorted_caseless_word]
