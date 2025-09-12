def is_armstrong_num(n):
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return n == total

def main():
    try:
        num = int(input('Insert an integer'))
    except ValueError: 
        print('Invalid input')

    if is_armstrong_num(num):
        print(f'{num} is an Armstrong number')
    else:
        print(f'{num} is not an Armstrong number')

if __name__ == '__main__':
    main()