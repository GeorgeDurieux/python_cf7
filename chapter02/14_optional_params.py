def get_formatted_date(day: int = 1, month: int = 1, year: int = 2000) -> str:
    """
    Returns a string representation of a date in the format 'dd/mm/yyyy'

    Args: 
        day (int): defaults to 1
        month (int): defaults to 1
        year (int): defaults to 2000

    Returns: 
        str: the formatted date
    """
    return f'{day:02d}/{month:02d}/{year:4d}'

def main():
    print(get_formatted_date())
    print(get_formatted_date(18))
    print(get_formatted_date(4, 2))
    print(get_formatted_date(14, 2, 2025))
    print(get_formatted_date(year = 2025))
    print(get_formatted_date(month = 3, day = 17))

if __name__ == '__main__':
    main()