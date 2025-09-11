products = {1: 'apple', 2: 'banana', 3: 'honey', 4: 'mellon'}

print(f'Initial: {products}')

products[5] = 'orange'

print(f'After insertion: {products}')

product_1 = products[1]

product_10 = products.get(10, 'Not found')

removed_item = products.pop(10, 'Not found')

print('Product 10 get:' + product_10)

print('Removed product 10:' + removed_item)

del products[1]

print('After deleting:' + products)

key, value = products.popitem()

for key in products:
    print(key, ':', products[key])

for value in products.values():
    print(value)

for key, value in products.items():
    print(f'{key} : {value}')

    