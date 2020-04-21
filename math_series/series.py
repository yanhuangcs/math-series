def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return n


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    pass
