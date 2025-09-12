def name_space(num):
    
    if not isinstance(num, int):
        print('Invalid input')
        return
    
    if num < 0:
        print('Need positive')
    
    name = input('Name: ')

    if not name:
        print('No name')
        return
    
    spaced_name = (' ' * num).join(name)

    print(spaced_name)

def main():
    try:
        num = int(input('Number: '))
        name_space(num)
    except ValueError:
        print('Error')

if __name__ == '__main__':
    main()