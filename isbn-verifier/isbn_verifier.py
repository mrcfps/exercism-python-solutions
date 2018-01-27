def verify(isbn):
    # Remove separating dashes
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    # Calculate with the formula
    sum = 0
    for digit, coef in zip(isbn, range(10, 0, -1)):
        if not digit.isdigit():
            if digit != 'X' or coef != 1:
                return False
            else:
                digit = 10
        sum += int(digit) * coef

    return sum % 11 == 0
