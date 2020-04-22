# # decorator
# def my_decorator(func):
#     def wrap(x, y):
#         print('***********')
#         func(x, y)
#         print('***********')
#     return wrap
#
#
# @my_decorator
# def hello(greeting, emoji):
#     print(greeting, emoji)
#
#
# hello("hi jerin", ":)")

# instead of x, y

# decorator


def my_decorator(func):
    def wrap(*args, **kwargs):
        print('***********')
        func(*args, **kwargs)
        print('***********')
    return wrap


@my_decorator
def hello(greeting, emoji=":?"):
    print(greeting, emoji)


hello("hi jerin")
