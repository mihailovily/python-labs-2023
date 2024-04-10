import numpy as np
from random import randint

a = []
b = []
stolbec = []
stolbcy = []

for i in range(5):
    for j in range(5):
        b.append(randint(0, 9))
    a.append(b.copy())
    b.clear()
    
for i in a:
    print(i)
    
def getMatrixMinor(arr,i,j):
    c = arr[:]
    c = np.delete(c, (i),axis=0)
    return [np.delete(row, (j),axis=0) for row in (c)]

f = getMatrixMinor(a, 2, 2)

for x in f:
    print(x)
print(np.linalg.det(f))

