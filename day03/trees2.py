
def count_trees(m, dx, dy):
    x = 0
    y = 0
    trees = 0

    while y < len(m):
        trees += m[y][x] == '#'
        x += dx
        x %= len(m[y])
        y += dy

    return trees


with open('in.txt') as f:
    lines = f.readlines()
    stripped = map(lambda s: s.strip(), lines)
    non_empty = filter(lambda s: s, stripped)

    m = list(non_empty)

    deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    counts = list(map(lambda pair: count_trees(m, dx=pair[0], dy=pair[1]), deltas))

    res = 1
    for c in counts:
        res *= c

    print(res)
    
