def main():
    store_a_products = {'Apples', 'Bananas', 'Cherries', 'Watermellons'}
    store_b_products = {'Bananas', 'Cherries', 'Figs', 'Grapes', 'Melons'}

    common_products = store_a_products & store_b_products
    common_products2 = store_a_products.intersection(store_b_products)
    print(f'Common: {common_products}')
    print(f'Common2: {common_products2}')

    all_products = store_a_products | store_b_products
    all_products2 = store_a_products.union(store_b_products)
    print(f'All: {all_products}')
    print(f'All2: {all_products2}')

    store_b_exclusive = store_b_products - store_a_products
    store_b_exclusive2 = store_b_products.difference(store_a_products)

    unique = store_a_products ^ store_b_products
    unique2 = store_a_products.symmetric_difference(store_b_products)

if __name__ == '__main__':
    main()