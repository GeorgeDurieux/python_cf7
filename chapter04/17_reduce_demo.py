from functools import reduce

my_ints = list(range(1, 6))

result = reduce(lambda x, y: x + y, my_ints)

print(result)

result2 = reduce(lambda x, y: x * y)

print(result2) 