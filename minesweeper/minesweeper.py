def analyze_board(input_board):
    """Check if this board is valid. If so, returns height and width.
    Else raises a ValueError.
    """
    if len(set(len(row) for row in input_board)) > 1:
        raise ValueError("Invalid board array")

    if len(input_board) > 0:
        return len(input_board), len(input_board[0])
    else:
        return 0, 0


def count_mines(board, row, col):
    """Count how many mines around the cell specified by row and col."""
    if board[row][col] == '*':
        return '*'

    if board[row][col] != ' ':
        raise ValueError("Invalid char in board")

    height, width = analyze_board(board)

    up_left = 1 if row > 0 and col > 0 and board[row-1][col-1] == '*' else 0
    up = 1 if row > 0 and board[row-1][col] == '*' else 0
    up_right = 1 if row > 0 and col < width-1 and board[row-1][col+1] == '*' else 0
    left = 1 if col > 0 and board[row][col-1] == '*' else 0
    right = 1 if col < width-1 and board[row][col+1] == '*' else 0
    down_left = 1 if row < height-1 and col > 0 and board[row+1][col-1] == '*' else 0
    down = 1 if row < height-1 and board[row+1][col] == '*' else 0
    down_right = 1 if row < height-1 and col < width-1 and board[row+1][col+1] == '*' else 0

    total = up_left + up + up_right + left + right + down_left + down + down_right
    return str(total) if total > 0 else " "


def board(input_board):
    height, width = analyze_board(input_board)
    return [
        ''.join(count_mines(input_board, i, j) for j in range(width))
        for i in range(height)
    ]
