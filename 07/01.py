# 편미분(partial Diffirentiation): x1을 4로 고정해서 설명
# x0 = 3, x1 = 4

import os
import sys
from pathlib import Path
try:
    sys.path.append(os.path.join(Path(os.getcwd()).parent, 'lib'))
    from common import numerical_diff
except ImportError:
    print('Library Module Can Not Found')


def f(x0):
    # y = x0**2 + x1**2
    return x0**2 + 4**2

# (x0, x1) = (3, 4)
print(f'Numerical Diffirentiation Value:{numerical_diff(f, 3)}')

# (x0, x1) = (1, 4)
print(f'Numerical Diffirentiation Value:{numerical_diff(f, 1)}')

# (x0, x1) = (2, 4)
print(f'Numerical Diffirentiation Value:{numerical_diff(f, 2)}')
