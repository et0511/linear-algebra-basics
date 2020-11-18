# 기울기(gradient)
import numpy as np

def f(x):
    return np.sum(x**2, axis=0)     # 손실 함수

# 수치미분으로 기울기 구하기
def numerical_gradient(f, x):
    h = 1e-4
    gradient = np.zeros_like(x)

    # h1 = f(np.array([x[0] + h, x[1]]))
    # h2 = f(np.array([x[0] - h, x[1]]))
    # gradient[0] = (h1 - h2) / (2 * h)

    # h1 = f(np.array([x[0], x[1] + h]))
    # h2 = f(np.array([x[0], x[1] - h]))
    # gradient[1] = (h1 - h2) / (2 * h)
    for i in range(x.size):
        tmp = x[i]

        x[i] = tmp + h
        h1 = f(x)

        x[i] = tmp - h
        h2 = f(x)

        gradient[i] = (h1 - h2) / (2 * h)
        x[i] = tmp

    return gradient


# 경사하강법 구현1
def gradient_descent(f, x, lr=0.01, epoch=100):
    for i in range(epoch):
        gradient = numerical_gradient(f, x)
        # 출력
        print(f'epoch={i+1}, gradient={gradient}, x={x}')
        x -= lr * gradient

    return x

# 최소제곱법(Method of Least Squares)
# 여러 점에서 직선의 기울기 구하기
def method_least_squares(x, y):
    mx = sum(x) / len(x)
    my = sum(y) / len(y)

    # s1 = 0
    # for i in range(len(x)):
    #     s2 += (x[i] - mx) * (y[i] - my)

    s1 = 0
    for i in range(len(x)):
        s1 += (x[i] - mx) * (y[i] - my)
    print(s1)

    s2 = 0
    for i in range(len(x)):
        s2 += (x[i] - mx)**2
    print(s2)

    s1 = sum([(i - mx) * (j - my) for i, j in zip(x, y)])
    s2 = sum([(i - mx)**2 for i in x])

    mls_a = s1 / s2
    mls_b = my - (mx * mls_a)

    return mls_a, mls_b