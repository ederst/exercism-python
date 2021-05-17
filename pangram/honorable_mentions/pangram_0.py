from string import ascii_lowercase

def is_pangram(sentence):
    lower_sentence = sentence.lower()

    for c in range(ord('a'), ord('z')+1):
        if lower_sentence.count(chr(c)) == 0:
            return False

    return True
