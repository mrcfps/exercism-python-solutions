def is_anagram(word, candidate):
    word = word.lower()
    candidate = candidate.lower()
    if word != candidate and sorted(candidate) == sorted(word):
        return True
    else:
        return False


def detect_anagrams(word, candidates):
    correct_list = []
    for candidate in candidates:
        if is_anagram(word, candidate):
            correct_list.append(candidate)
    return correct_list
