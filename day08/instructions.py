from enum import Enum
from dataclasses import dataclass
from typing import List


class InstructionType(Enum):
    NOP = 0
    ACC = 1
    JMP = 2


@dataclass
class Instruction:
    ins_type: InstructionType
    arg: int
    call_count: int = 0


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
        while code[self.i].call_count < 1:
            curr = code[self.i]
            self.interpret(curr)
            curr.call_count += 1

        return self.acc


def parse_line(line: str) -> Instruction:
    split = line.split(' ')
    ins_type = InstructionType[split[0].upper()]
    value = (-1, 1)[split[1][0] == '+'] * int(split[1][1:])
    return Instruction(ins_type, value)


def load_file(filename: str) -> List[Instruction]:
    with open(filename) as f:
        return list(map(lambda l: parse_line(l.strip()), filter(lambda l: l and not l.isspace(), f.readlines())))


if __name__ == '__main__':
    interpreter = Interpreter()
    instructions = load_file('in.txt')
    retval = interpreter.run(instructions)
    print(retval)

