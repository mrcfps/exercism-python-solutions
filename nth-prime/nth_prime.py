import math
from itertools import count


def is_prime(number):
    for i in range(2, math.floor(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def nth_prime(n):
    if n <= 0:
        raise ValueError("n must be positive")
    counter = 1
    for number in count(2):
        if is_prime(number):
            if counter < n:
                counter += 1
            else:
                return number
