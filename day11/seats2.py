from typing import List
from enum import Enum


class Seat(Enum):
    Floor = 0
    Empty = 1
    Occupied = 2

    @staticmethod
    def from_str(s: str):
        if s  == '.':
            return Seat.Floor
        if s == 'L':
            return Seat.Empty
        if s == '#':
            return Seat.Occupied


SeatMap = List[List[Seat]]


def load(filename: str) -> SeatMap:
    with open(filename) as f:
        lines = [s.strip() for s in f.readlines() if s and not s.isspace()]
        return [[Seat.from_str(char) for char in line] for line in lines]


def is_occupied(seats: SeatMap, x: int, y: int) -> bool:
    width, height = len(seats[0]), len(seats)
    if not (0 <= x < width and 0 <= y < height):
        return False
    return seats[y][x] == Seat.Occupied


def get_adjacent_seat(seats: SeatMap, x: int, y: int, dx: int, dy: int) -> tuple[int, int]:
    width, height = len(seats[0]), len(seats)
    cx, cy = x+dx, y+dy

    while 0 <= cx < width and 0 <= cy < height and seats[cy][cx] == Seat.Floor:
        cx, cy = cx+dx, cy+dy

    return cx, cy


def count_occupied_adjacent(seats: SeatMap, x: int, y: int) -> int:
    occupied = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == j == 0):
                adj_x, adj_y = get_adjacent_seat(seats, x=x, y=y, dx=i, dy=j)
                occupied += is_occupied(seats, adj_x, adj_y)
    return occupied


def run_iteration(seats: SeatMap) -> tuple[SeatMap, int]:
    copy: SeatMap = [line[:] for line in seats]
    changes = 0

    for y in range(len(seats)):
        for x in range(len(seats[0])):
            if seats[y][x] == Seat.Floor:
                continue
            adj = count_occupied_adjacent(seats, x, y)
            if adj == 0 and copy[y][x] == Seat.Empty:
                copy[y][x] = Seat.Occupied
                changes += 1
            elif adj >= 5 and copy[y][x] == Seat.Occupied:
                copy[y][x] = Seat.Empty
                changes += 1

    return copy, changes


def count_occupied(seats: SeatMap) -> int:
    return sum(map(lambda row: sum(map(lambda seat: seat == Seat.Occupied, row)), seats))


def run_simulation(seats: SeatMap) -> int:
    changes = 1
    while changes:
        seats, changes = run_iteration(seats)
    return count_occupied(seats)


def run():
    seats = load('in.txt')
    print(run_simulation(seats))

if __name__ == '__main__':
    run()

