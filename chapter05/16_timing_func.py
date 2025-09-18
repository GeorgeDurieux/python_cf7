import time

def get_time(num):
    start_time = time.time()
    result = sum(range(num))
    end_time = time.time()
    print(f'Took {end_time - start_time} seconds')

def main():
    print(get_time(1_000_000))

if __name__ == '__main__':
    main()
