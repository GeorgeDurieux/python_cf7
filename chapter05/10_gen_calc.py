def calculator(n1, n2, operation):
    try:
        return operation(n1, n2)
    except TypeError as e:
        print(e)

def add(n1, n2):
    return n1 + n2

def mul(n1, n2):
    return n1 * n2
    
def main():
    print(calculator(7, 9, add))

if __name__ == '__main__':
    main()