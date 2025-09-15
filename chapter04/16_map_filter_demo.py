cities = ['london', 'paris', 'athens', 'barcelona', 'casablanca']

long_cities = filter(lambda city: len(city) > 5, cities)

print(*long_cities)

cap_length_cities = list(map(lambda city: city.title(), long_cities))

print(long_cities)

clc = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities)))

print(clc)

cap_title_cities_compr = [city.title() for city in cities if len(city) > 5]