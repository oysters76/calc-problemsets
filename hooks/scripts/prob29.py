#refer problems/prob29.txt 

import math

def h(x, derv=False):
    if derv:
        return 2/math.sqrt((2*x))
    return 4 * math.sqrt(2*x)

def g(x, derv=False):
    if derv:
        return 6 * (math.e ** (2-x))
    return -6 * math.e ** (2-x)

def f(x, derv=False):
    return h(x, derv) + g(x, derv)

def tangent_equation(x0):
    m = f(x0, True) 
    y0 = f(x0) 
    b = y0 - m * x0 

    print(f"f({x0}) = {y0:.4f}") 
    print(f"f'({x0}) = {m:.4f}") 
    print() 

    sign = "+" if b >= 0 else "-"
    print(f"Equation: y = {m:.4f}x {sign} {abs(b):.4f}") 
    print() 

    def t(x):
        return m * (x-x0)  + y0 

    return t 


t = tangent_equation(2) 
