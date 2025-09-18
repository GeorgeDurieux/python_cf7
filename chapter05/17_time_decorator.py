import time

def timer_decorator(func):
    """
    Decorator to measure the execution time of a function.

    Params:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function with added fuctionality.
    """
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} took {end_time - start_time} seconds')
        return result
    
    return inner_function

def sum_function(n):
    return sum(range(n))

timed_sum_function = timer_decorator(sum_function)

print(timed_sum_function(1_000_000))

@timer_decorator
def avg_function(n):
    if n == 0:
        return 0
    return sum(range(n)) / n

print(avg_function(1_000_000))