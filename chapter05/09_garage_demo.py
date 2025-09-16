from collections import deque

def display_garage(garage: deque) -> None:
    if garage:
        print('Cars: ')
        for i, car in enumerate(garage, 1):
            print(f'{i} - {car}')
    else:
        print('Empty')

def add_car(garage: deque, max_capacity: int) -> None:
    if len(garage) < max_capacity:
        car_name = input('Id of car: ')
        garage.append(car_name)
        print(f'{car_name} has entered')
    else:
        print('Full')

def remove_car(garage: deque):
    if garage:
        car = garage.popleft()
        print(f'{car} has left')
    else:
        print('Garage is empty')

def main():
    pass

if __name__ == '__main__':
    main()