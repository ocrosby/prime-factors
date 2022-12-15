from utils.prime import prime_factors
from utils.prime import sieve_of_eratosthenes
from utils.prime import least_prime_factor
from utils.prime import next_prime


class TestPrimeFactors:
    def test_0(self):
        assert prime_factors(0) == []

    def test_1(self):
        assert prime_factors(1) == []

    def test_2(self):
        assert prime_factors(2) == [2]

    def test_3(self):
        assert prime_factors(3) == [3]

    def test_4(self):
        assert prime_factors(4) == [2, 2]

    def test_5(self):
        assert prime_factors(5) == [5]

    def test_6(self):
        assert prime_factors(6) == [2, 3]

    def test_7(self):
        assert prime_factors(7) == [7]

    def test_8(self):
        assert prime_factors(8) == [2, 2, 2]

    def test_9(self):
        assert prime_factors(9) == [3, 3]

    def test_10(self):
        assert prime_factors(10) == [2, 5]

    def test_11(self):
        assert prime_factors(11) == [11]

    def test_12(self):
        assert prime_factors(12) == [2, 2, 3]

    def test_13(self):
        assert prime_factors(13) == [13]

    def test_14(self):
        assert prime_factors(14) == [2, 7]

    def test_15(self):
        assert prime_factors(15) == [3, 5]

    def test_16(self):
        assert prime_factors(16) == [2, 2, 2, 2]

    def test_17(self):
        assert prime_factors(17) == [17]

    def test_12246(self):
        assert prime_factors(12246) == [2, 3, 13, 157]


class TestLeastPrimeFactor:
    def test_1(self):
        assert least_prime_factor(1) == 1

    def test_2(self):
        assert least_prime_factor(2) == 2

    def test_3(self):
        assert least_prime_factor(3) == 3

    def test_4(self):
        assert least_prime_factor(4) == 2

    def test_5(self):
        assert least_prime_factor(5) == 5

    def test_6(self):
        assert least_prime_factor(6) == 2

    def test_7(self):
        assert least_prime_factor(7) == 7

    def test_8(self):
        assert least_prime_factor(8) == 2

    def test_9(self):
        assert least_prime_factor(9) == 3

    def test_10(self):
        assert least_prime_factor(10) == 2


class TestNextPrime:
    def test_0(self):
        assert next_prime(0) == 2

    def test_1(self):
        assert next_prime(1) == 2

    def test_2(self):
        assert next_prime(2) == 3

    def test_3(self):
        assert next_prime(3) == 5

    def test_4(self):
        assert next_prime(4) == 5

    def test_5(self):
        assert next_prime(5) == 7

    def test_6(self):
        assert next_prime(6) == 7

    def test_7(self):
        assert next_prime(7) == 11

    def test_8(self):
        assert next_prime(8) == 11

    def test_9(self):
        assert next_prime(9) == 11

    def test_10(self):
        assert next_prime(10) == 11

    def test_11(self):
        assert next_prime(11) == 13

    def test_12(self):
        assert next_prime(12) == 13

    def test_13(self):
        assert next_prime(13) == 17

    def test_14(self):
        assert next_prime(14) == 17

    def test_15(self):
        assert next_prime(15) == 17

    def test_16(self):
        assert next_prime(16) == 17

    def test_17(self):
        assert next_prime(17) == 19

    def test_18(self):
        assert next_prime(18) == 19

    def test_19(self):
        assert next_prime(19) == 23

    def test_20(self):
        assert next_prime(20) == 23





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



def test_sieve_of_eratosthenes_0():
    assert sieve_of_eratosthenes(0) == []