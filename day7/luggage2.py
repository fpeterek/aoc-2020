from typing import Dict
from functools import cache


class Bag:
    def __init__(self, color: str, carries: Dict[str, int]):
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

    def __get__(self, color):
        return self.carries[color]


def parse_line(line: str) -> Bag:
    split = line.split()
    color = f'{split[0]} {split[1]}'
    carries = dict()

    if (split[4], split[5]) != ('no', 'other'):
        i = 5
        while i+1 < len(split):
            carries[(f'{split[i]} {split[i+1]}')] = int(split[i-1])
            i += 4

    return Bag(color, carries)


def load_bags(filename: str) -> Dict[str, Bag]:
    with open(filename) as f:
        bags = [parse_line(line.strip()) for line in f if line and not line.isspace()]
        return {b.color: b for b in bags}


bags = load_bags('in.txt')


@cache
def dfs(bag):
    return sum(map(lambda tpl: tpl[1] * (1 + dfs(bags[tpl[0]])), bag.carries.items()))


print(dfs(bags['shiny gold']))

