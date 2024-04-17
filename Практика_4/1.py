from random import randint

positive = []
negative = []
dlina = int(input('Введие длину списка: '))
for i in range(dlina):
    positive.append(randint(-99, 99))
for k in positive:
    if k < 0:
        negative.append(k)
print(positive, negative, sep='\n')
