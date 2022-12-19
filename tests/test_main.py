from main import sieve_of_atkin
from main import encode
from main import sieve_of_eratosthenes


class TestEncode:
    def test_0(self):
        assert encode(0) == "."

    def test_1(self):
        assert encode(1) == "()"

    def test_2(self):
        assert encode(2) == "(())"

    def test_3(self):
        assert encode(3) == "(.())"

    def test_4(self):
        assert encode(4) == "((()))"

    def test_5(self):
        assert encode(5) == "(..())"

    def test_6(self):
        assert encode(6) == "(()())"

    def test_7(self):
        assert encode(7) == "(...())"

    def test_8(self):
        assert encode(8) == "((.()))"

    def test_9(self):
        assert encode(9) == "(.(()))"

    def test_10(self):
        assert encode(10) == "(().())"

    def test_11(self):
        assert encode(11) == "(....())"


class TestSieveOfAtkin:
    def test_0(self):
        assert sieve_of_atkin(0) == []

    def test_1(self):
        assert sieve_of_atkin(1) == []

    def test_2(self):
        assert sieve_of_atkin(2) == [2]

    def test_3(self):
        assert sieve_of_atkin(3) == [2, 3]

    def test_4(self):
        assert sieve_of_atkin(4) == [2, 3]

    def test_5(self):
        assert sieve_of_atkin(5) == [2, 3, 5]

    def test_6(self):
        assert sieve_of_atkin(6) == [2, 3, 5]

    def test_7(self):
        assert sieve_of_atkin(7) == [2, 3, 5, 7]

    def test_8(self):
        assert sieve_of_atkin(8) == [2, 3, 5, 7]

    def test_9(self):
        assert sieve_of_atkin(9) == [2, 3, 5, 7]

    def test_10(self):
        assert sieve_of_atkin(10) == [2, 3, 5, 7]

    def test_11(self):
        assert sieve_of_atkin(11) == [2, 3, 5, 7, 11]

    def test_12(self):
        assert sieve_of_atkin(12) == [2, 3, 5, 7, 11]

    def test_13(self):
        assert sieve_of_atkin(13) == [2, 3, 5, 7, 11, 13]

    def test_14(self):
        assert sieve_of_atkin(14) == [2, 3, 5, 7, 11, 13]

    def test_15(self):
        assert sieve_of_atkin(15) == [2, 3, 5, 7, 11, 13]

    def test_16(self):
        assert sieve_of_atkin(16) == [2, 3, 5, 7, 11, 13]

    def test_30(self):
        assert sieve_of_atkin(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    def test_equivalence_1000000(self):
        assert sieve_of_atkin(1000000) == sieve_of_eratosthenes(1000000)


class TestSieveOfEratosthenes:
    def test_0(self):
        assert sieve_of_eratosthenes(0) == []

    def test_1(self):
        assert sieve_of_eratosthenes(1) == []

    def test_2(self):
        assert sieve_of_eratosthenes(2) == [2]

    def test_3(self):
        assert sieve_of_eratosthenes(3) == [2, 3]

    def test_4(self):
        assert sieve_of_eratosthenes(4) == [2, 3]

    def test_5(self):
        assert sieve_of_eratosthenes(5) == [2, 3, 5]

    def test_6(self):
        assert sieve_of_eratosthenes(6) == [2, 3, 5]

    def test_7(self):
        assert sieve_of_eratosthenes(7) == [2, 3, 5, 7]

    def test_8(self):
        assert sieve_of_eratosthenes(8) == [2, 3, 5, 7]

    def test_9(self):
        assert sieve_of_eratosthenes(9) == [2, 3, 5, 7]

    def test_10(self):
        assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]

    def test_11(self):
        assert sieve_of_eratosthenes(11) == [2, 3, 5, 7, 11]

    def test_12(self):
        assert sieve_of_eratosthenes(12) == [2, 3, 5, 7, 11]

    def test_13(self):
        assert sieve_of_eratosthenes(13) == [2, 3, 5, 7, 11, 13]

    def test_14(self):
        assert sieve_of_eratosthenes(14) == [2, 3, 5, 7, 11, 13]

    def test_15(self):
        assert sieve_of_eratosthenes(15) == [2, 3, 5, 7, 11, 13]

    def test_16(self):
        assert sieve_of_eratosthenes(16) == [2, 3, 5, 7, 11, 13]

    def test_30(self):
        assert sieve_of_eratosthenes(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
