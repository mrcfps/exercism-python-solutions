class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')

    def _double(self, digit):
        """Double a digit according to Luhn Algorithm."""
        return digit*2 if digit*2 < 10 else digit*2 - 9

    def is_valid(self):
        """Decide whether a card_num is valid."""
        # Strings of length 1 or less are not valid
        if len(self.card_num) <= 1:
            return False

        # Convert card_num to a list of ints and reverse it
        try:
            seq = [int(digit) for digit in reversed(self.card_num)]
        except ValueError:  # Non-digit character detected
            return False

        luhn_sum = sum(map(self._double, seq[1::2])) + sum(seq[::2])
        return luhn_sum % 10 == 0
