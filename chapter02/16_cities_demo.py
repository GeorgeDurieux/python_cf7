def print_cities(*cities, sep=', ', end='\n'):
    """
    Prints a list of cities separated and ending with a specified character.

    Parameters: 
        *cities (str): Cities to be printed
        sep (str): Separator. Default is ', '
        end (str): End character. Default is '\n'
    """
    if not cities:
        print('No cities provided', end = end)
    else:
        print('Cities:', sep.join(cities), end = end)

def main():
    print_cities()
    print_cities('Athens')
    print_cities('Athens', 'London', 'Paris')
    print_cities('Athens', 'London', 'Paris', sep=' | ', end = '.\n')

if __name__ == '__main__':
    main()