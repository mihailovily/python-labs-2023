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



from_ = int(input())
to_ = int(input())

amicable_pairs = []
for i in range(from_, to_ + 1):
    for j in range(i + 1, to_ + 1):
        if amic(i) and amic(j):
            amicable_pairs.append((i, j))

if amicable_pairs:
    for pair in amicable_pairs:
        print(pair)
