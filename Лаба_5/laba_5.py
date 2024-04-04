from random import randint
import time
import random

# названия функций сортировки начинаем с sort


def is_number(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False


def generate_list(numbers):  # инициализируем тестовый массив
    testmassiv = []
    for k in range(numbers):
        testmassiv.append(randint(-1 * numbers, numbers))
    return testmassiv


def sort_bubble(massiv_to_sort):
    sorted_massiv = massiv_to_sort.copy()
    N = len(sorted_massiv)
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if sorted_massiv[j] > sorted_massiv[j + 1]:
                sorted_massiv[j], sorted_massiv[j + 1] = (
                    sorted_massiv[j + 1],
                    sorted_massiv[j],
                )
    return sorted_massiv.copy()


def sort_selection(massiv_to_sort):
    sorted_massiv = massiv_to_sort.copy()
    n = len(sorted_massiv)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if sorted_massiv[j] < sorted_massiv[min]:
                min = j
        sorted_massiv[i], sorted_massiv[min] = sorted_massiv[min], sorted_massiv[i]
    return sorted_massiv.copy()


def sort_insertion(massiv_to_sort):
    sorted_massiv = massiv_to_sort.copy()
    for i in range(1, len(sorted_massiv)):
        for j in range(i - 1, -1, -1):
            if sorted_massiv[j] > sorted_massiv[j + 1]:
                sorted_massiv[j], sorted_massiv[j + 1] = (
                    sorted_massiv[j + 1],
                    sorted_massiv[j],
                )
    return sorted_massiv.copy()


def sort_merge(massiv_to_sort):
    size = len(massiv_to_sort)
    if size > 1:
        middle = size // 2
        left_arr = massiv_to_sort[:middle]
        right_arr = massiv_to_sort[middle:]

        sort_merge(left_arr)
        sort_merge(right_arr)

        p = 0
        q = 0
        r = 0

        left_size = len(left_arr)
        right_size = len(right_arr)
        while p < left_size and q < right_size:
            if left_arr[p] < right_arr[q]:
                massiv_to_sort[r] = left_arr[p]
                p += 1
            else:
                massiv_to_sort[r] = right_arr[q]
                q += 1

            r += 1

        while p < left_size:
            massiv_to_sort[r] = left_arr[p]
            p += 1
            r += 1

        while q < right_size:
            massiv_to_sort[r] = right_arr[q]
            q += 1
            r += 1
    return massiv_to_sort.copy()


def sort_quick(massiv_to_sort):
    if len(massiv_to_sort) <= 1:
        return massiv_to_sort
    else:
        q = random.choice(massiv_to_sort)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in massiv_to_sort:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return sort_quick(s_nums) + e_nums + sort_quick(m_nums)


def sort_timsort(massiv_to_sort):
    return sorted(massiv_to_sort)


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
        heapify(arr, n, largest)


def sort_heap(massiv_to_sort):
    n = len(massiv_to_sort)
    for i in range(n // 2, -1, -1):
        heapify(massiv_to_sort, n, i)
    for i in range(n - 1, 0, -1):
        (massiv_to_sort[i], massiv_to_sort[0]) = (
            massiv_to_sort[0],
            massiv_to_sort[i],
        )  # swap
        heapify(massiv_to_sort, i, 0)


def sort_counting(massiv_to_sort):
    size = len(massiv_to_sort)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[massiv_to_sort[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[massiv_to_sort[i]] - 1] = massiv_to_sort[i]
        count[massiv_to_sort[i]] -= 1
        i -= 1
    return output


def sort_bucket(massiv_to_sort):
    max_value = max(massiv_to_sort)
    size = max_value / len(massiv_to_sort)
    buckets_list = []
    for x in range(len(massiv_to_sort)):
        buckets_list.append([])
    for i in range(len(massiv_to_sort)):
        j = int(massiv_to_sort[i] / size)
        if j != len(massiv_to_sort):
            buckets_list[j].append(massiv_to_sort[i])
        else:
            buckets_list[len(massiv_to_sort) - 1].append(massiv_to_sort[i])
    for z in range(len(massiv_to_sort)):
        sort_insertion(buckets_list[z])
    final_output = []
    for x in range(len(massiv_to_sort)):
        final_output = final_output + buckets_list[x]
    return final_output


def countingSortForRadix(inputArray, placeValue):
    countArray = [0] * 10
    inputSize = len(inputArray)
    # equal to 2
    for i in range(inputSize):
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] += 1

    for i in range(1, 10):
        countArray[i] += countArray[i - 1]
    outputArray = [0] * inputSize
    i = inputSize - 1
    while i >= 0:
        currentEl = inputArray[i]
        placeElement = (inputArray[i] // placeValue) % 10
        countArray[placeElement] -= 1
        newPosition = countArray[placeElement]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray


def sort_radix(massiv_to_sort):
    maxEl = max(massiv_to_sort)
    D = 1
    while maxEl > 0:
        maxEl /= 10
        D += 1
    placeVal = 1
    outputArray = massiv_to_sort
    while D > 0:
        outputArray = countingSortForRadix(outputArray, placeVal)
        placeVal *= 10
        D -= 1
    return outputArray


print("Генерирую тестовый массив")
test_massiv = generate_list(10000)

while True:
    print(
        "Как будем сортировать?\n1 - Bubble sort\n2 - Selection sort\n3 - Insertion sort\n4 - Merge sort\n5 - Quick sort\n6 - Timsort\n7 - Heap sort\n8 - Counting sort\n9 - Bucket Sort\n10 - Radix Sort\n"
    )
    selection = input()
    if is_number(selection):
        selection = int(selection)
    if selection == 1:  # Сортировка пузырьком (Bubble Sort)
        time_start = time.perf_counter()
        test_sorted = sort_bubble(test_massiv)
        time_finish = time.perf_counter()
        print(test_sorted)
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 2:  # Сортировка выбором (Selection Sort)
        time_start = time.perf_counter()
        test_sorted = sort_selection(test_massiv)
        time_finish = time.perf_counter()
        print(test_sorted)
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 3:  # Сортировка вставками (Insertion Sort)
        time_start = time.perf_counter()
        test_sorted = sort_insertion(test_massiv)
        time_finish = time.perf_counter()
        print(test_sorted)
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 4:  # Сортировка слиянием (Merge Sort)
        time_start = time.perf_counter()
        test_massiv_2 = test_massiv.copy()
        sort_merge(test_massiv_2)
        time_finish = time.perf_counter()
        print(test_massiv_2)
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 5:  # Быстрая сортировка (Quick Sort)
        test_massiv_2 = test_massiv.copy()
        time_start = time.perf_counter()
        test_sorted = sort_quick(test_massiv_2)
        time_finish = time.perf_counter()
        print(test_sorted)
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 6:  # Тим-сортировка (Timsort)
        time_start = time.perf_counter()
        test_sorted = sort_timsort(test_massiv)
        time_finish = time.perf_counter()
        print(test_sorted)
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 7:  # Сортировка кучей (Heap Sort):
        test_massiv_2 = test_massiv.copy()
        time_start = time.perf_counter()
        sort_heap(test_massiv_2)
        time_finish = time.perf_counter()
        print(test_massiv_2)
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 8:  # Сортировка подсчетом (Counting Sort)
        time_start = time.perf_counter()
        test_sorted = sort_counting(test_massiv)
        time_finish = time.perf_counter()
        print(test_sorted)
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 9:  # Блочная сортировка (Bucket Sort)
        time_start = time.perf_counter()
        test_sorted = sort_bucket(test_massiv)
        time_finish = time.perf_counter()
        print(test_sorted)
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 10:  # Сортировка радиксом (Radix Sort)
        time_start = time.perf_counter()
        test_sorted = sort_radix(test_massiv)
        time_finish = time.perf_counter()
        print(test_sorted)
        print("Время работы: " + str(time_finish - time_start))
    else:
        print("Неверный ввод")
