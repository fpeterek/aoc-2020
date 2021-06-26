from typing import List


class FileProcessor:

    preamble_size = 25

    def __init__(self):
        self.preamble = []

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

    def process_file(self, filename: str) -> int:
        with open(filename) as f:
            for line in f:
                if not line or line.isspace():
                    continue
                value = int(line)
                
                if self.preamble_full and not self.is_valid(value):
                    return value

                self.add(value)


if __name__ == '__main__':
    print(FileProcessor().process_file('in.txt'))

