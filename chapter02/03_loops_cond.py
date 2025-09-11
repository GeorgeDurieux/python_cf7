a = range(10)
print(type(a))
print(a)

for i in range(1000000000):
    if i ==5:
        break
    print(i, end=' ')
print()

for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
else:
    print('Loop ended normally') 

for i in range(10):
    if i == 5:
        continue
    print(i, end=' ')
else:
    print('Loop ended normally')

fruits = ['banana', 'orange', 'mango', 'grapes']

fruit_to_check = 'banana'

for fruit in fruits:
    if fruit == fruit_to_check:
        print(f'{fruit_to_check} is in the list')
        break
else:
    print(f'{fruit_to_check} not in list')

print('Why do python devs never get lost?')
print('Because they always know where "in" is!')    

if fruit_to_check in fruits:
    print(f'{fruit_to_check} is in the list')
else:
    print(f'{fruit_to_check} not in list')

print(f'{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} the list')