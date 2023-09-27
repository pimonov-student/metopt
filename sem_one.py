import numpy as np
import math

def func(x):
    return x ** 3 + math.exp(-x)

def perebor(a, b, eps):
    N = (b - a)  / eps
    delta_x = (b - a) / N

    x = a
    f = func(x)
    x_n = x + delta_x
    f_n = func(x_n)

    func_calc_num = 2

    while (f_n < f):
        func_calc_num += 1
        
        x = x_n
        f = f_n
        x_n = x + delta_x
        f_n = func(x_n)
    
    return x, func_calc_num

def golden_ratio(a, b, max_calc_num):
    x_2 = a + ((math.sqrt(5) - 1) / 2) * (b - a)
    x_1 = a + b - x_2

    f_2 = func(x_2)
    f_1 = func(x_1)

    func_calc_num = 0

    while(func_calc_num < max_calc_num):
        if (f_2 > f_1):
            b = x_2
            x_2 = x_1
            f_2 = f_1

            x_1 = a + b - x_2
            f_1 = func(x_1)

            func_calc_num += 1
        else:
            a = x_1
            x_1 = x_2
            f_1 = f_2

            x_2 = a + ((math.sqrt(5) - 1) / 2) * (b - a)
            f_2 = func(x_2)

            func_calc_num += 1
    
    min = (b + a) / 2
    eps = (b - a) / 2

    return min, eps
    
min_perebor, perebor_func_calc_num = perebor(0, 1, 0.05)
min_gold, eps_gold = golden_ratio(0, 1, perebor_func_calc_num)

print('Минимум:\t\t\t', min_perebor)
print('Значение в минимуме:\t\t', func(min_perebor))
print('Количество вычислений функции:\t', perebor_func_calc_num)

print()

print('Минимум:\t\t\t', min_gold)
print('Значение в минимуме:\t\t', func(min_gold))
print('Точность:\t\t\t', eps_gold)
