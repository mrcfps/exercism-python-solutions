import math

ALLERGIES = [
    'eggs', 'peanuts', 'shellfish', 'strawberries',
    'tomatoes', 'chocolate', 'pollen', 'cats',
]


class Allergies(object):

    def __init__(self, score):
        self.score = score
        self.allergies = []

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        if self.score == 0:
            return self.allergies

        # 2^power <= score < 2^(power+1)
        power = math.floor(math.log2(self.score))

        # Get a copy of score to avert side effect
        remain = self.score

        while remain > 0 and power >= 0:
            if remain >= 2**power:
                if power < len(ALLERGIES):
                    self.allergies.append(ALLERGIES[power])
                remain -= 2**power
            power -= 1

        return self.allergies
