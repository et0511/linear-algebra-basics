# y = -log(-x)
from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return -np.log(-x)

data_x = np.arange(-2, 0, 0.01)
data_y = f(data_x)

fig, splt = plt.subplots()
splt.plot(data_x, data_y)

splt.axvline(x=0, color='r')
splt.axhline(y=0, color='r')

splt.set_xticks([])
splt.set_yticks([])

plt.show()
