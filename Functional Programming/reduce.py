from functools import reduce

list1 = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


new_list = reduce(accumulator, list1, 0)
print(new_list)
