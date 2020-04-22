# decorator
def my_decorator(func):
    def wrap():
        print('***********')
        func()
        print('***********')

    return wrap


@my_decorator
def hello():
    print('hellooooooo')


@my_decorator
def bye():
    print('see ya later')


hello()
print()
bye()
