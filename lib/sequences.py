#!/usr/bin/env python3

def print_fibonacci(length):
    array = list()

    if length == 0:
        print(array)
    elif length == 1:
        array.append(0)
        print(array)
    else:
        sequence = [0, 1]
        for i in range(2, length):
            next_fib = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_fib)
        print(sequence)


print_fibonacci(9)
print_fibonacci(20)
