import numpy as np

great_num_of_calc = 0
def function(arg):
    global great_num_of_calc
    great_num_of_calc += 1
    return 5 * (arg[0] ** 2) + 5 * (arg[1] ** 2) + 8 * arg[0] * arg[1]

def golden_ratio(func, a, b, x_2, eps, coord):
    x_1 = x_2.copy()
    x_1[coord] = a[coord] + b[coord] - x_2[coord]

    f_2 = func(x_2)
    f_1 = func(x_1)

    func_calc_num = 0
    
    while(b[coord] - a[coord] > 2 * eps):
        if (f_2 > f_1):
            b = x_2.copy()
            x_2 = x_1.copy()
            f_2 = f_1

            x_1[coord] = a[coord] + b[coord] - x_2[coord]
            f_1 = func(x_1)

            func_calc_num += 1
        else:
            a = x_1.copy()
            x_1 = x_2.copy()
            f_1 = f_2

            x_2[coord] = a[coord] + ((np.sqrt(5) - 1) / 2) * (b[coord] - a[coord])
            f_2 = func(x_2)

            func_calc_num += 1
    
    min = (b[coord] + a[coord]) / 2

    return min

def coordinate_descent(func, dim, eps, start):
    curr_point = start.copy()
    prev_point = start.copy()

    while (True):
        delta = eps / np.sqrt(dim)
        for coord in range(dim):
            # Будем хранить начальное направление убывания функции
            # и флаг, оповещающий о нахождении диапазона
            direction = ""
            area_is_found = False

            # Определяем начальный диапазон
            a = curr_point.copy()
            b = a.copy()
            b[coord] += delta

            # Значения функции в начальных точках
            f_a = func(a)
            f_b = func(b)

            # Ищем диапазон
            while(not area_is_found):
                # Первая итерация, определяем направление убывания
                if (direction == ""):
                    if (f_b > f_a):
                        direction = "left"
                    elif (f_b < f_a):
                        direction = "right"
                    else:
                        area_is_found = True
                        continue
                
                # Функция убывает "влево"
                if (direction == "left"):
                    if (f_b > f_a):
                        last_edge = b.copy()
                        b = a.copy()
                        f_b = f_a
                        delta *= (np.sqrt(5) + 1) / 2
                        a[coord] -= delta
                        f_a = func(a)
                    else:
                        area_is_found = True
                        continue
                # Функция убывает "вправо"
                elif (direction == "right"):
                    if (f_b < f_a):
                        last_edge = a.copy()
                        a = b.copy()
                        f_a = f_b
                        delta *= (np.sqrt(5) + 1) / 2
                        b[coord] += delta
                        f_b = func(b)
                    else:
                        area_is_found = True
                        continue

            # Нашли диапазон    
            # print("area is found")

            # Ищем минимум по координате
            if (direction == "left"):
                coord_min = golden_ratio(func, a, last_edge, b, eps, coord)
            elif (direction == "right"):
                coord_min = golden_ratio(func, last_edge, b, a, eps, coord)
            
            curr_point[coord] = coord_min

        length = 0
        for coord in range(dim):
            length += (prev_point[coord] - curr_point[coord]) ** 2
        length = np.sqrt(length)
        
        if length <= eps:
            break
        prev_point = curr_point.copy()
    
    return curr_point

dimension = 2
epsilon = 0.01

start_point = [1, 1]

# res = 0
# f = func(res)
# num_of_calculations = 0

res = coordinate_descent(function, dimension, epsilon, start_point)
print("result point:\t\t", res)
print("f(result point):\t", function(res))
print("number of calculations:\t", great_num_of_calc)
