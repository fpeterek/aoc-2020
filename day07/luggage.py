from typing import List, Set


class Bag:
    def __init__(self, color: str, carries: Set[str]):
        self.color = color
        self.carries = carries

    def __str__(self):
        return f'{self.color}: {self.carries}'

    def __hash__(self):
        return hash(self.color)

    def __contains__(self, color: str) -> bool:
        return color in self.carries

    def __eq__(self, other):
        return self.color == other.color


def parse_line(line: str) -> Bag:
    split = line.split()
    color = f'{split[0]} {split[1]}'
    carries = set()

    if (split[4], split[5]) != ('no', 'other'):
        i = 5
        while i+1 < len(split):
            carries.add(f'{split[i]} {split[i+1]}')
            i += 4

    return Bag(color, carries)


def load_bags(filename: str) -> List[Bag]:
    with open(filename) as f:
        return [parse_line(line.strip()) for line in f if line and not line.isspace()]


bags = load_bags('in.txt')

additions = set(filter(lambda bag: 'shiny gold' in bag, bags))
result = set()

while additions:
    new = set()
    for b in additions:
        new.update(set(filter(lambda bag: b.color in bag and bag not in result, bags)))

    result.update(additions)
    additions = new

print(len(result))

