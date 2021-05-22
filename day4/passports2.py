def validate_in_range(string, lower, upper):
    return string.isdigit() and lower <= int(string) <= upper


def validate_by(passport):
    return validate_in_range(passport.get('byr', ''), 1920, 2002)


def validate_iy(passport):
    return validate_in_range(passport.get('iyr', ''), 2010, 2020)


def validate_ey(passport):
    return validate_in_range(passport.get('eyr', ''), 2020, 2030)


def validate_ht(passport):
    hgt = passport.get('hgt', '')
    
    if len(hgt) < 3:
        return False

    unit = hgt[-2:]
    val = hgt[:-2]
    
    if not val.isdigit():
        return False

    if unit == 'cm':
        return 150 <= int(val) <= 193
    if unit == 'in':
        return 59 <= int(val) <= 76
    return False


def validate_hc(passport):
    hcl = passport.get('hcl', '')

    if len(hcl) != 7 or hcl[0] != '#':
        return False

    return all(map(lambda c: c.isdigit() or 'a' <= c <= 'f', hcl[1:]))


eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def validate_ec(passport):
    return passport.get('ecl', '') in eye_colors


def validate_pi(passport):
    pid = passport.get('pid', '')
    return len(pid) == 9 and pid.isdigit()


def validate_ci(passport):
    return True


validators = [validate_by, validate_iy, validate_ey, validate_ht, validate_hc, validate_ec,
              validate_pi, validate_ci]


def validate_passport(passport):
    return all(map(lambda fn: fn(passport), validators))


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

    res = sum(map(validate_passport, passports))
    print(res)

