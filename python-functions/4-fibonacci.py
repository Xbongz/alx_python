#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci = [0, 1]
        for i in range (2, n):
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
        return fibonacci