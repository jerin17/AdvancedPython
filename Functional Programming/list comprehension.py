# list1 = []
# for i in 'hello':
#     list1.append(i)

list1 = [i for i in 'hello']
print(list1)

list2 = [n for n in range(20)]
print(list2)

list3 = [n*2 for n in range(20)]
print(list3)

list4 = [n*2 for n in range(20) if n % 2 == 0]
print(list4)


list5 = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = set([i for i in list5 if list5.count(i) > 1])
print(list(duplicates))
