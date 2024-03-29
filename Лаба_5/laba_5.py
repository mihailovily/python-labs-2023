from random import randint
import time

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


def sort_bubble():
    pass

def sort_selection():
    pass

def sort_insertion():
    pass

def sort_merge():
    pass

def sort_quick():
    pass

def sort_timsort():
    pass

def sort_heap():
    pass

def sort_counting():
    pass

def sort_bucket():
    pass

def sort_radix():
    pass


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
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 2:  # Сортировка выбором (Selection Sort)
        time_start = time.perf_counter()
        test_sorted = sort_selection(test_massiv)
        time_finish = time.perf_counter()
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 3:  # Сортировка вставками (Insertion Sort)
        time_start = time.perf_counter()
        test_sorted = sort_insertion(test_massiv)
        time_finish = time.perf_counter()
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 4:  # Сортировка слиянием (Merge Sort)
        time_start = time.perf_counter()
        test_sorted = sort_merge(test_massiv)
        time_finish = time.perf_counter()
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 5:  # Быстрая сортировка (Quick Sort)
        time_start = time.perf_counter()
        test_sorted = sort_quick(test_massiv)
        time_finish = time.perf_counter()
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 6:  # Тим-сортировка (Timsort)
        time_start = time.perf_counter()
        test_sorted = sort_timsort(test_massiv)
        time_finish = time.perf_counter()
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 7:  # Сортировка кучей (Heap Sort):
        time_start = time.perf_counter()
        test_sorted = sort_heap(test_massiv)
        time_finish = time.perf_counter()
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 8:  # Сортировка подсчетом (Counting Sort)
        time_start = time.perf_counter()
        test_sorted = sort_counting(test_massiv)
        time_finish = time.perf_counter()
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 9:  # Блочная сортировка (Bucket Sort)
        time_start = time.perf_counter()
        test_sorted = sort_bucket(test_massiv)
        time_finish = time.perf_counter()
        print("Время работы: " + str(time_finish - time_start))
    elif selection == 10:  # Сортировка радиксом (Radix Sort)
        time_start = time.perf_counter()
        test_sorted = sort_radix(test_massiv)
        time_finish = time.perf_counter()
        print("Время работы: " + str(time_finish - time_start))
    else:
        print("Неверный ввод")
