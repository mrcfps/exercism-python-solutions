def fence_pattern(message_size, rails):
    """Return a matrix filled with '.' and '?', where '?'
    means a character and '.' means empty cell."""
    pattern = [['.']*message_size for _ in range(rails)]
    row, col = 0, 0
    down = True
    while col < message_size:
        pattern[row][col] = '?'
        col += 1
        row = row + 1 if down else row - 1
        if row == 0:
            down = True
        if row == rails - 1:
            down = False
    return pattern


def encode(message, rails):
    pattern = fence_pattern(len(message), rails)

    # Fill in the pattern with message, column by column
    idx = 0
    for col in range(len(message)):
        for row in range(rails):
            if pattern[row][col] == '?':
                pattern[row][col] = message[idx]
                idx += 1

    encoded = ''.join(
        ''.join(cell for cell in row if cell != '.')
        for row in pattern
    )
    return encoded


def decode(encoded_message, rails):
    pattern = fence_pattern(len(encoded_message), rails)

    # Fill in the pattern with encoded message, row by row
    idx = 0
    for row in range(rails):
        for col in range(len(encoded_message)):
            if pattern[row][col] == '?':
                pattern[row][col] = encoded_message[idx]
                idx += 1

    decoded = ''.join(
        ''.join(cell for cell in col if cell != '.')
        for col in zip(*pattern)
    )
    return decoded
