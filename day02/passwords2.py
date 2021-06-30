
def validate(line):
    split = line.split(':')
    left, psswd = split[0].strip(), split[1].strip()

    split = left.split()
    bounds, letter = split[0].strip(), split[1].strip()

    split = bounds.split('-')
    lower, upper = int(split[0]) - 1, int(split[1]) - 1

    return (0 <= lower < len(psswd) and psswd[lower] == letter) ^ (upper < len(psswd) and psswd[upper] == letter)
    

with open('in.txt') as f:
    lines = f.readlines()
    stripped = map(lambda s: s.strip(), lines)
    non_empty = filter(lambda s: s, stripped)

    valid = sum(map(validate, non_empty))
    print(valid)

