from random import randint

a = []
for i in range(100):
    a.append(randint(-100, 100))
a = a + a.copy()
print(a)