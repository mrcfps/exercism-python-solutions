zero_to_nineteen = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

ty = [
    "twenty", "thirty", "forty", "fifty",
    "sixty", "seventy", "eighty", "ninety",
]

magnitudes = ["thousand", "million", "billion"]


def hundred_converter(number):
    """Convert a number from 0 to 99 to English."""
    if 0 <= number < 20:
        english = zero_to_nineteen[number]
    else:
        tens = number // 10
        units = number % 10
        if units:
            english = ty[tens-2] + '-' + zero_to_nineteen[units]
        else:
            english = ty[tens-2]
    return english


def thousand_converter(number):
    """Convert a number from 0 to 999 to English."""
    if 0 <= number < 100:
        english = hundred_converter(number)
    else:
        hundreds = number // 100
        remainder = number % 100
        if remainder:
            english = ''.join([
                zero_to_nineteen[hundreds],
                " hundred and ",
                hundred_converter(remainder),
            ])
        else:
            english = zero_to_nineteen[hundreds] + " hundred"
    return english


def split_to_chunks(number):
    """Convert number to list of chunks, e.g. 12345 to [345, 12]."""
    digits = list(reversed(str(number)))
    chunks = []
    for stride in range(0, len(digits), 3):
        three_digits = digits[stride:stride+3]
        chunks.append(int(''.join(three_digits[::-1])))
    return chunks


def large_number_converter(number):
    """Convert number over 1000 to English."""
    chunks = split_to_chunks(number)

    if len(chunks) > len(magnitudes) + 1:
        raise ValueError("number too large")

    english = []
    if 0 < chunks[0] < 100:
        english.insert(0, "and " + hundred_converter(chunks[0]))
    elif 100 <= chunks[0] < 1000:
        english.insert(0, thousand_converter(chunks[0]))

    for chunk, mag in zip(chunks[1:], magnitudes):
        if chunk:
            english.insert(0, thousand_converter(chunk) + ' ' + mag)

    return ' '.join(english)


def say(number):
    """Say a number out in English."""
    number = int(number)
    if number < 0:
        raise ValueError("input number is negative")
    elif 0 <= number < 1000:
        english = thousand_converter(number)
    else:
        english = large_number_converter(number)
    return english
