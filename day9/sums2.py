from typing import List


class FileProcessor:

    preamble_size = 25

    def __init__(self):
        self.preamble: List[int] = []
        self.all: List[int] = []
        self.invalid = None
        self.disallowed: List[int] = []

    @property
    def preamble_full(self) -> bool:
        return len(self.preamble) == FileProcessor.preamble_size

    def is_valid(self, num: int) -> bool:
        for i in range(FileProcessor.preamble_size):
            for j in range(i+1, FileProcessor.preamble_size):
                if self.preamble[i] + self.preamble[j] == num:
                    return True
        return False

    def add(self, value: int) -> None:
        if self.preamble_full:
            self.preamble.pop(0)

        self.preamble.append(value)
        self.all.append(value)

    def find(self, candidates: List[int], desired_value: int) -> List[int]:
        for i in range(len(candidates)):
            total = candidates[i]
            j = i+1
            while total < desired_value:
                total += candidates[j]
                j += 1
            if total == desired_value:
                return candidates[i:j]

    def break_code(self) -> int:
        candidates = list(filter(lambda x: x < self.invalid, self.all))
        values = self.find(candidates, self.invalid)
        return min(values) + max(values)

    def process_file(self, filename: str) -> int:
        with open(filename) as f:
            for line in f:
                if not line or line.isspace():
                    continue
                value = int(line)
                
                if self.preamble_full and not self.is_valid(value):
                    self.invalid = value

                self.add(value)

        return self.break_code()


if __name__ == '__main__':
    print(FileProcessor().process_file('in.txt'))

