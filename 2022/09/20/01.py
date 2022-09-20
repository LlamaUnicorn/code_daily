# How to merge two dictionaries
# in Python 3.5+
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
print(f'\nx: {x}', f'\ny: {y}')
z = {**x, **y}

for _ in x:
    print(f'{_} = {x[_]}')

for _ in y:
    print(f'{_} = {y[_]}')
    
print(f'z: {z}')
# {'c': 4, 'a': 1, 'b': 3}
list1 = [1, 2]
list2 = [3, 4]
print(f'list1: {list1}, list2: {list2}')
list12 = [*list1, *list2]
print(f'list12: {list12}')
# In Python 2.x you could
# use this:
# z = dict(x, **y)
# print(z)
# {'a': 1, 'c': 4, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting 
# duplicates from left to right.