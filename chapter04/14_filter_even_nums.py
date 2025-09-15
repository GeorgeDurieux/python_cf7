numbers = list(range(1, 11))

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(*even_numbers)

even_num_list = list(filter(lambda x: x % 2 == 0, numbers))

print(even_num_list)

def even_num_func(n):
    return n % 2 == 0

my_list = list(filter(even_num_func, numbers))

print(my_list)
