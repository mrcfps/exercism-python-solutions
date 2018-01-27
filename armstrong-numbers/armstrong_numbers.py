def is_armstrong(number):
    return number == sum(int(digit) ** len(str(number)) for digit in str(number))
