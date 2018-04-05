bracket_dict = {'(': ')', '[': ']', '{': '}'}


def is_match(left, right):
    return bracket_dict[left] == right


def is_paired(input_string):
    stack = []
    for c in input_string:
        if c in bracket_dict.keys():
            stack.append(c)
        elif c in bracket_dict.values():
            try:
                top = stack.pop()
            except IndexError:  # stack is empty
                return False
            if not is_match(top, c):
                return False

    # Check if there is any unmatched left bracket.
    return len(stack) == 0
