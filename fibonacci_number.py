def fib(n):
    """
    Compute the nth Fibonacci number, n >= 2

    """
    prev, curr = 0, 1
    k = 2
    while k < n:
        prev, curr = curr, curr + prev
        k += 1
    return curr

help(fib)