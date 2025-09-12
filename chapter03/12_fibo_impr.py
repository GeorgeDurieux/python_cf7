def main():
    n = int(input('Num: '))

    if n in (0, 1): return n
    
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    print(f'The {n}th fibo number is: {b}')

if __name__ == '__main__':
    main()