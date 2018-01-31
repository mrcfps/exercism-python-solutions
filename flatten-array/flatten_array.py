def flatten(iterable):
    result = []
    for elem in iterable:
        if isinstance(elem, (list, tuple)):
            result += flatten(elem)
        elif elem or elem == 0:
            result.append(elem)
    return result
