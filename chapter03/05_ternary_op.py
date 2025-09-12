def compare_ints(a, b):
    result = 'Equal' if a == b else 'a is bigger' if a > b else 'b is bigger'

def main():
    try:
        a = int(input('a: '))
        b = int(input('b: '))
    except ValueError:
        print('Integers only')
        return
    
    compare_ints(a, b)

if __name__ == '__main__':
    main()