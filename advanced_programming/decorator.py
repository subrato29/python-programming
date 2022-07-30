import time


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Wrapper function called func:")
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorator
def foo(x, y, z):
    print(x, y)


foo(1, 2, 3)

"""
Equivalent to above:
==================
def foo():
    print("Without decorator calling")

decorator(foo)(500)
"""


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        total_time = end_time - start_time
        print("Time taken to execute:", total_time)
        return result

    return wrapper()


@timer
def loop():
    for _ in range(1000):
        pass


loop()
