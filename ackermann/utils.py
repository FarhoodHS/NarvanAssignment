
# Ackermann Calculation Logic


def ackermann_func(m, n):
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ackermann_func(m - 1, 1)

    return ackermann_func(m - 1, ackermann_func(m, n - 1))
