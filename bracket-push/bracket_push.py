def is_match(left, right):
    if left == '[' and right == ']':
        return True
    elif left == '{' and right == '}':
        return True
    elif left == '(' and right == ')':
        return True
    else:
        return False


def is_paired(input_string):
    stack = []
    for c in input_string:
        if c in ['[', '{', '(']:
            stack.append(c)
        elif c in [']', '}', ')']:
            if len(stack) == 0:
                return False
            elif is_match(stack[-1], c):
                stack.pop()
            else:
                return False

    # Check if there is any unmatched left bracket.
    if len(stack) != 0:
        return False
    else:
        return True
