meters = float(input('Введите число в метрах: '))
convert_to = int(input('Во что конвертируем?\n1 - сантиметры\n2 - миллиметры\n3 - километры\n'))
if convert_to == 1:
    print("Сантиметры: ", meters * 100)
elif convert_to == 2:
    print("Миллиметры: ", meters * 1000)
elif convert_to == 3:
    print("Километры: ", meters / 1000)
else:
    print("Error")