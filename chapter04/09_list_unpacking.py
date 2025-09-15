my_list = [1, 2, 3, 4, 5]

a, _, c, _, e = my_list

print(f'a = {a}, c = {c}, e = {e}')

a, *b = my_list

print(f'a = {a}, b = {b}')

*a, b, c = my_list

print(f'a = {a}, b = {b}, c = {c}')