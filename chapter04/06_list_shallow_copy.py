my_list = [1, 2, 'Hello', [3, 4, 5]]

new_list = my_list[:]

print(f'Sliced: {my_list is new_list}')

my_list[0] = 100
my_list[3][0] = 300

print(my_list)
print(new_list)


