chislo = int(input())
pyramid = []

layer = 1

for i in range(1, chislo+1):
    pyramid.append(i**2)
    if sum(pyramid) == chislo:
        print(pyramid)
        break
    if sum(pyramid) > chislo:
        print('Число не пирамидальное')
        break

