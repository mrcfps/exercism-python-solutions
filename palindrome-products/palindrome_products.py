def is_palindrome(number):
    num = str(number)
    return num == num[::-1]


def largest_palindrome(max_factor, min_factor):
    if max_factor < min_factor:
        raise ValueError(
            "max factor should be larger than or equal to min factor")
    value = 0
    factors = set()

    for x in range(max_factor, min_factor-1, -1):
        for y in range(x, min_factor-1, -1):
            if is_palindrome(x * y):
                if x * y > value:
                    value = x * y
                    factors.clear()
                    factors.add((y, x))
                elif x * y == value:
                    factors.add((y, x))

    if len(factors) == 0:
        raise ValueError("no palindrome products found")

    return value, factors


def smallest_palindrome(max_factor, min_factor):
    if max_factor < min_factor:
        raise ValueError(
            "max factor should be larger than or equal to min factor")
    value = float('inf')
    factors = set()

    for x in range(min_factor, max_factor+1):
        for y in range(x, max_factor+1):
            if is_palindrome(x * y):
                if x * y < value:
                    value = x * y
                    factors.clear()
                    factors.add((x, y))
                elif x * y == value:
                    factors.add((x, y))

    if len(factors) == 0:
        raise ValueError("no palindrome products found")

    return value, factors
