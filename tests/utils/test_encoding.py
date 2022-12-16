import pytest

from utils import encoding
from collections import deque
from utils.tape import ReadTape


class TestEncode:
    def test_0(self):
        assert encoding.encode(0) == "."

    def test_1(self):
        assert encoding.encode(1) == "()"

    def test_2(self):
        assert encoding.encode(2) == "(())"

    def test_3(self):
        assert encoding.encode(3) == "(.())"

    def test_4(self):
        assert encoding.encode(4) == "((()))"

    def test_5(self):
        assert encoding.encode(5) == "(..())"

    def test_6(self):
        assert encoding.encode(6) == "(()())"

    def test_7(self):
        assert encoding.encode(7) == "(...())"

    def test_8(self):
        assert encoding.encode(8) == "((.()))"

    def test_9(self):
        assert encoding.encode(9) == "(.(()))"

    def test_10(self):
        assert encoding.encode(10) == "(().())"

    def test_11(self):
        assert encoding.encode(11) == "(....())"


class TestDecodeExponents:

    def test_2(self):
        assert encoding.decode_exponents("(())") == deque([1])

    def test_3(self):
        assert encoding.decode_exponents("(.())") == deque([0, 1])

    def test_4(self):
        assert encoding.decode_exponents("((()))") == deque([2])

    def test_5(self):
        assert encoding.decode_exponents("(..())") == deque([0, 0, 1])

    def test_6(self):
        assert encoding.decode_exponents("(()())") == deque([1, 1])

    def test_7(self):
        assert encoding.decode_exponents("(...())") == deque([0, 0, 0, 1])

    @pytest.mark.skip(reason="Still not working")
    def test_8(self):
        assert encoding.decode_exponents("((.()))") == deque([3])

    def test_9(self):
        assert encoding.decode_exponents("(.(()))") == deque([0, 2])

    def test_10(self):
        assert encoding.decode_exponents("(().())") == deque([1, 0, 1])

    def test_11(self):
        assert encoding.decode_exponents("(....())") == deque([0, 0, 0, 0, 1])

    def test_12(self):
        assert encoding.decode_exponents("((())())") == deque([2, 1])


class TestNextExponent:
    def test_0(self):
        itape = ReadTape(".")
        assert encoding.next_exponent(itape) is None

    def test_1(self):
        itape = ReadTape("()")
        assert encoding.next_exponent(itape) == 1

    def test_2(self):
        itape = ReadTape("(())")
        assert encoding.next_exponent(itape) == 2


class TestExperiment:
    def test_0(self):
        assert encoding.experiment(".") == []

    def test_1(self):
        assert encoding.experiment("()") == [(2,0)]

    def test_2(self):
        assert encoding.experiment("(())") == [(2,1)]

    @pytest.mark.skip(reason="Still not working")
    def test_3(self):
        assert encoding.experiment("(.())") == [(2,0),(3,1)]

    def test_4(self):
        assert encoding.experiment("((()))") == [(2,2)]

    @pytest.mark.skip(reason="Still not working")
    def test_5(self):
        assert encoding.experiment("(..())") == [(2,0),(3,0),(5,1)]

    @pytest.mark.skip(reason="Still not working")
    def test_6(self):
        assert encoding.experiment("(()())") == [(2,1),(3,1)]

    @pytest.mark.skip(reason="Still not working")
    def test_7(self):
        assert encoding.experiment("(...())") == [(2,0),(3,0),(5,0),(7,1)]

    @pytest.mark.skip(reason="Still not working")
    def test_8(self):
        assert encoding.experiment("((.()))") == [(2,3)]

    @pytest.mark.skip(reason="Still not working")
    def test_9(self):
        assert encoding.experiment("(.(()))") == [(2,0),(3,2)]

    @pytest.mark.skip(reason="Still not working")
    def test_10(self):
        assert encoding.experiment("(().())") == [(2,1),(3,0),(5,1)]

    @pytest.mark.skip(reason="Still not working")
    def test_11(self):
        assert encoding.experiment("(....())") == [(2,0),(3,0),(5,0),(7,0),(11,1)]

    @pytest.mark.skip(reason="Still not working")
    def test_12(self):
        assert encoding.experiment("((())())") == [(2,2),(3,1)]


class TestDecode:
    def test_empty(self):
        with pytest.raises(ValueError, match="Unable to decode empty string!"):
            encoding.decode("")

    def test_0(self):
        assert encoding.decode(".") == 0

    def test_1(self):
        assert encoding.decode("()") == 1

    def test_2(self):
        assert encoding.decode("(())") == 2

    def test_3(self):
        assert encoding.decode("(.())") == 3

    def test_4(self):
        assert encoding.decode("((()))") == 4

    def test_5(self):
        assert encoding.decode("(..())") == 5

    def test_6(self):
        assert encoding.decode("(()())") == 6

    def test_7(self):
        assert encoding.decode("(...())") == 7

    @pytest.mark.skip(reason="Still not working")
    def test_8(self):
        assert encoding.decode("((.()))") == 8

    def test_9(self):
        assert encoding.decode("(.(()))") == 9

    def test_10(self):
        assert encoding.decode("(().())") == 10

    def test_11(self):
        assert encoding.decode("(....())") == 11


class TestTuringMachine:
    def test_init_empty_data(self):
        machine = encoding.TuringMachine("")

        assert machine.state == 0
        assert machine.itape.data == ""

    def test_step_0_lparen(self):
        # Arrange
        machine = encoding.TuringMachine("()")

        # Act
        assert machine.step()

        # Assert
        assert machine.state == 1
        assert machine.otape.data == "("

    def test_step_0_dot(self):
        # Arrange
        machine = encoding.TuringMachine(".")

        # Act
        assert machine.step()

        # Assert
        assert machine.state == 2
        assert machine.otape.data == "."

    def test_step_0_rparen(self):
        # Arrange
        machine = encoding.TuringMachine(")")

        # Act
        assert machine.step()

        # Assert
        assert machine.state == 3
        assert machine.otape.data == ")"


