import math


def aliquot_sum(number):
    if number == 1:
        return 0
    factors = [1]
    sqrt = math.sqrt(number)
    for n in range(2, math.ceil(sqrt)):
        if number % n == 0:
            factors.append(n)
            factors.append(number / n)
    if int(sqrt) == sqrt:
        factors.append(sqrt)
    return sum(factors)


def classify(number):
    if number <= 0:
        raise ValueError("natural numbers required")
    if aliquot_sum(number) == number:
        return "perfect"
    elif aliquot_sum(number) > number:
        return "abundant"
    else:
        return "deficient"
