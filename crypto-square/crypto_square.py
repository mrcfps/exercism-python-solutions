import math
import re


def rec(length):
    """
    Input the length of the original text, return the number of rows
    and columns of the rectangle.
    """
    if length == 0:
        r, c = 0, 0
    else:
        r = round(math.sqrt(length))
        c = round(length / r)
    return r, c


def encode(plain_text):
    # Normalize input
    text = re.sub(r'\W', '', plain_text.lower())

    # Figure out rows and columns of the rectangle
    r, c = rec(len(text))

    # Add spaces to fill the rectangle
    text += (r*c - len(text)) * ' '

    return ' '.join(text[start::c] for start in range(c))
