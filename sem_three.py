import numpy as np

def solver(data):
    data = np.append([[0, 0, 0, 0, 0, 0, 0, 0, 1, 1]], data, axis=0)

    for i in range(len(data[0])):
        if data[0][i] == 1:
            for j in range(len(data)):
                if j != 0 and data[j][i] == 1:
                    data[0] = data[0] - data[j]
    
    while(True):
        for i in range(len(data[0])):
            if i == 0: continue

            if data[0][i] < 0:
                min_idx = 1000000
                min = 1000000
                for j in range(len(data)):
                    if j == 0: continue
                    if data[j][0] / data[j][i] < min:
                        min_idx = j
                        min = data[j][0] / data[j][i]
                data[min_idx] = data[min_idx] / data[min_idx][i]
                
                for j in range(len(data)):
                    if j == min_idx: continue
                    data[j] = data[j] - (data[min_idx] * data[j][i])
                print(data)


data = np.array([[1.0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                 [5.0, 10, -1, -1, 1, -1, -1, 0, 0, 1],
                 [7.0, 12, 1, 12, -1, 1, 0, 1, 0, 0]])

print(data)
print()

solver(data)

