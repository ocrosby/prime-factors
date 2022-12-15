
from utils.tape import ReadTape, WriteTape

class TestReadTape:
    def test_read(self):
        itape = ReadTape("abc")
        assert itape.read() == "a"
        assert itape.read() == "b"
        assert itape.read() == "c"
        assert itape.read() == ""

    def test_peek(self):
        itape = ReadTape("abc")
        assert itape.peek() == "a"
        assert itape.peek() == "a"
        assert itape.read() == "a"
        assert itape.peek() == "b"
        assert itape.peek() == "b"
        assert itape.read() == "b"
        assert itape.peek() == "c"
        assert itape.peek() == "c"
        assert itape.read() == "c"
        assert itape.peek() == ""
        assert itape.peek() == ""
        assert itape.read() == ""
        assert itape.peek() == ""
        assert itape.peek() == ""
        assert itape.read() == ""

    def test_str(self):
        itape = ReadTape("abc")
        assert str(itape) == "abc"
        assert itape.read() == "a"
        assert str(itape) == "bc"
        assert itape.read() == "b"
        assert str(itape) == "c"
        assert itape.read() == "c"
        assert str(itape) == ""
        assert itape.read() == ""
        assert str(itape) == ""

    def test_repr(self):
        itape = ReadTape("abc")
        assert repr(itape) == "abc"
        assert itape.read() == "a"
        assert repr(itape) == "bc"
        assert itape.read() == "b"
        assert repr(itape) == "c"
        assert itape.read() == "c"
        assert repr(itape) == ""
        assert itape.read() == ""
        assert repr(itape) == ""


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
