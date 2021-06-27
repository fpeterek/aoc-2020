from typing import List, Dict


def load_adapters(filename: str) -> List[int]:
    with open(filename) as f:
        return sorted(list(map(lambda s: int(s), filter(lambda s: s and not s.isspace(), f.readlines()))))


def count_diffs(adapters: List[int]) -> Dict[int, int]:
    res = dict()
    for i in range(len(adapters) - 1):
        diff = adapters[i+1] - adapters[i]
        res[diff] = res.get(diff, 0) + 1
    return res


if __name__ == '__main__':
    adapters = load_adapters('in.txt')
    adapters.insert(0, 0)
    adapters.append(adapters[-1] + 3)
    diffs = count_diffs(adapters)
    print(diffs.get(3, 0) * diffs.get(1, 0))

