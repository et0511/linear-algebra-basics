# 편미분(partial Diffirentiation): x0를 3으로 고정해서 설명
# x0 = 3, x1 = 4

def f(x1):
    return 3.**2 + x1**2

def numerical_diff(f, x1):
    h = 1.0e-4      # 개인 지정
    return (f(x1 + h) - f(x1 - h)) / (2 * h)

def analytic_diff(x1):
    return 2 * x1

# (x0, x1) = (3, 4)
print(f'Numerical Diffirentiation Value:{numerical_diff(f, 4)}')
print(f'(Analytic Diffirentiation Value:{analytic_diff(4)}')

# (x0, x1) = (3, 1)
print(f'Numerical Diffirentiation Value:{numerical_diff(f, 1)}')
print(f'(Analytic Diffirentiation Value:{analytic_diff(1)}')

# (x0, x1) = (3, 2)
print(f'Numerical Diffirentiation Value:{numerical_diff(f, 2)}')
print(f'(Analytic Diffirentiation Value:{analytic_diff(2)}')