def is_simple(chislo):
    return (all_delitels(chislo) == [1, chislo] or all_delitels(chislo) == [1])

def all_delitels(chislo):
    delitels = []
    for i in range(1, chislo+1):
        if chislo % i == 0:
            delitels.append(i)
    return delitels

def find_all_simple_delitels(chislo):
    all_ = all_delitels(chislo)
    simple_delitels = []
    for k in all_:
        if is_simple(k):
            simple_delitels.append(k)
    if simple_delitels:
        return simple_delitels
    return 'Число не имеет простых делителей'

print(find_all_simple_delitels(int(input())))