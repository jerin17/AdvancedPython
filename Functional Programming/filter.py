my_list = [1, 2, 3]


def only_odd(item):
    return item % 2 != 0


new_list = list(filter(only_odd, my_list))
print(new_list)