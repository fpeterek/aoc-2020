from typing import List, Dict
from functools import cache


def load_adapters(filename: str) -> List[int]:
    with open(filename) as f:
        return sorted(list(map(lambda s: int(s), filter(lambda s: s and not s.isspace(), f.readlines()))))


@cache
def count_arrangements(index: int) -> int:
    if index == len(adapters) - 1:
        return 1

    arrangements = 0
    i = index + 1
    while i < len(adapters) and adapters[i] - adapters[index] <= 3:
        arrangements += count_arrangements(i)
        i += 1

    return arrangements


if __name__ == '__main__':
    adapters = load_adapters('in.txt')
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    print(count_arrangements(0))

