import re
from itertools import groupby


def decode(string):
    decoded = []

    while string:
        # Find out the first non-numeric symbol
        first_char_idx = re.search(r'[a-zA-Z\s]', string).start()
        first_char = string[first_char_idx]

        # How many times the char has repeated
        repeat = int(string[:first_char_idx]) if string[:first_char_idx] else 1

        decoded.append(repeat * first_char)

        # Strip processed characters off the string
        string = string[first_char_idx + 1:]

    return ''.join(decoded)

def encode(string):
    encoded = []

    for c, group in groupby(string):
        # Number of times the letter c has repeated
        repeat = len(list(group))

        if repeat > 1:
            encoded.append(str(repeat) + c)
        else:
            encoded.append(c)

    return ''.join(encoded)
