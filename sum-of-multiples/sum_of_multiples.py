def sum_of_multiples(limit, multiples):
    selected_nums = []
    for multiple in multiples:
        selected_nums.extend(range(multiple, limit, multiple))
    return sum(set(selected_nums))
