import random
from string import ascii_lowercase

class Cipher(object):
    def __init__(self, key=None):
        self.key = key

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        if key is None:
            self._key = self._generate_random_key()
        else:
            for char in key:
                if char not in ascii_lowercase:
                    raise ValueError("invalid key")
            self._key = key

    def _generate_random_key(self):
        return ''.join(random.choice(ascii_lowercase)
                       for _ in range(100))

    def _convert(self, text_char, key_char, encode=True):
        offset = ascii_lowercase.index(key_char)
        char_idx = ascii_lowercase.index(text_char)
        if encode:
            converted = ascii_lowercase[(char_idx+offset) % 26]
        else:
            converted = ascii_lowercase[(char_idx-offset) % 26]
        return converted

    def encode(self, text):
        text = text.lower()
        return ''.join(
            self._convert(char, self.key[idx % len(self.key)])
            for idx, char in enumerate(text)
            if char in ascii_lowercase)

    def decode(self, text):
        return ''.join(
            self._convert(char, self.key[idx % len(self.key)], encode=False)
            for idx, char in enumerate(text)
            if char in ascii_lowercase)


class Caesar(Cipher):

    def __init__(self):
        Cipher.__init__(self, "dddd")
