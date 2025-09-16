import functools

def calculate(args):

    def plus():
        return functools.reduce(lambda x, y: x + y, args)
    
    def minus():
        return functools.reduce(lambda x, y: x - y, args)
    
    def mul():
        return functools.reduce(lambda x, y: x * y, args)
    
    def div():
        return args[0] / sum(args[1:])
    
    return {
        'add': plus,
        'subtract': minus,
        'multiply': mul,
        'division': div
    }

def main():
    list_of_ints = [26, 5, 4, 3, 2, 1]
    operations = calculate(list_of_ints)

    while True:
        print('\nChoose an operation:')
        print('Addition')
        print('Subtraction')
        print('Mutiplication')
        print('Division')
        print('Exit')

        try:
            choice = int(input('Choose an option (1-5): '))
        except ValueError:
            print('Invalid input')
            continue

        match choice:
            case 1:
                print(f'Addition: {operations['add']()}')
            case 2:
                print(f'Subtraction: {operations['subtract']()}')
            case 3:
                print(f'Mutiplication: {operations['multiply']()}')
            case 4:
                print(f'Division: {operations['division']()}')
            case 5:
                print('Ciao')
                break
            case _:
                print('Invalid input.')
            


if __name__ == '__main__':
    main()