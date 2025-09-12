def process_characters():
    ch = input('char: ')

    while ch != '#':
        print(ch, ' : ', ord(ch))
        ch = input('char: ')
    print('Ciao')

def process_characters2():
    while True:
        ch = input('char: ')
        if ch == '#':
            break
        print(ch, ' : ', ord(ch))
        
    print('Ciao')

def main():
    process_characters()
    process_characters2()

if __name__ == '__main__':
    main()