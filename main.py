#!/usr/bin/env python3

import sys

from utils.encoding import encode

if __name__ == "__main__":
    lines = sys.stdin.readlines()

    for line in lines:
        value = int(line)
        encoded_value = encode(value)

        print(encoded_value)
