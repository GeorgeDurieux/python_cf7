message = 'Factory'

for i in range(len(message)):
    print(message[i] * (i + 1))

for i in range(len(message)):
    print(message[i] * (i + 1), end='*' * (len(message) - i - 1))
    print()    