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
    
    return plus, minus, mul, div

def main():
    list_of_ints = [26, 5, 4, 3, 2, 1]
    plus_func, minus_func, mul_func, div_func = calculate(list_of_ints)
    print(plus_func())
    print(minus_func())
    print(mul_func())
    print(div_func())

if __name__ == '__main__':
    main()