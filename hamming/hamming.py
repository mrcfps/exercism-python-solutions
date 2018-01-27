def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Input strands don't have equal length.")

    counter = 0
    for nuc_a, nuc_b in zip(strand_a, strand_b):
        if nuc_a != nuc_b:
            counter += 1
    return counter
