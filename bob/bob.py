import re


def is_question(phrase):
    """Returns whether a phrase is a question."""
    return phrase.strip().endswith('?')


def is_yelling(phrase):
    """Returns whether a phrase is a yelling sentence."""
    return phrase.isupper()


def is_saying_nothing(phrase):
    """Returns whether a phrase is not saying anything."""
    return re.match(r'^\s*$', phrase)


def hey(phrase):
    if is_question(phrase) and is_yelling(phrase):
        reply = "Calm down, I know what I'm doing!"
    elif is_question(phrase):
        reply = "Sure."
    elif is_yelling(phrase):
        reply = "Whoa, chill out!"
    elif is_saying_nothing(phrase):
        reply = "Fine. Be that way!"
    else:
        reply = "Whatever."

    return reply
