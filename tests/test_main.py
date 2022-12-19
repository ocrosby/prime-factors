from main import sieve_of_atkin


class TestSieveOfAtkin:
    def test_5(self):
        assert sieve_of_atkin(5) == [2, 3, 5]

    def test_6(self):
        assert sieve_of_atkin(6) == [2, 3, 5]

    def test_100(self):
        assert sieve_of_atkin(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
