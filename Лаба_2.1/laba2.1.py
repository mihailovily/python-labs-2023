import random

def QuestionGenerator(level):
    if level == 1:
        num1 = random.randint(0,20)
        num2 = random.randint(0,20)
        oper = random.choice(['+','-'])
        if oper == '+':
            question = f'{num1} {oper} {num2}'
            answer = num1 + num2
        else:
            question = f'{num1} {oper} {num2}'
            answer = num1 - num2
    elif level == 2:
        num1 = 1
        num2 = 3
        while not (num1 % num2 == 0):
            num1 = random.randint(0, 30)
            num2 = random.randint(1, 30)
        oper = random.choice(['*', '/'])
        if oper == '*':
            question = f'{num1} {oper} {num2}'
            answer = num1 * num2
        else:
            question = f'{num1} {oper} {num2}'
            answer = num1 // num2
    elif level == 3:
        num1 = random.randint(0, 300)
        num2 = random.randint(1, 300)
        oper = random.choice(['*', '/'])
        if oper == '*':
            question = f'{num1} {oper} {num2}'
            answer = num1 * num2
        else:
            question = f'{num1} {oper} {num2}'
            answer = num1 / num2
    return [question, answer]

print("Привет")
print("Сейчас тебе предстоит пройти математический тест")
print("Какое количество вопросов будет в тесте?")
questsnum = int(input())
print(f"сейчас ты решишь {questsnum} заданий, поехали")

score = [0,0,0] 
for i in range(questsnum):
    level = random.randint(1,3)
    quest = QuestionGenerator(level)
    print(quest[0] + ' = ?')
    if int(input()) == quest[1]:
        print("Верно")
        score = [score[0]+1,score[1]+level,score[2]+level]
    else:
        print("Неверно")
        score[2] += level

print(f'Количество ответов: {score[0]} | твой счёт: {score[1]}/{score[2]}')

