#https://github.com/Andres-Arvelo/lab11-AA-FZ.git
#Partner 1: Andres Arvelo
#Partner 2: Fareed Zaki
import math



def square_root(a):
        if a < 0:
            raise ValueError("square root input must be non-negative")
        return math.sqrt(a)

def hypotenuse(a, b):
    try:
        return math.hypot(a,b)
    except Exception as e:
        print(f"Error: {e}")

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero is not allowed")
    return a / b

def log(a, b):
    if b <= 0:
        raise ValueError("logarithm input must be positive")
    if a <= 0 or a == 1:
        raise ValueError("logarithm base must be positive and not equal to 1")
    math.log(b, a)

def exp(a, b):
    return a ** b