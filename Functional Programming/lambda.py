list1 = [1, 2, 3]
new_list = list(map(lambda x: x*2, list1))
print(new_list)
print(list1)
print()

list2 = [5, 4, 3]
new_list = list(map(lambda x: x**2, list2))
print(new_list)
print(list2)
print()

list3 = [(0, 2), (4, 3), (9, 9), (10, -1)]
list3.sort(key=lambda x: x[1])
# new_list = list(map(lambda x: x**2, list2))
# print(new_list)
print(list3)