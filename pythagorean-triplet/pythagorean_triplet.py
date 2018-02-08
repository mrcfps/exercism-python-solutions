import math
from itertools import combinations


def _is_coprime(a, b):
    """Given two numbers a and b, return whether they are coprime."""
    for n in range(2, min(a, b) + 1):
        if a % n == 0 and b % n == 0:
            return False
    return True


def _is_both_odd(a, b):
    """Given two numbers a and b return whether they are both odd numbers."""
    return a % 2 != 0 and b % 2 != 0


def primitive_triplets(number):
    if number % 4 != 0:
        raise ValueError("invalid input")

    results = set()

    # Formula reference:
    # https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
    mn = int(number / 2)
    for n in range(1, int(math.sqrt(mn))+1):
        m, remainder = divmod(mn, n)
        if remainder == 0 and _is_coprime(m, n) and not _is_both_odd(m, n):
            results.add(tuple(sorted([m**2 - n**2, 2*m*n, m**2 + n**2])))
    return results


def triplets_in_range(range_start, range_end):
    results = set()
    for comb in combinations(range(range_start, range_end+1), 3):
        if is_triplet(comb):
            results.add(comb)
    return results


def is_triplet(triplet):
    triplet = sorted(triplet)
    return triplet[0]**2 + triplet[1]**2 == triplet[2]**2
