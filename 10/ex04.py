# 경사하강법(해석편미분)
import os
import sys
from pathlib import Path
try:
    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))
    from common import method_least_squares, mean_squares_error
except ImportError:
    print('Library Module Can Not Found')
import numpy as np

# data
times = [2, 4, 6, 8]
scores = [81, 93, 91, 97]

def analytic_gradient(x, data_training):
    dx = np.zeros_like(x)

    n = len(data_training[0])
    data_y_hay = x[0] * data_training[0] + x[1]
    error = data_y_hay - data_training[1]

    dx[0] = (2/n) * np.sum(error * data_training[0])
    dx[1] = (2/n) * np.sum(error)

    return dx

# 경사하강법
x = np.array([0., 0.])
lr= 0.01
epoch = 100

for i in range(epoch):
    gradient = analytic_gradient(x, (np.array(times), np.array(scores)))
    print(f'epoch={i+1}, gradient={gradient}, x={x}')

    x -= lr * gradient

a, b = tuple(x)
print(f'직선 y = {x[0]}x + {x[0]}')
print(f'오차(평균제곱오차):{mean_squares_error(np.array([a, b]), (times, scores)) }')