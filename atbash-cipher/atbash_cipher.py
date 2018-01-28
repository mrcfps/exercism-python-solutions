from string import ascii_lowercase


def convert(char):
    """Encode or decode a single character."""
    if char.isnumeric():
        converted = char
    else:
        idx = ascii_lowercase.index(char.lower())
        converted = ascii_lowercase[-idx-1]
    return converted

def group_cipher(cipher):
    """Transform cipher into groups of five letters."""
    return ' '.join(cipher[i:i+5] for i in range(0, len(cipher), 5))

def encode(plain_text):
    encoded = [convert(char) for char in plain_text if char.isalnum()]
    return group_cipher(''.join(encoded))

def decode(ciphered_text):
    decoded = [convert(char) for char in ciphered_text if char.isalnum()]
    return ''.join(decoded)
