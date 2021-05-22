

with open('in.txt') as f:
    passports = []
    append_new = True

    for line in f:
        stripped = line.strip()
        if not stripped:
            append_new = True
            continue

        if append_new:
            passports.append(dict())
            append_new = False
        
        pairs = stripped.split()
        for pair in pairs:
            split = pair.split(':')
            k, v = split[0], split[1]
            passports[-1][k] = v

    res = sum(map(lambda pp: len(pp) == 8 or (len(pp) == 7 and 'cid' not in pp), passports))
    print(res)

