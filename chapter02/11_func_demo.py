def say_hello(name: str = 'CF'):
    """
    Prints a greeting message.
    Args:
        name (str): The name to greet. Default: 'CF'
    """
    print(f'Hello {name}')

def main():
    say_hello()
    say_hello('Ragnar')
    print('DOCS')
    print(say_hello.__doc__)
    print('HELP')
    help(say_hello)

if __name__ == '__main__':
    main()
