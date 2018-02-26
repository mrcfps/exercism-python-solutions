many_bottles = [
    "{} bottles of beer on the wall, {} bottles of beer.",
    "Take one down and pass it around, {} bottles of beer on the wall.",
]

two_bottles = [
    "2 bottles of beer on the wall, 2 bottles of beer.",
    "Take one down and pass it around, 1 bottle of beer on the wall.",
]

one_bottle = [
    "1 bottle of beer on the wall, 1 bottle of beer.",
    "Take it down and pass it around, no more bottles of beer on the wall.",
]

no_more_bottles = [
    "No more bottles of beer on the wall, no more bottles of beer.",
    "Go to the store and buy some more, 99 bottles of beer on the wall.",
]


def recite(start, take=1):
    song = []
    for bottle in range(start, start-take, -1):
        if bottle == 0:
            song.extend(no_more_bottles)
        elif bottle == 1:
            song.extend(one_bottle)
        elif bottle == 2:
            song.extend(two_bottles)
        else:
            song.extend([
                many_bottles[0].format(bottle, bottle),
                many_bottles[1].format(bottle-1)
            ])
        song.append("")
    song.pop()
    return song
