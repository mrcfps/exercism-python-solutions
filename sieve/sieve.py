def sieve(limit):
    numbers = list(range(1, limit+1))
    for num in numbers:
        if num not in (0, 1):
            # Assign zeros to multiples of this prime
            numbers[2*num-1::num] = [0] * len(numbers[2*num-1::num])
    return [number for number in numbers if number not in (0, 1)]
