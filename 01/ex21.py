# 행렬과 벡터의 @연산

import numpy as np

m1 = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

m2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

v = np.array([10, 100])

# 벡터와의 @ 연산도 가능하다.: 행렬의 열의 크와 같아야 한다.
m3 = m1 @ v
print(m3, m3.shape)

# 오류!
# v @ m1

# 벡터와의 @ 연산도 가능하다.: 행렬의 행의 차원과 같아야 한다.
m4 = v @ m2
print(m4, m4.shape)

# 오류!
# m2 @ v
