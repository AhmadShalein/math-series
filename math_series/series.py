def fibonacci(n):
    # if n == 0:
    #     return 0
        
    # elif n == 1:
    #     return 1

    # else:
    #     return fibonacci(n-1) + fibonacci(n-2)
    return sum_series(n)


def lucas(n):
    # if m == 0:
    #     return 2

    # elif m == 1:
    #     return 1

    # else:
    #     return lucas(m-1) + lucas(m-2)
    return sum_series(n,2,1)


def sum_series(n,x=0,y=1):
    if n == 0:
        return x

    elif n == 1:
        return y

    else:
        return sum_series(n-1,x,y) + sum_series(n-2,x,y)

print(fibonacci(6))
print(lucas(6))
