def make_list(n):
    result = []
    for i in range(n):
        result.append(i)
    return result


l1 = make_list(10)
print(l1)


def generator_func(n):
    for i in range(n):
        yield i


g = generator_func(10)
print(g)
next(g)
next(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))