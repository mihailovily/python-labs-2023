def is_simple(chislo):
    return (all_delitels(chislo) == [1, chislo] or all_delitels(chislo) == [1])

def all_delitels(chislo):
    delitels = []
    for i in range(1, chislo+1):
        if chislo % i == 0:
            delitels.append(i)
    return delitels

for i in range(int(input()), int(input())+1):
    if is_simple(i):
        print(i)