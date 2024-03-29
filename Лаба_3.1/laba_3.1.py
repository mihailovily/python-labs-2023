board = [
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

def board_print(board):
    for row in board:
        for element in row:
            print(element, end=' ')
        print()

def is_number(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

def win(board, player):
    for row in board:
        if row.count(player) == 3: return True

    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player: return True

    if all([board[i][i] == player for i in range(3)]): return True

    if all([board[i][2 - i] == player for i in range(3)]): return True

player = '0'
while True:
    board_print(board)
    print(f"Ход игрока {player}")
    row = (input("Введите строку: "))
    column = (input("Введите столбец: "))
    if is_number(row) and is_number(column):
        row = int(row) - 1
        column = int(column) - 1
        if row > 2 or row < 0 or column > 2 or column < 0:
            print('неверный формат координат')
            continue      
    else:
        print('неверный формат координат')
        continue
    board[row][column] = player
    if win(board,player) == True:
        print(f"Победил игрок {player}")
        break

    if player == '0':
        player = 'X'
    else: player = '0'