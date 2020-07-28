people_cars = {'Adam': 'Volvo', 'Kate': 'BMW', 'Mark': 'BMW', 'Hannah': 'Ford', 'Max': 'Volvo', 'Celine':'Fiat'}

car_make_lengths = set()

for value in people_cars.values():
    car_make_lengths.add(len(value))

print(f'There will be {len(car_make_lengths)} different sizes of key rings.')

