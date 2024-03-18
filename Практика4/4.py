from random import randint

zel = []
dejstv = []
dlina = int(input('Введие длину списка: '))
for i in range(dlina):
    zel.append(randint(-99, 99))
    dejstv.append(randint(-99, 99) / 1.5)

uniq = []
for i in range(dlina):
    if zel[i] < 5:
        uniq.append(zel[i])
    if dejstv[i] < 5:
        uniq.append(dejstv[i])


print(uniq)
