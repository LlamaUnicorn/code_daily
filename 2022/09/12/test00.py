# The lambda keyword in Python provides a
# shortcut for declaring small and 
# anonymous functions:

add = lambda x, y: x + y
check0 = add(5, 3)
print(check0)

add2 = lambda a, b: a + b
check1 = add2(1, 2)
print(check1)

## That didn't work
# lst = [1, 2, 3]
# for i in lst:
#     print(lambda i: i * 2)

# You could declare the same add() 
# function with the def keyword:

def add(x, y):
    return x + y
check = add(5, 3)
print(check)

# So what's the big fuss about?
# Lambdas are *function expressions*:
(lambda x, y: x + y)(5, 3)


# • Lambda functions are single-expression 
# functions that are not necessarily bound
# to a name (they can be anonymous).

# • Lambda functions can't use regular 
# Python statements and always include an
# implicit `return` statement.