from typing import Sequence, TypeVar, List, Any, Optional

T = TypeVar('T')

Number = TypeVar('Number', int, float)

def first(seq: Sequence[T]) -> T:
    """
    Returns the first element of a sequence
    If sequence is empty, raises ValueError

    Args:
        seq (Sequence[T]: The sequence)

    Returns: 
        T: The first element
    """
    if not seq:
        raise ValueError('Is empty')
    return seq[0]

def last(seq: Sequence[T]) -> T:
    """
    Returns the last element of a sequence
    If sequence is empty, raises ValueError

    Args:
        seq (Sequence[T]: The sequence)

    Returns: 
        T: The last element
    """
    if not seq:
        raise ValueError('Is empty')
    return seq[-1]

def count_truthy(elements: List[Any]) -> bool:
    """
    Returns the last element of a sequence

    Args:
        elements (List[Any]: The list)

    Returns: 
        bool: The number of truthy elements
    """
    return sum(1 for element in elements if element)

def len_str(s: Optional[str] = None) -> int:
    return len(s) if s is not None else 0

def main():
    numbers = [10, 20, 30, 40, 50]
    print(first(numbers))
    print(last(numbers))
    try:
        print(first([]))
    except ValueError as e:
        print(e)

    mixed_values = [0, True, False, 'Hi', '', None,  17]
    print(count_truthy(mixed_values))
    print(len_str('Hello World'))
    print(len_str(None))


if __name__ == '__main__':
    main()    

