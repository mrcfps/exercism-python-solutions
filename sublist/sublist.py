SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(4)


def check_lists(first_list, second_list):
    if first_list == second_list:
        return EQUAL

    # Convert lists to comma-separated strings
    first = ','.join(str(c) for c in first_list)
    second = ','.join(str(c) for c in second_list)

    if first in second:
        return SUBLIST
    elif second in first:
        return SUPERLIST
    else:
        return UNEQUAL
