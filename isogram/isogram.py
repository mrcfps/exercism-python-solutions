def is_isogram(string):
    # Remove spaces and hyphens and lower it
    processed = string.replace('-', '').replace(' ', '').lower()

    return len(set(processed)) == len(processed)
