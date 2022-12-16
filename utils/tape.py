
class ReadTape:
    def __init__(self, data: str):
        self.data = data
        self.index = 0

    def eof(self) -> bool:
        return self.index >= len(self.data)

    def retract(self, n: int = 1):
        self.index -= n

    def read(self) -> str:
        if self.eof():
            return ""

        self.index += 1
        return self.data[self.index - 1]

    def peek(self) -> str:
        if self.eof():
            return ""

        return self.data[self.index]

    def __str__(self):
        return self.data[self.index:]

    def __repr__(self):
        return self.data[self.index:]


class WriteTape:
    def __init__(self):
        super().__init__()
        self.data = ""

    def write(self, data: str):
        self.data += data

    def __str__(self):
        return self.data

    def __repr__(self):
        return self.data
