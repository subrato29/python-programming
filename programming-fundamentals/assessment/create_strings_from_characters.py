def create_strings_from_characters(frequencies, string1, string2):
    counter = 0
    if validate_frq_chars(frequencies, string1):
        counter += 1

    if validate_frq_chars(frequencies, string2):
        counter += 1

    return counter


def validate_frq_chars(frequencies, string):
    for ch in set(string):
        if string.count(ch) > frequencies.get(ch, 0):
            return False
        else:
            frequencies[ch] = frequencies.get(ch, 0) - string.count(ch)
    return True
