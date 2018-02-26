pieces = {
    1: ["first", "and a Partridge in a Pear Tree."],
    2: ["second", "two Turtle Doves"],
    3: ["third", "three French Hens"],
    4: ["fourth", "four Calling Birds"],
    5: ["fifth", "five Gold Rings"],
    6: ["sixth", "six Geese-a-Laying"],
    7: ["seventh", "seven Swans-a-Swimming"],
    8: ["eighth", "eight Maids-a-Milking"],
    9: ["ninth", "nine Ladies Dancing"],
    10: ["tenth", "ten Lords-a-Leaping"],
    11: ["eleventh", "eleven Pipers Piping"],
    12: ["twelfth", "twelve Drummers Drumming"],
}


def verse(key):
    res = "On the {} day of Christmas my true love gave to me".format(pieces[key][0])
    if key == 1:
        res += ", a Partridge in a Pear Tree."
    else:
        for n in range(key, 0, -1):
            res += ", {}".format(pieces[n][1])
    return res


def recite(start_verse, end_verse):
    return [verse(n) for n in range(start_verse, end_verse+1)]
