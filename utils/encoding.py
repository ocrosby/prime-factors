from utils.prime import is_prime
from utils.prime import prime_factors
from utils.prime import sieve_of_eratosthenes
from utils.prime import next_prime
from collections import deque
from utils.tape import ReadTape, WriteTape


class TuringMachine:
    state: int
    itape: ReadTape
    otape: WriteTape

    def __init__(self, data: str):
        self.state = 0
        self.itape = ReadTape(data)
        self.otape = WriteTape()
        self.transitions = {
            0: {
                "(": ("(", 1, "R"),
                ".": (".", 2, "R"),
                ")": (")", 3, "R"),
            },

        }

    def step(self):
        if self.itape.eof():
            return False

        current_char = self.itape.read()
        transition = self.transitions[self.state][current_char]
        self.otape.write(transition[0])
        self.state = transition[1]

        if transition[2] == "L":
            self.itape.retract()
        elif transition[2] == "R":
            self.itape.read()

        return True

    def run(self):
        while self.step():
            pass

        return self.output_tape



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


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def next_exponent(itape: ReadTape) -> int:
    exponent = 1
    stack = deque()

    while not itape.eof():
        char = itape.read()

        if char == ".":
            return None

        if char == "(":
            stack.append(char)
        elif char == ")":
            stack.pop()

            if len(stack) == 0:
                break
            else:
                exponent += 1

    return exponent


def experiment(data: str) -> list:
    """Return a list of tuples containing the prime factorization.
    The first element of each tuple is the prime factor, and the second element is the exponent.

    :param data:
    :return:
    """
    char_stack = deque()

    itape = ReadTape(data)
    factorization = []

    prime_factor = 2
    exponent = 0

    while not itape.eof():
        char = itape.read()

        if char == ".":
            if itape.eof():
                return []
        elif char == '(':
            char_stack.append(char)
        elif char == ')':
            if len(factorization) == 0:
                factorization.append((prime_factor, 0))
            else:
                factorization[-1] = (factorization[-1][0], factorization[-1][1] + 1)

            char_stack.pop()

            if len(char_stack) == 0:
                exponent = 0
                prime_factor = next_prime(prime_factor)

    return factorization



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


