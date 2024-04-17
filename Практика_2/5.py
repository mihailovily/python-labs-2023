def nod(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return nod(a - b, b)
        else:
            return nod(a, b - a)


print(nod(175, 90))
