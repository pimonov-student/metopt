import numpy as np

def function(point):
    return 3 * (point[0] ** 2) + point[0] * point[1] + (point[1] ** 2) + np.exp(point[1])

def function_grad(point):
    return np.array([6 * point[0] + point[1], point[0] + 2 * point[1] + np.exp(point[1])])

def h_matrix(y):
    return np.array([[6, 1], [1, 2 + np.exp(y)]])

def newton(start_point, eps):
    x_i = start_point.copy()
    iter = 0
    while True:
        iter += 1
        x_i_grad = function_grad(x_i)
        if(np.linalg.norm(x_i_grad) < eps):
            return x_i, iter
        h_i = h_matrix(x_i[1])
        h_i_inv = np.linalg.inv(h_i)
        delta_x = h_i_inv @ -(x_i_grad)
        x_i_new = x_i + delta_x
        x_i = x_i_new

start_point = np.array([1, 1])
eps = 0.01

res, iter = newton(start_point, eps)

print(res)
print(function(res))
print(iter)