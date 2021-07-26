def fibonacci(n):
    if n == 0:
        return 0
        
    elif n == 1:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(m):
    if m == 0:
        return 2

    elif m == 1:
        return 1

    else:
        return lucas(m-1) + lucas(m-2)


def sum_series(z, x=0, y=1):
    if z == 0:
        return x

    elif z == 1:
        return y

    else:
        return sum_series(z-1, x, y) + sum_series(z-2, x, y)

print(lucas(6))
