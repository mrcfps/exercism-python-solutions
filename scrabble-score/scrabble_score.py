scrabble = {
    'AEIOULNRST': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10,
}

def value(letter):
    for key, value in scrabble.items():
        if letter.upper() in key:
            return value
    return 0

def score(word):
    return sum(value(letter) for letter in word)
