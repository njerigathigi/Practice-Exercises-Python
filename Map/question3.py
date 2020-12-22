# Write a Python program to listify the list of given strings individually using Python map.

cars = ['ford', 'volvo', 'nisssan']

new_car_list = list(map(list, cars))

print(new_car_list)
