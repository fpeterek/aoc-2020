from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, List


class InstructionType(Enum):
    NOP = 0
    ACC = 1
    JMP = 2


@dataclass
class Instruction:
    ins_type: InstructionType
    arg: int
    call_count: int = 0


@dataclass
class State:
    loop: bool
    state: int

    @property
    def terminated(self) -> bool:
        return not self.loop


class Interpreter:
    def __init__(self):
        self.acc = 0
        self.i = 0

    def interpret(self, instruction: Instruction) -> None:
        if instruction.ins_type == InstructionType.NOP:
            self.i += 1
        elif instruction.ins_type == InstructionType.ACC:
            self.acc += instruction.arg
            self.i += 1
        elif instruction.ins_type == InstructionType.JMP:
            self.i += instruction.arg
        else:
            raise ValueError(f'Unknown instruction {instruction.ins_type}')

    def run(self, code: List[Instruction]) -> int:
        loop = False
        while self.i < len(code):
            if code[self.i].call_count >= 1:
                loop = True
                break
            curr = code[self.i]
            self.interpret(curr)
            curr.call_count += 1

        return State(loop, self.acc)


class Optimizer:
    def __init__(self, code: List[Instruction]):
        self.code = code
        self.fixable: List[int] = list()
        for idx, ins in enumerate(code):
            if (ins.ins_type == InstructionType.NOP and ins.arg) or ins.ins_type == InstructionType.JMP:
                self.fixable.append(idx)

    def next(self) -> List[Instruction]:
        copy = [Instruction(ins.ins_type, ins.arg) for ins in self.code]
        old = copy[self.fixable[0]]
        new_type = InstructionType.NOP if old.ins_type == InstructionType.JMP else InstructionType.JMP
        new = Instruction(new_type, old.arg)
        copy[self.fixable[0]] = new
        self.fixable.pop(0)
        return copy


def parse_line(line: str) -> Instruction:
    split = line.split(' ')
    ins_type = InstructionType[split[0].upper()]
    value = (-1, 1)[split[1][0] == '+'] * int(split[1][1:])
    return Instruction(ins_type, value)


def load_file(filename: str) -> List[Instruction]:
    with open(filename) as f:
        return list(map(lambda l: parse_line(l.strip()), filter(lambda l: l and not l.isspace(), f.readlines())))


if __name__ == '__main__':
    instructions = load_file('in.txt')
    optimizer = Optimizer(instructions)
    while True:
        interpreter = Interpreter()
        code = optimizer.next()
        retval = interpreter.run(code)
        if retval.terminated:
            print(retval.state)
            break

