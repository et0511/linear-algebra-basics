# Losixtic Regression(로지스틱 회귀)

import os
import sys
from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt
try:
    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))
    from common import gradient_descent

except ImportError:
    print('Library Module Can Not Found')


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def analytic_greadient(x, data_in, data_out):
    gradient = [0., 0.]
    gradient[0] = data_in * (sigmoid(x[0] * data_in + x[1]) - data_out)
    gradient[1] = sigmoid(x[0] * data_in + x[1]) - data_out

    return gradient

# data
times = [2, 4, 6, 8, 10, 12, 14]
passed = [0, 0, 0, 1, 1, 1, 1]


# 경사하강법
x = [0, 0]
for i in range(3000):
    for data_in, data_out in zip(times, passed):
        gradient = analytic_greadient(x, data_in, data_out)

        # 출력
        print(f'epoch={i+1}, gradient={gradient}, x={x}')

        x[0] -= 0.1 * gradient[0]
        x[1] -= 0.1 * gradient[1]


# 그래프
data_x = np.arange(0, 15, 0.1)
data_y = sigmoid(x[0] * data_x + x[1])

fig, splt = plt.subplots()
splt.scatter(times, passed)
splt.plot(data_x, data_y)


plt.show()

