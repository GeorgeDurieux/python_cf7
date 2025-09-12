def calculate_sum_and_product(upper_bound):
    sum = 0
    prod = 1
    for i in range(1, upper_bound + 1):
        sum += i
        prod *= i

    return sum, prod

def main():
    try:
        upper_bound = int(input('Insert an integer: '))
    except ValueError:
        print('Error')
        return
    
    sum, prod = calculate_sum_and_product(upper_bound)
    print(f'Sum: {sum}')
    print(f'Prod: {prod}')

if __name__ == '__main__':
    main()