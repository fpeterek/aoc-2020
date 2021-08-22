
class Bus:
    def __init__(self, number: int, offset: int, begin: int = 0):
        self.number = number
        self.offset = offset
        self.begin = begin


def load_file(filename: str) -> tuple[int, list[int]]:
    with open(filename) as f:
        timestamp = int(f.readline())
        buses = f.readline().split(',')
        return [Bus(int(bus), offset) for offset, bus in enumerate(buses) if bus and bus != 'x']


def lcm(x: int, y: int, begin: int = 0, offset: int = 0) -> int:
    delta = x
    multiply = begin if begin else delta
    while (multiply < offset) or ((multiply + offset) % y):
        multiply += delta
    return multiply 


def find(b1: Bus, b2: Bus) -> Bus:
    period = lcm(b1.number, b2.number)
    t1 = lcm(x=b1.number, y=b2.number, begin=b1.begin, offset=b2.offset)
    return Bus(number=period, offset=0, begin=t1)


def run() -> None:
    buses = load_file('in.txt')
    while len(buses) > 1:
        b1, b2 = buses.pop(0), buses.pop(0)
        buses.insert(0, find(b1, b2))
    print(buses[0].begin)


if __name__ == '__main__':
    run()

