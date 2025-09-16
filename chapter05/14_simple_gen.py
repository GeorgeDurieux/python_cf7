def simple_generator():
    print('1')
    yield 1
    print('2')
    yield 2

def main():
    gen = simple_generator()
    print(next(gen))
    print(next(gen))

if __name__ == '__main__':
    main()