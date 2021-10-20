"""
Here we are using "yield" keyword(instead of "return" keyword and Generators (instead of
Iterables) for memory optimization so that we can even calculate the 1000000th term of
the Fibonacci
"""


def fibonacci(k):
    x = 0
    y = 1
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        for i in range(2, k + 1):
            s = x + y
            x = y
            y = s
        yield y


for r in fibonacci(1000000):
    print(r)
