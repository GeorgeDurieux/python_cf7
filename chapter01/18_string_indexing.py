message = 'Coding Factory'

print(message[0])

print(f'Length: {len(message)}')

for char in message: 
    print(char, end=' ')

for i in range(10):
    print(i)

print(i)        

for i in range(len(message)):
    print(message[i], end=' ')
print()    

my_num = 123456789

result = int(str(my_num)[0]) + int(str(my_num)[len(str(my_num)) - 1])

print(result)
