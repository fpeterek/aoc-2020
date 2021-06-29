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


class Ship:
    def __init__(self, direction: Direction, position: Position):
        self.dir = direction
        self.pos = position

    def move(self, direction: Direction, distance: int) -> None:
        dx = math.cos(math.radians(direction.value)) * distance
        dy = math.sin(math.radians(direction.value)) * distance
        self.pos += (dx, dy)

    def apply(self, ins: Instruction) -> None:
        if ins.type == InstructionType.Forward:
            self.move(self.dir, ins.value)
        elif ins.type == InstructionType.Move:
            self.move(ins.dir, ins.value)
        elif ins.type == InstructionType.Turn:
            self.dir += ins.value


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
    ship = Ship(Direction.Right, Position(x=0, y=0))
    for ins in instructions:
        ship.apply(ins)
    lx, ly = ship.pos.tuple
    print(int(abs(lx) + abs(ly)))


if __name__ == '__main__':
    run()

