from random import randint

zel = []
dejstv = []
dlina = int(input('Введие длину списка: '))
for i in range(dlina):
    zel.append(randint(-99, 99))
    dejstv.append(randint(-99, 99) / 1.5)

uniq = []
for i in range(dlina):
    if zel.count(zel[i]) == 1 and dejstv.count(zel[i]) == 0:
        uniq.append(zel[i])
    if zel.count(dejstv[i]) == 0 and dejstv.count(dejstv[i]) == 1:
        uniq.append(dejstv[i])


print(uniq)
