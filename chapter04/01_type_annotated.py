def my_add(a: float | int, b: float | int) -> float | int:
    """
    Adds two numbers.

    Args: 
        a (int, float)
        b (int, float)

    Returns:
        int | float: The sum.

    Raise: 
        TypeError: if a or b not int or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError('Need floats or ints')
    
    return a + b

def main():
    try:
        print(my_add('Hello', 20.5))
    except TypeError as e:
        print(e)
        print(my_add.__annotations__)
        print(my_add.__doc__)

if __name__ == '__main__':
    main()