class Group:
    def __init__(self):
        self.dct = dict()
        self.persons = 0

    def add(self, answers):
        for c in answers:
            self.dct[c] = self.dct.get(c, 0) + 1
        self.persons += 1

    @property
    def common_answers(self):
        return sum(map(lambda count: count == self.persons, self.dct.values()))


with open('in.txt') as f:
    questionnaires = []
    append_new = True

    for line in f:
        stripped = line.strip()
        if not stripped:
            append_new = True
            continue

        if append_new:
            questionnaires.append(Group())
            append_new = False
        
        questionnaires[-1].add(stripped)

    res = sum(map(lambda group: group.common_answers, questionnaires))
    print(res)

