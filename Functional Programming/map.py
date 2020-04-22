def multiply_by_2(li):
    new_list = []
    for i in li:
        new_list.append(i * 2)
    return new_list


print(multiply_by_2([1, 2, 3]))


def multiply_by_2_by_map(item):
    return item * 10


my_list = [1, 2, 3]
print(list(map(multiply_by_2_by_map, my_list)))
print(my_list)
