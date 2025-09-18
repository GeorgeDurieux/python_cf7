import logging
from typing import List, Any

def configure_logger(log_file: str, logger_name: str) -> logging.Logger:
    """
    Configure and return a logger with both file and console handlers.

    Args: 
        log_file (str): The name of the log file.
        logger_name (str): The name of the logger.

    Returns:
        logging,Logger: Configure logger instance.
    """
    logger = logging.getLogger(logger_name)

    file_handler = logging.FileHandler(log_file, mode='a')

    file_handler.setFormatter(
        logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    )

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(
        logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    )

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def search_item(items: List[Any], item_to_find: Any, logger: logging.Logger) -> int:
    """
    Search for an item in a list and return index.
    
    Args:
        items: (List[Any]): List of items to search.
        item_to_find (Any): Item to find.
        logger (logging.logger): Logger instance for logging messages.

    Returns: 
        int: The index of the item in the list.

    Raises:
        ValueError: If not found.
    """
    if not items:
        logger.warning('List is empty')
        raise ValueError('Cannot search in empty list.')
    
    try:
        index = items.index(item_to_find)
        logger.info(f'Item {item_to_find} found in index {index}')
        return index
    except ValueError as e:
        logger.error(f'Item {item_to_find} not found. Error: {e}', exc_info=True)
        raise # re-raise the same e

def main():
    log_file = 'cf7_2.log'

    logger = configure_logger(log_file, 'search-app2')

    employee_names = ['Alice', 'Bob', 'Charlie', 'Melanie', 'Helen', 'Diana']

    employee_to_find = 'Chris'

    try: 
        index = search_item(employee_names, employee_to_find, logger)
        print(f'{employee_to_find} found at index {index}')
    except ValueError:
        print(f'{employee_to_find} was not found')


if __name__ == '__main__':
    main()