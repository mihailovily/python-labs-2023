import csv

def is_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def filter_below_zero(list_with_zeros):
    list_bigger_zeros = []
    for i in list_with_zeros:
        if i > 0:
            list_bigger_zeros.append(i)
    return list_bigger_zeros


csv_file_path = 'example.csv'
list_of_floats = []

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    data_list = []
    for row in csv_reader:
        data_list.append(row)

for row in data_list:
    for item in row:
        if is_number(item):
            list_of_floats.append(float(item))
print('Вывожу содержмое CSV файла:', data_list, '\nВывожу среднее значение:', (sum(list_of_floats) / len(list_of_floats)), '\nНаибольшее:', max(list_of_floats), '\nНаименьшее:', min(list_of_floats), '\nЧисел в списке:', len(list_of_floats))



