def to_rna(dna_strand):
    trans_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    try:
        return ''.join(trans_dict[c] for c in dna_strand)
    except KeyError:
        raise ValueError("Invalid DNA strand input.")
