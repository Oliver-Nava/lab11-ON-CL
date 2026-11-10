# https://github.com/Oliver-Nava/lab11-ON-CL
# Oliver Nava Partner 1
# Carlos Laege

"""
calculator.py
- Defines functions used to create a simple calculator
One function per operation, in order.
"""
import math

def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError("Cant use negative numbers")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return a / b  # raise ZeroDivisionError if a == 0


def logarithm(a, b):
    if b <= 0:
        raise ValueError
    elif a == 1:
        raise ValueError
    elif a <= 0:
        raise ValueError
    return math.log(b, a)  # use math library + raise ValueError


def exp(a, b):
    return a**b
