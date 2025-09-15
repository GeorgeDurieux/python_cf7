list_of_ints = list(range(1, 8))

sq_nums = [num ** 2 for num in list_of_ints]

print(sq_nums)

sq_nums_map = list(map(lambda num: num ** 2, list_of_ints))

print(sq_nums_map)

def square_function(num):
    return num ** 2

sq_nums_func = [square_function(num) for num in list_of_ints if num < 5]

sq_map_func = list(map(square_function, list_of_ints))

filtered_list_compr = [num ** 2 for num in list_of_ints if num < 5]