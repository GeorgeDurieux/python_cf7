def calc_facto(n):
    facto = 1

    for i in range(1, n + 1):
        facto *= i
        return facto

def main(): 
    try:
        n = int(input('Insert an integer: '))
        if n < 0:
            raise ValueError
    except ValueError:
        print('Error')
        return
    
    facto = calc_facto(n)
    print(f'{n}! = {facto}')

if __name__ == '__main__':
    main()