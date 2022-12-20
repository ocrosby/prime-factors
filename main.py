#!/usr/bin/env python3
import sys

inputs = []

while True:
    line = sys.stdin.readline()

    if not line:
        break

    line = line.strip()

    if line.isdecimal():
        inputs.append(int(line))
    else:
        print(f"Invalid input: '{line}', expected a decimal number.")
        exit(1)

n = max(inputs)

is_prime = [True] * (n + 1)

for i in range(2, n + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

def encode(n):
    if n == 0:
        return "."

    if n == 1:
        return "()"

    res = ""

    i = 2
    while i <= n+1:
        if is_prime[i]:
            val = 0
            while n % i == 0:
                val += 1
                n //= i

            res += encode(val)

        if n == 1:
            break

        i += 1

    return f"({res})"


if __name__ == "__main__":
    for input in inputs:
        print(encode(input))
