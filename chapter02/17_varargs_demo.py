def get_average(*numbers):
    if not numbers:
        return 'No numbers provided'
    average = sum(numbers) / len(numbers)
    return '{:.2f}'.format(average)

def main():
    nums = [10, 20, 30, 40]
    avg = get_average(*nums)
    print(avg)

if __name__ == '__main__':
    main()