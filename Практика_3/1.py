def sum_delitels(n):
    delitels = []
    for i in range(1, n):
        if n % i == 0:
            delitels.append(i)
    return sum(delitels)

def amic(num):
    first = sum_delitels(num)
    second = sum_delitels(first)

    return num == second and num != first


print(amic(int(input())))
