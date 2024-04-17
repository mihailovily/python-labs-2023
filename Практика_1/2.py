chislo = int(input())
pyramid = []

layer = 1

for i in range(1, chislo+1):
    pyramid.append(i**2)
    if sum(pyramid) == chislo:
        break
    if sum(pyramid) > chislo:
        print('Число не пирамидальное')
        break

if len(pyramid) > 2:
    m = [1, 4]
    for i in range(1, len(pyramid)):
        m.append(m[i]+m[i-1])
    print(m)