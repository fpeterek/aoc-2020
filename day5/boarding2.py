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


def is_available(seat, occupied):
    return seat-1 in occupied and seat+1 in occupied and seat not in occupied


with open('in.txt') as f:
    lines = f.readlines()
    stripped = map(str.strip, lines)
    non_empty = filter(lambda s: s, stripped)
    boarding_passes = list(non_empty)
    boarding_passes = {bp: seat_id(bp) for bp in boarding_passes}

    occupied = set(boarding_passes.values())

    for i in range(0, 128*8):
        if is_available(i, occupied):
            print(i)
            break

