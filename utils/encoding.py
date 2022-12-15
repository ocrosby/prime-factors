from utils.prime import is_prime
from utils.prime import prime_factors
from utils.prime import sieve_of_eratosthenes
from utils.prime import next_prime


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


def decode(data: str) -> int:
    if data == ".":
        return 0

    if data == "()":
        return 1

    stack = []

    base = 2
    result = 1

    expression = data[1:-1]
    for char in expression:
        if char == ".":
            stack.append(0)
        elif char == '(':
            stack.append(char)
        else:
            if stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                stack[-1] += 1




