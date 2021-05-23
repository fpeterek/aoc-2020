

with open('in.txt') as f:
    questionnaires = []
    append_new = True

    for line in f:
        stripped = line.strip()
        if not stripped:
            append_new = True
            continue

        if append_new:
            questionnaires.append(set())
            append_new = False
        
        questionnaires[-1].update(stripped)

    res = sum(map(lambda s: len(s), questionnaires))
    print(res)

