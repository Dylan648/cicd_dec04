import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square(a):
    return a ** 2


def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)


def logarithm(a, base=math.e):
    if a <= 0:
        raise ValueError("Logarithm argument must be positive")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    
    if base == math.e:
        return math.log(a)
    return math.log(a, base)


def sine(a):
    return math.sin(a)


def cosine(a):
    return math.cos(a)


def percentage(value, total):
    if total == 0:
        raise ValueError("Total cannot be zero for percentage calculation")
    return (value / total) * 100