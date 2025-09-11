a = 10
b = 20
res = a + b

print(f'{a} + {b} = {res}')

print(f'Type of a: {type(a)}')

magic_result = a.__add__(b)

print(f'Magic result: {magic_result}')