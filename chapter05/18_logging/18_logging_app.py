import logging

def main():
    log_file = 'cf7.log'

    file_handler = logging.FileHandler(log_file, mode='a')

    handlers = [file_handler]

    logger = logging.getLogger('search-app')

    logging.basicConfig(
        handlers=handlers,
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'
    )

    my_nums = [10, 20, 30, 40, 50]

    num_to_find = 200

    try:
        index = my_nums.index(num_to_find)
        print('Found')
        print(index)
    except ValueError as e:
        logger.error(f'ERROR: {e}', exc_info=True)

if __name__ == '__main__':
    main()