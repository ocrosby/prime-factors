#!/usr/bin/env python3

from utils.encoding import encode

if __name__ == "__main__":
    buffer = input()
    while buffer != 'exit':
        value = int(buffer)
        encoded_value = encode(value)

        print(encoded_value)
        buffer = input()
