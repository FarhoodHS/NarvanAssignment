
# Factorial Calculation Logic
# This can also be done by using "math" library


def factorial_func(num):
    res = 1
    if num == 0 or num == 1:
        return res
    else:
        for i in range(1, num+1):
            res *= i
    return res
