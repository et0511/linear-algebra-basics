# 항등행렬
# 단위 행렬의 다른 이름이다.

import numpy as np

m1 = np.identity(3)
print(m1)

m2 = np.arange(1, 10). reshape(3, 3)
print(m2)

# 단위행렬(항등행렬)과의 닷(dot()) 연산(0) 결과는 그대로 이다.
m3 = np.dot(m2, m1)
print(m3)
