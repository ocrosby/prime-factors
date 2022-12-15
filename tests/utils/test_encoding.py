from utils import encoding


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
