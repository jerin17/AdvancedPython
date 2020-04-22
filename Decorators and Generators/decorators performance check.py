from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"It took {t2-t1} s")
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i += 10


long_time()
