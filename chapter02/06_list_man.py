fruits = ['apple', 'banana', 'cherry', 'apple']

print(f'Initial list: {fruits}')

fruits.append('berry')

print(f'After adding berry: {fruits}')

fruits.extend(['grapes', 'fig'])

print(f'After adding fruit: {fruits}')

fruits.insert(1, 'coconut')

print(f'After adding coconut: {fruits}')

fruits[0] = 'watermellon'

print(f'After adding updating the first element: {fruits}')

fruits[1:3] = ['tomato']

print(f'After adding slicing: {fruits}')

removed_items = fruits.pop(2)
print(f'Popped: {removed_items}')
print(f'After popping: {fruits}')

if 'berry' in fruits:
    fruits.remove('berry')
    print(f'After removing berry: {fruits}')

idx = fruits.index('fig')
print(f'Fig index: {idx}')

