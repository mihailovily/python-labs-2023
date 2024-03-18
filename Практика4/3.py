from random import randint

zel = []
dejstv = []
dlina = int(input('Введие длину списка: '))
for i in range(dlina):
    zel.append(randint(-99, 99))
    dejstv.append(randint(-99, 99) / 1.2)

projizv = 1
for i in range(dlina):
    projizv = projizv * zel[i] * dejstv[i]

print(projizv)