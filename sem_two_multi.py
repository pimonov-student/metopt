import numpy as np
import math

def og_func(x):
    return math.sin(x) + (x / 2) - ((x ** 2) / 20)

def new_func(x):
    return math.sin(x) + (x / 4) - ((x ** 2) / 40)

def perebor(func, a, b, eps, L):
    delta = eps / L
    min_f = 1000000
    min_x = 0

    x = a
    f = func(x)

    while (x <= b):
        if (f < min_f):
            min_x = x
            min_f = f
        x += delta
        f = func(x)
    
    return min_x

apr_eps = 0.01

min_perebor = perebor(og_func, 0, 10, apr_eps, 3 / 2)
min_new_perebor = perebor(new_func, 0, 9, apr_eps, 1.25)

print('Минимум:\t\t\t', min_perebor)
print('Значение в минимуме:\t\t', og_func(min_perebor))

print()

print('Минимум:\t\t\t', min_new_perebor)
print('Значение в минимуме:\t\t', new_func(min_new_perebor))
