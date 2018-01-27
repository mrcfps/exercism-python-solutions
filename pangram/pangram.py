import string


def is_pangram(sentence):
    lowered_sentence = sentence.lower()
    for letter in string.ascii_lowercase:
        if letter not in lowered_sentence:
            return False
    return True
