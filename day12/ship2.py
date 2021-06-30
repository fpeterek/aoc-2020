from enum import Enum
from dataclasses import dataclass
from typing import List
import math


@dataclass
class Position:
    x: int
    y: int

    def __add__(self, vec: tuple[int, int]):
        dx, dy = vec
        return Position(self.x + dx, self.y + dy)

    @property
    def tuple(self) -> tuple[int, int]:
        return self.x, self.y


class Direction(Enum):
    Right = 0
    Left = 180
    Up = 90
    Down = 270

    def __add__(self, degrees: int):
        return Direction((self.value + degrees) % 360)

    @staticmethod
    def from_str(s: str):
        if s == 'N':
            return Direction.Up
        if s == 'E':
            return Direction.Right
        if s == 'S': 
            return Direction.Down
        if s == 'W':
            return Direction.Left


class InstructionType(Enum):
    Move = 0
    Forward = 1
    Turn = 2

    @staticmethod
    def from_str(s: str):
        if s in ('N', 'E', 'S', 'W'):
            return InstructionType.Move
        if s == 'F':
            return InstructionType.Forward
        if s in ('R', 'L'):
            return InstructionType.Turn


class Instruction:
    def __init__(self, ins_type: InstructionType, direction: Direction = None, value: int = None):
        self.type = ins_type
        self.dir = direction
        self.value = value


class Waypoint:
    def __init__(self, position: Position):
        self.pos = position

    def move(self, ins: Instruction) -> None:
        dx, dy = 0, 0

        if ins.dir == Direction.Right:
            dx = ins.value
        elif ins.dir == Direction.Left:
            dx = -ins.value
        elif ins.dir == Direction.Up:
            dy = ins.value
        elif ins.dir == Direction.Down:
            dy = -ins.value

        self.pos += (dx, dy)

    @property
    def distance(self) -> float:
        return (self.pos.x**2 + self.pos.y**2) ** 0.5

    def turn(self, deg: int) -> None:
        dist = self.distance
        if not dist:
            return
        cos = self.pos.x / dist
        angle = math.acos(cos)
        angle = angle if self.pos.y >= 0 else (math.pi*2)-angle
        angle += math.radians(deg)
        nx, ny = round(math.cos(angle) * dist), round(math.sin(angle) * dist)
        self.pos.x, self.pos.y = nx, ny

    def apply(self, ins: Instruction) -> None:
        if ins.type == InstructionType.Move:
            return self.move(ins)
        if ins.type == InstructionType.Turn:
            return self.turn(ins.value)


class Ship:
    def __init__(self, waypoint: Waypoint, position: Position):
        self.wp = waypoint
        self.pos = position

    def move(self, distance: int) -> None:
        self.pos += (self.wp.pos.x * distance, self.wp.pos.y * distance)

    def apply(self, ins: Instruction) -> None:
        self.wp.apply(ins)
        if ins.type == InstructionType.Forward:
            self.move(ins.value)


def parse_instruction(s: str) -> Instruction:
    ins = s[0]
    val = int(s[1:])
    tp = InstructionType.from_str(ins)
    if ins == 'R':
        val *= -1
    direction = Direction.from_str(ins) if tp == InstructionType.Move else None
    return Instruction(ins_type=tp, direction=direction, value=val)


def load_file(filename: str) -> List[Instruction]:
    with open(filename) as f:
        return [parse_instruction(line.strip()) for line in f if line and not line.isspace()]


def run():
    instructions = load_file('in.txt')
    ship = Ship(Waypoint(Position(x=10, y=1)), Position(x=0, y=0))
    for ins in instructions:
        ship.apply(ins)
    lx, ly = ship.pos.tuple
    print(int(abs(lx) + abs(ly)))


if __name__ == '__main__':
    run()

