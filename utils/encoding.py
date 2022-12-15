from utils.prime import is_prime
from utils.prime import prime_factors
from utils.prime import sieve_of_eratosthenes
from utils.prime import next_prime
from collections import deque


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


def decode_exponents(data: str) -> list:
    expression = data[1:-1]

    char_stack = deque()
    exponent_stack = deque()

    expression = data[1:-1]
    for i in range(0, len(expression)):
        char = expression[i]

        if char == ".":
            if len(char_stack) == 0:
                exponent_stack.append(0)
        elif char == '(':
            if len(char_stack) == 0:
                exponent_stack.append(0)

            char_stack.append(char)
        elif char == ')':
            if len(char_stack) > 0:
                char_stack.pop()

                if len(exponent_stack) == 0:
                    exponent_stack.append(0)

                exponent_stack[-1] += 1


    return exponent_stack


def decode(data: str) -> int:
    if len(data) == 0:
        raise ValueError("Unable to decode empty string!")

    if data == ".":
        return 0

    exponents = decode_exponents(data)

    prime = 2
    product = 1

    for exponent in exponents:
        product *= prime ** exponent
        prime = next_prime(prime)

    return product


