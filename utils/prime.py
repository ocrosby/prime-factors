
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


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise.

    :param n: The number to check for evenness.
    :return: True if n is even, False otherwise.
    """
    return n % 2 == 0


def is_prime(n: int) -> bool:
    """Return True if n is prime, False otherwise.

    :param n: The number to check for primality.
    :return: True if n is prime, False otherwise.
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if is_even(n):
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def next_prime(n: int) -> int:
    """Return the next prime number after n.

    :param n: The number to find the next prime number after.
    :return: The next prime number after n.
    """
    if n < 1:
        return 2

    if n == 1:
        return 2

    if is_prime(n):
        n += 1

    if is_even(n):
        n += 1

    while not is_prime(n):
        n += 2

    return n


def least_prime_factor(n: int) -> int:
    """Return the least prime factor of n.

    :param n: The number to find the least prime factor of.
    :return: The least prime factor of n.
    """
    if n < 1:
        return 0

    if n == 1:
        return 1

    if is_even(n):
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
