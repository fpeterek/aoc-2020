
def validate(line):
    split = line.split(':')
    left, psswd = split[0].strip(), split[1].strip()

    split = left.split()
    bounds, letter = split[0].strip(), split[1].strip()

    split = bounds.split('-')
    lower, upper = int(split[0]), int(split[1])

    return len(list(filter(lambda c: c == letter, psswd))) in range(lower, upper+1)
    

with open('in.txt') as f:
    lines = f.readlines()
    stripped = map(lambda s: s.strip(), lines)
    non_empty = filter(lambda s: s, stripped)

    valid = sum(map(validate, non_empty))
    print(valid)

