my_list = [1, 2, 'Hello', [3, 4, 5]]

print('Start')

for item in my_list:
    print(f'{item} : {id(item)}')

new_list = my_list * 2

print('Dublicated:' + new_list)

new_list[0] = 100
new_list[3][0] = 300

print(new_list)