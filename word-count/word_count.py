import re
from collections import Counter

def word_count(phrase):
    # Split the phrase into words
    words = [
        word.strip(".':?!&@$%^&").lower()
        for word in re.split(r'[\s,_]+', phrase)
        if re.match(r'^[^\w]*$', word) is None  # remove non-words
    ]
    return Counter(words)
