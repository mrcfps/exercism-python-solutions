import math
import re


def rec(length):
    """
    Input the length of the original text, return the number of rows
    and columns of the rectangle.
    """
    base = math.floor(math.sqrt(length))
    if base * base == length:
        r, c = base, base
    elif base * base < length <= base * (base+1):
        r, c = base, base+1
    else:
        r, c = base+1, base+1
    return r, c


def encode(plain_text):
    # Normalize input
    text = re.sub(r'\W', '', plain_text.lower())

    # Figure out rows and columns of the rectangle
    r, c = rec(len(text))

    # Add spaces to fill the rectangle
    text += (r*c - len(text)) * ' '

    return ' '.join(text[start::c] for start in range(c))
