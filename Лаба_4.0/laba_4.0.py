import sys


file_path = 'example.txt'
f = open(file_path, "r").read()


def is_number(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

def analyze_file(where_to_search):
    stroki = len(where_to_search.split('\n'))
    slova = len(' '.join(where_to_search.split('\n')).split())
    result = 'Файл проанализирован. Полученные результаты:\nСтроки:' + str(stroki) + '\nСлова: ' + str(slova)
    print(result)
    r = open("results.txt", "w")
    r.write(result)
    r.close()
    print('Результаты записаны в results.txt')

def search_word(word_to_search, where_to_search):
    file_to_analyze = where_to_search.split('\n')
    word_to_search = word_to_search.lower()
    for i in range(len(file_to_analyze)):
        k = file_to_analyze[i]
        if word_to_search in k.lower():
            print('Совпадение найдено в строке', i, ':', k, '\n')

while True:
    print('1 - прочитать текст из файла и провести его анализ\n2 - поискать в файле\n0 - выход')
    choose = input()
    if is_number(choose):
        choose = int(choose)
    if choose == 1:
        analyze_file(f)
    elif choose == 2:
        search_word(input('Введите слово для поиска:\n'), f)
    elif choose == 0:
        sys.exit()
    else:
        print('Неверный ввод')

