def is_square(length: int, width: int) -> bool:
    return length == width

def main():
    try:
        length = int(input('Length: '))
        width = int(input('Width: '))
        if is_square(length, width):
            print('It is square')
        else:
            print('It is not square')
    except ValueError:
        print('Enter integer')

if __name__ == '__main__':
    main()