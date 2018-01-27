allergies = {
    1: "eggs",
    2: "peanuts",
    4: "shellfish",
    8: "strawberries",
    16: "tomatoes",
    32: "chocolate",
    64: "pollen",
    128: "cats",
}

class Allergies(object):

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        return [item for i, item in allergies.items() if self.score & i]
