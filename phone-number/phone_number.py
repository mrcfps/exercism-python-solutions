import re


class Phone(object):
    def __init__(self, phone_number):
        self._number_tuple = self._transform(phone_number)

    def _transform(self, phone_number):
        m = re.match(
            r'\+?1?\W*\(?([2-9]\d{2})\)?[-. ]*([2-9]\d{2})[-. ]*(\d{4})$',
            phone_number.strip()
        )

        # No matched, so it's invalid.
        if m is None:
            raise ValueError("Invalid phone number")

        return m.groups()

    @property
    def number(self):
        return ''.join(self._number_tuple)

    @property
    def area_code(self):
        return self._number_tuple[0]

    def pretty(self):
        return '({}) {}-{}'.format(*self._number_tuple)
