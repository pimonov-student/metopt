import numpy as np
import math

def func(x):
    return x ** 3 + math.exp(-x)

def func_1(x):
    return 3 * (x ** 2) - math.exp(-x)

def func_2(x):
    return 6 * x + math.exp(-x)

def horde(a, b, eps):
    n = 0
    delta = eps
    q = delta

    f_a = func_1(a)
    f_b = func_1(b)
    n += 2

    c = a - (f_a * (b - a))/(f_b - f_a)

    f_c = func_1(c)
    n += 1

    while(abs(f_c) > q):
        if (f_c > q):
            b = c
            f_b = f_c
        elif (f_c < -q):
            a = c
            f_a = f_c
        c = a - (f_a * (b - a))/(f_b - f_a)
        f_c = func_1(c)
        n += 1
        
    min = c
    apostr_eps = abs(func_1(min)) * (b - a)

    return min, n, apostr_eps

def newton(a, b, eps):
    n = 0
    x_0 = (b - a) / 2
    q = eps

    while(abs(func_1(x_0)) > q):
        x_0 = x_0 - (func_1(x_0))/(func_2(x_0))
        n += 2
    
    min = x_0
    apostr_eps = abs(func_1(min)) * (b - a)

    return min, n, apostr_eps

apr_eps = 0.001
min_horde, n_horde, apostr_eps_horde = horde(0, 1, apr_eps)
min_newton, n_newton, apostr_eps_newton = newton(0, 1, apr_eps)

print('Минимум:\t\t\t', min_horde)
print('Значение в минимуме:\t\t', func(min_horde))
print('Количество итераций:\t\t', n_horde)
print('Апостериорная точность:\t\t', apostr_eps_horde)

print()

print('Минимум:\t\t\t', min_newton)
print('Значение в минимуме:\t\t', func(min_newton))
print('Количество итераций:\t\t', n_newton)
print('Апостериорная точность:\t\t', apostr_eps_newton)
