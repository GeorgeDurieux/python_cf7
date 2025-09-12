def main():
    n = int(input('Num: '))
    a = 0
    b = 1
    
    for i in range(2, n + 1):
        temp = a
        a = b
        b += temp
    
    print(f'The {n}th fibo number is: {b}')

if __name__ == '__main__':
    main()