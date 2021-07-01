from typing import List


def load_file(filename: str) -> tuple[int, List[int]]:
    with open(filename) as f:
        timestamp = int(f.readline())
        buses = f.readline().split(',')
        buses = [int(bus) for bus in buses if bus and bus != 'x']
        return timestamp, buses


def wait_time(bus: int, ts: int) -> int:
    return bus - (ts % bus)


def find_bus(buses: List[int], ts: int) -> tuple[int, int]:
    bus = min(buses, key=lambda bus: wait_time(bus, ts))
    wait = wait_time(bus, ts)
    return bus, wait


def run():
    ts, buses = load_file('in.txt')
    bus, wait = find_bus(buses, ts)
    print(bus * wait)


if __name__ == '__main__':
    run()

