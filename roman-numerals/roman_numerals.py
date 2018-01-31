# Map from magnitudes to roman letters
LETTERS = {
    1: ('I', 'V'),
    10: ('X', 'L'),
    100: ('C', 'D'),
    1000: ('M',),
}

def convert(digit, mag):
    """
    Given a digit (0~9) by its magnitude (1, 10, 100, 1000),
    return its roman numeral.
    """
    if digit == 9:
        result = LETTERS[mag][0] + LETTERS[mag*10][0]
    elif 5 <= digit < 9:
        result = LETTERS[mag][1] + LETTERS[mag][0] * (digit - 5)
    elif digit == 4:
        result = LETTERS[mag][0] + LETTERS[mag][1]
    else:  # 0 <= digit < 4
        result = LETTERS[mag][0] * digit
    return result

def numeral(number):
    number = str(number)
    return ''.join(
        convert(int(digit), 10 ** (len(number)-mag-1))
        for mag, digit in enumerate(number))
