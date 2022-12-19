#!/usr/bin/env python3
import math
import sys


def sieve_of_eratosthenes(n: int) -> list:
    """Return a list of prime numbers less than or equal to n.

    :param n: The upper limit of the range of numbers to check for primality.
    :return: A list of prime numbers less than or equal to n.
    """
    if n <= 0:
        return []

    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(len(primes)) if primes[i]]

def sieve_of_atkin(limit: int) -> list:
    """Return a list of prime numbers less than or equal to n.

    :param n: The upper limit of the range of numbers to check for primality.
    :return: A list of prime numbers less than or equal to n.
    """
    # 2 and 3 are known
    # to be prime
    P = [2, 3]
    r = range(1, int(math.sqrt(limit)) + 1)
    sieve = [False] * (limit + 1)
    for x in r:
        for y in r:
            xx = x * x
            yy = y * y
            xx3 = 3 * xx
            n = 4 * xx + yy
            if n <= limit and (n % 12 == 1 or n % 12 == 5): sieve[n] = not sieve[n]
            n = xx3 + yy
            if n <= limit and n % 12 == 7: sieve[n] = not sieve[n]
            n = xx3 - yy
            if x > y and n <= limit and n % 12 == 11: sieve[n] = not sieve[n]
    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            xx = x * x
            for y in range(xx, limit + 1, xx):
                sieve[y] = False
    for p in range(5, limit):
        if sieve[p]: P.append(p)
    return P

    # Print primes
    # using sieve[]
    # for a in range(5, n + 1):
    #     if sieve[a]:
    #         print(a, end=" ")


def least_prime_factor(n: int) -> int:
    """Return the least prime factor of n.

    :param n: The number to find the least prime factor of.
    :return: The least prime factor of n.
    """
    if n < 1:
        return 0

    if n == 1:
        return 1

    if n % 2 == 0:
        return 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i

    return n

def prime_factors(n: int) -> list:
    """Return a list of the prime factors of n.

    :param n: The number to find the prime factors of.
    :return: A list of the prime factors of n.
    """
    factors = []

    if n >= 1:
        while n != 1:
            factor = least_prime_factor(n)
            factors.append(factor)
            n = n // factor

    return factors


def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise.

    :param n: The number to check for primality.
    :return: True if n is prime, False otherwise.
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def count_factors(factor: int, factor_list: list) -> int:
    """Return the number of times factor appears in factor_list.

    :param factor: The factor to count.
    :param factor_list: The list of factors to count factor in.
    :return: The number of times factor appears in factor_list.
    """
    count = 0
    for i in factor_list:
        if i == factor:
            count += 1

    return count


def encode(data: int) -> str:
    """Return a string representation of data.

    :param data: The data to encode.
    :return: A string representation of data.
    """
    if data == 0:
        return "."

    if data == 1:
        return "()"

    # primes_lte = sieve_of_eratosthenes(data)
    primes_lte = sieve_of_atkin(data)
    factor_list = prime_factors(data)
    max_factor = max(factor_list)

    buffer = ""
    for prime in primes_lte:
        if prime > max_factor:
            if not is_prime(data):
                continue

        exponent = count_factors(prime, factor_list)
        buffer += encode(exponent)

    return f"({buffer})"


if __name__ == "__main__":
    while True:
        line = sys.stdin.readline()

        if not line:
            break

        print(encode(int(line)))
