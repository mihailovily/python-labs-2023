from random import randint


# 1 - камень
# 2 - ножницы
# 3 - бумага
user_win = 'Игрок победил'
pc_win = 'Компьютер победил'


def game(user_choose, pc_choose):
        if user_choose in [1, 2, 3]:
            if user_choose == pc_choose:
                return 'Ничья'
            if user_choose == 1:
                 if pc_choose == 2:
                      return user_win
                 return pc_win
            if user_choose == 2:
                 if pc_choose == 1:
                      return pc_win
                 return user_win
            if user_choose == 3:
                 if pc_choose == 1:
                      return user_win
                 return pc_win
        else:
            return 'Ошибка'


pc_choose = randint(1, 3)
print('1 - камень, \n2 - ножницы, \n3 - бумага')
user_choose = int(input())
print(' PC:', pc_choose, '\n', 'USER:', user_choose, '\n', 'Result:' ,game(user_choose, pc_choose))
    

