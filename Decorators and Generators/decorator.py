# higher order function - which accepts a function as
# parameter or returns a function


def hello(func):
    func()


def greet():
    print("still here!")


print(hello(greet))


# HOF example
def greet2():
    def func():
        return 5
    return func
