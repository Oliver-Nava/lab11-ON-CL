"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a  # raise ZeroDivisionError if a == 0


def log(a, b):
    if b <= 0:
        raise ValueError
    elif a == 1:
        raise ValueError
    elif a <= 0:
        raise ValueError
    return math.log(b, a)  # use math library + raise ValueError


def exp(a, b):
    return a**b
