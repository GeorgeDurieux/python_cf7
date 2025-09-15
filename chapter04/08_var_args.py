def my_add(*args: int) -> int:
    return sum(args)

def my_avg(*args: int) -> float:
    return sum(args) / len(args) if args else 0