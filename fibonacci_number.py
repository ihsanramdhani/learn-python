def fib(n):
    """
    Compute the nth Fibonacci number, n >= 2

    >>> fib(8)
    13
    >>> fib(3)
    1

    """
    prev, curr = 0, 1
    k = 2
    while k < n:
        prev, curr = curr, curr + prev
        k += 1
    return curr

if __name__ == '__main__':
    import doctest
    doctest.testmod()
