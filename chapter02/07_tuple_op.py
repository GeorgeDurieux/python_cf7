students = ('Alice', 'Bob', 'Charlie')

print(f'Students: {students}, type: {type(students)}')

for index, student in enumerate(students):
    print(f'{index}:{student}')

first_st, second_st, third_st = students