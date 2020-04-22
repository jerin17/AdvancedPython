
set1 = {i for i in 'hello'}
print(set1)

set2 = {n for n in range(20)}
print(set2)

set3 = {n*2 for n in range(20)}
print(set3)

set4 = {n*2 for n in range(20) if n % 2 == 0}
print(set4)

sample_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

my_dict1 = {k: v**2 for k, v in sample_dict.items() if v % 2 == 0}
print(my_dict1)

my_dict2 = {x: x*2 for x in [1, 2, 3, 4, 5]}
print(my_dict2)
