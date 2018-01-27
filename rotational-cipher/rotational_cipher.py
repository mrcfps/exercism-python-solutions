from string import ascii_lowercase, ascii_uppercase


def encrypt(char, key):
    """Encrypt a single character with given rotational key."""
    if char.islower():
        char_idx = ascii_lowercase.index(char)
        value = ascii_lowercase[(char_idx+key) % 26]
    elif char.isupper():
        char_idx = ascii_uppercase.index(char)
        value = ascii_uppercase[(char_idx+key) % 26]
    else:
        # Leave non-letters unchanged
        value = char

    return value


def rotate(text, key):
    return ''.join(encrypt(char, key) for char in text)
