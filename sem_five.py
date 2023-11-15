import numpy as np

great_num_of_calc = 0
def function(arg):
    global great_num_of_calc
    great_num_of_calc += 1
    return 5 * (arg[0] ** 2) + 5 * (arg[1] ** 2) + 8 * arg[0] * arg[1]

def hooke_jeeves(func, dim, eps, start):
    delta = 0.5

    curr_point = start.copy()
    prev_point = start.copy()
    
    f_start = 0

    while True:
        if f_start == 0:
            f_start = func(curr_point)
        
        # Ищем по координатам точку, меньше начальной
        for coord in range(dim):
            curr_point[coord] -= delta
            f_moved = func(curr_point)
            if (f_moved > f_start):
                curr_point[coord] += delta
                f_moved = f_start
            else:
                f_start = f_moved
        
        # Нашли новую точку
        # Проверяем на критерий остановки
        length = 0
        for coord in range(dim):
            length += (prev_point[coord] - curr_point[coord]) ** 2
        length = np.sqrt(length)
        if (length <= eps):
            break

        # Если критерий остановки не сработал, двигаемся
        new_curr_point = 2 * curr_point - prev_point
        new_f_start = func(new_curr_point)
        

        for coord in range(dim):
            new_curr_point[coord] -= delta
            new_f_moved = func(new_curr_point)
            if (new_f_moved > new_f_start):
                new_curr_point[coord] += delta
                new_f_moved = new_f_start
            else:
                new_f_start = new_f_moved
        
        if (new_f_start >= f_start):
            prev_point = new_curr_point.copy()
        else:
            prev_point = curr_point.copy()
            curr_point = new_curr_point.copy()


    return curr_point

dimension = 2
epsilon = 0.01

start_point = [1, 1]

res = hooke_jeeves(function, dimension, epsilon, start_point)
print("result point:\t\t", res)
print("f(result point):\t", function(res))
print("number of calculations:\t", great_num_of_calc)
