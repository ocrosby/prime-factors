
from utils.tape import ReadTape, WriteTape


class TestReadTape:
    def test_retract(self):
        input_tape = ReadTape("something")
        assert input_tape.read() == "s"
        assert input_tape.read() == "o"

        input_tape.retract()

        assert input_tape.peek() == "o"

    def test_read(self):
        input_tape = ReadTape("abc")
        assert input_tape.read() == "a"
        assert input_tape.read() == "b"
        assert input_tape.read() == "c"
        assert input_tape.read() == ""

    def test_peek(self):
        input_tape = ReadTape("abc")
        assert input_tape.peek() == "a"
        assert input_tape.peek() == "a"
        assert input_tape.read() == "a"
        assert input_tape.peek() == "b"
        assert input_tape.peek() == "b"
        assert input_tape.read() == "b"
        assert input_tape.peek() == "c"
        assert input_tape.peek() == "c"
        assert input_tape.read() == "c"
        assert input_tape.peek() == ""
        assert input_tape.peek() == ""
        assert input_tape.read() == ""
        assert input_tape.peek() == ""
        assert input_tape.peek() == ""
        assert input_tape.read() == ""

    def test_str(self):
        input_tape = ReadTape("abc")
        assert str(input_tape) == "abc"
        assert input_tape.read() == "a"
        assert str(input_tape) == "bc"
        assert input_tape.read() == "b"
        assert str(input_tape) == "c"
        assert input_tape.read() == "c"
        assert str(input_tape) == ""
        assert input_tape.read() == ""
        assert str(input_tape) == ""

    def test_repr(self):
        input_tape = ReadTape("abc")
        assert repr(input_tape) == "abc"
        assert input_tape.read() == "a"
        assert repr(input_tape) == "bc"
        assert input_tape.read() == "b"
        assert repr(input_tape) == "c"
        assert input_tape.read() == "c"
        assert repr(input_tape) == ""
        assert input_tape.read() == ""
        assert repr(input_tape) == ""


class TestWriteTape:
    def test_write(self):
        otape = WriteTape()
        otape.write("a")
        otape.write("b")
        otape.write("c")
        assert str(otape) == "abc"
        assert repr(otape) == "abc"

    def test_str(self):
        otape = WriteTape()
        otape.write("a")
        otape.write("b")
        otape.write("c")
        assert str(otape) == "abc"
        assert repr(otape) == "abc"

    def test_repr(self):
        otape = WriteTape()
        otape.write("a")
        otape.write("b")
        otape.write("c")
        assert str(otape) == "abc"
        assert repr(otape) == "abc"
