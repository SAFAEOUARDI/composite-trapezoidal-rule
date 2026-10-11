
import math

def f(x):
    return math.exp(-x**2)

def composite_simpson(f, a, b, n):
    h = (b - a) / n
    I = f(a)

    for i in range(1, n):
        x = a + i * h

        if i % 2 == 1:
            I = I + 4 * f(x)
        else:
            I = I + 2 * f(x)

    I = I + f(b)
    I = I * h / 3

    return I

a = 0
b = 1

for n in [4, 6]:
    I = composite_simpson(f, a, b, n)
    print("Integral I =", "n =", n, "I =", I)
