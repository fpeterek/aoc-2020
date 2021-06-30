import math


def bs(string, lower, upper):
    for c in string:
        if c == 'F' or c == 'L':
            upper -= math.ceil((upper-lower)/2)
        else:
            lower += math.ceil((upper-lower)/2)
    return lower


def seat_id(bp):
    row = bs(string=bp[0:7], lower=0, upper=127)
    seat = bs(string=bp[7:], lower=0, upper=7)

    return row * 8 + seat


with open('in.txt') as f:
    lines = f.readlines()
    stripped = map(str.strip, lines)
    non_empty = filter(lambda s: s, stripped)
    boarding_passes = list(non_empty)
    boarding_passes = {bp: seat_id(bp) for bp in boarding_passes}

    print(max(boarding_passes.values()))

