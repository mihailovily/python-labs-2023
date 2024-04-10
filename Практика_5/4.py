from random import randint

a = []
b = []


for i in range(3):
    for j in range(3):
        b.append(randint(0, 9))
    a.append(b.copy())
    b.clear()

def printMatrix(a):
    for i in a:
        print(i)
    print()
    


printMatrix(a)
a[2][2] = 'x'
printMatrix(a)
a[2][1] = 'x'
printMatrix(a)
a[2][0] = 'x'
printMatrix(a)
a[1][0] = 'x'
printMatrix(a)
a[0][0] = 'x'
printMatrix(a)
a[0][1] = 'x'
printMatrix(a)
a[0][2] = 'x'
printMatrix(a)
a[1][2] = 'x'
printMatrix(a)
a[1][1] = 'x'
printMatrix(a)