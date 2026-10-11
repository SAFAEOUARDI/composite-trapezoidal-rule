
import math

def f(x):
    return math.exp(-x**2)

def composite_trapezoidal(f, a, b, n):
    h = (b - a) / n
    S = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        S = S + 2 * f(x)

    I = (h / 2) * S
    return I

a = 0
b = 1

for n in [4, 6]:
    I = composite_trapezoidal(f, a, b, n)
    print("Integral I =", "n =", n, "I =", I)
