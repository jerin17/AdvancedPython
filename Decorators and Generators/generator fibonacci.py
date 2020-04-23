def fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b


def fib2(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


for x in fib(20):
    print(x)

print(fib2(20))