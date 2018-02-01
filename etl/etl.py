def transform(legacy_data):
    new_data = {
        letter.lower(): point
        for point, letters in legacy_data.items()
        for letter in letters
    }

    return new_data
