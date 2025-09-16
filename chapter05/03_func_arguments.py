def test_args_func(pos_arg1, pos_arg2, opt_arg1=None, opt_arg2=None, *args, **kwargs) :
    """
    A function to demonstrate the useage of positional, optional, additional optional (*args) and additional optional keyword arguments (**kwargs).

    Parameters: 
        pos_arg1 (Any): The first positional argument.
        pos_arg2 (Any): The second positional argument.
        opt_arg1 (Any): The first optional argument.
        opt_arg2 (Any): The second optional argument.
        *args (Any): Additional positional arguments.
        **kwargs (Any): Additional keyword arguments. 
    """
    if args:
        print('Additional arguments:')
        for arg in args:
            print(arg)

    if kwargs:
        print('Additional keyword arguments:')
        for key, value in kwargs:
            print(key, value)

def main():
    test_args_func('hello', 'CF', 100, 200)
    test_args_func('hello', 'CF', name='George', age=34)

if __name__ == '__main__':
    main()