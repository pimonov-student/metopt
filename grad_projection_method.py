import numpy as np

def func(point):
    x, y, z = point[0], point[1], point[2]
    return np.exp(x) * (y ** 2 + y * z + z ** 2 + 1)

def func_grad(point):
    x, y, z = point[0], point[1], point[2]
    grad = np.array([np.exp(x) * (y ** 2 + y * z + z ** 2 + 1),
                     (2 * y + z) * np.exp(x),
                     (2 * z + y) * np.exp(x)])
    return grad

def is_good(point):
    x, y, z = point[0], point[1], point[2]
    is_good = True if ((x - 1) ** 2 + (y - 2) ** 2 + (z - 3) ** 2) <= 1 else False
    return is_good

def do_projection(point, sphere_center):
    projected_point = sphere_center + (point - sphere_center) * 1 / (np.linalg.norm(point - sphere_center))
    return projected_point

def grad_projection(start_point, sphere_center, eps):
    curr_point = start_point.copy()
    if not is_good(curr_point):
        curr_point = do_projection(curr_point, sphere_center)
    
    while True:
        prev_point = curr_point.copy()
        # find minimum
        alpha = 1
        while alpha > eps:
            grad = func_grad(curr_point)
            new_curr_point = curr_point - alpha * grad

            f_curr = func(curr_point)
            f_new_curr = func(new_curr_point)
            
            if np.linalg.norm(curr_point - new_curr_point) < eps:
                break

            if f_curr < f_new_curr:
                alpha /= 2
            else:
                curr_point = new_curr_point.copy()
        
        if not is_good(curr_point):
            curr_point = do_projection(curr_point, sphere_center)
        if np.linalg.norm(curr_point - prev_point) < eps:
            break
    
    return curr_point

sphere_center = np.array([1, 2, 3])
start_point = np.array([0, 0, 0])
eps = 0.01

minimum = grad_projection(start_point, sphere_center, eps)

print("Точка: ", minimum)
print("Удовлетворяет ограничению? : ", is_good(minimum))
print("Значение функции в точке: ", func(minimum))
