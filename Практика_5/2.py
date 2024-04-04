from random import randint

a = []
b = []
stolbec = []
stolbcy = []

for i in range(10):
    for j in range(10):
        b.append(randint(10, 99))
    a.append(b.copy())
    b.clear()

#for i in a:
#    print(i)

for i in range(10):
    for j in range(10):
        stolbec.append(a[j][i])
    stolbcy.append(sum(stolbec))
    stolbec.clear()
    
print(stolbcy.index(max(stolbcy)))
