# менеджер задач с приоитетами
# приоритет, название
import sys


tasks = []
def add_task(name, priority):
    for i in range(len(tasks)):
        if name == tasks[i][1]:
            return "Имя уже занято"
    tasks.append([str(priority), str(name)])
    return 'Задача выполнена успешно'

def remove_task(name):
    for i in range(len(tasks)):
        if name == tasks[i][1]:
            tasks.pop(i)
            return 'Успешно'
    return 'Нет задачи с таким названием'


def update_task(name, priority):
    for i in range(len(tasks)):
        if name == tasks[i][1]:
            tasks[i][0] = priority
            return 'Успешно'
    return 'Нет задачи с таким названием'

def print_tasks():
    return sorted(tasks, key=lambda priritet: priritet[0])

while True:
    print('Вэлком ту таск манагер. Что хотите сделать?\n1 - добавить задачу\n2 - удалить задачу\n3 - обновить приоритет\n4 - вывести задачи\n0 - выйти')
    selected = int(input())
    if selected == 1:
        print(add_task(input('Введите название задачи\n'), int(input('Введите приоритет задачи (от 0 до 10)\n'))))
    elif selected == 2:
        print(remove_task(input('Введите название задачи\n')))
    elif selected == 3:
        print(update_task(input('Введите название задачи\n'), int(input('Введите приоритет задачи (от 0 до 10)\n'))))
    elif selected == 4:
        print(print_tasks())
    elif selected == 0:
        sys.exit()
    else:
        print('я тебя совсем не понял')