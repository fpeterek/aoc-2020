
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

    print(count_trees(m, 3, 1))
