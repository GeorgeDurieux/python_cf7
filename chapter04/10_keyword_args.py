from typing import List, Tuple, Dict, Optional

def get_results(products, **kwargs):
    """
    Filter a list of products based on given keyword arguments.
    Each keyword argument corresponds to a product attribute.

    Params: 
        products (List[Tuple[str, int]]): A list of tuples that contain brand and price. 
        **kwargs (Dict[str, str | int]): Arbitrary keyword arguments for filtering.

    Returns: 
        results (List[Tuple[str, int]]): Filtered list of products.
    """
    results = [
        (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') == price
    ]
    return results

def main():
    products = [('Lenovo', 100), (('Lenovo', 40), ('Imb', 100))]
    criteria = {'brand': 'Lenovo', 'price': 100}

    print(get_results(products, **criteria))

if __name__ == '__main__':
    main()