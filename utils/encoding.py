from utils.prime import is_prime
from utils.prime import prime_factors
from utils.prime import sieve_of_eratosthenes
from utils.prime import next_prime
from utils.tape import ReadTape, WriteTape
from utils.adt import Stack


def count_factors(factor: int, factor_list: list) -> int:
    count = 0
    for i in factor_list:
        if i == factor:
            count += 1
    return count


def has_repeating_factors(data: int) -> bool:
    factor_list = prime_factors(data)
    factor_set = set(factor_list)

    for factor in factor_set:
        exponent = count_factors(factor, factor_list)
        if exponent > 1:
            return True

    return False


def encode(data: int) -> str:
    if data == 0:
        return "."

    if data == 1:
        return "()"

    primes_lte = sieve_of_eratosthenes(data)
    factor_list = prime_factors(data)
    # factor_set = set(factor_list)

    buffer = ""
    for prime in primes_lte:
        if not is_prime(data) and prime > max(factor_list):
            continue

        exponent = count_factors(prime, factor_list)
        buffer += encode(exponent)

    return f"({buffer})"


def decode_factorization(data: str) -> list:
    """Return a list of tuples containing the prime factorization.
    The first element of each tuple is the prime factor, and the second element is the exponent.

    :param data:
    :return:
    """

    stack = Stack()
    factorization = []

    prime_factor = 2
    exponent = 0

    # Handle 0
    if data == ".":
        return []

    # Handle 1
    if data == "()":
        return [(2, 0)]

    tape = ReadTape(data[1:-1])

    while not tape.eof():
        char = tape.read()

        if char == ".":
            if stack.is_empty:
                factorization.append((prime_factor, 0))
                prime_factor = next_prime(prime_factor)
                exponent = 0
            else:
                exponent += 1
        elif char == "(":
            stack.push(char)
        elif char == ")":
            if stack.peek() == "(":
                stack.pop()
                exponent += 1

            if stack.is_empty:
                factorization.append((prime_factor, exponent))
                prime_factor = next_prime(prime_factor)
                exponent = 0

    return factorization


def decode(data: str) -> int:
    if len(data) == 0:
        raise ValueError("Unable to decode empty string!")

    factorization = decode_factorization(data)

    if len(factorization) == 0:
        return 0

    value = 1
    for factor, exponent in factorization:
        value *= factor ** exponent

    return value
