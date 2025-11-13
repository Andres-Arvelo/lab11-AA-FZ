
import math
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a==0:
        raise ZeroDivisionError
    b / a # raise ZeroDivisionError if a == 0


def log(a, b):
    loga(b)# use math library + raise ValueError
    if a<=0 or a==1 or b<=0:
        raise ValueError
    return math.log(b,a)


def exp(a, b):
    return a**b
