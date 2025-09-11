a = True
b = False

print(type(a), a, sep=', ')
print(type(b), b, sep=', ')

# Short circuit
res = a or b
print(res)

print('True + true =', True + True)