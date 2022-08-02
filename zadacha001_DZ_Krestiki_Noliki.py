# 41. Создайте программу для игры в "Крестики-нолики".

import random
tableForMove = [[' ', ' ', ' ', '  1'], [' ', ' ', ' ', '  2'],
                [' ', ' ', ' ', '  3'], ['a', 'b', 'c', ' ']]


def PrintTableForMove(list):
    print('\n\n\n\n    Таблица для ходов:\n')
    for i in range(0, len(list)):
        if i == 0 or i == 1:
            print(
                f'    {list[i][0]} | {list[i][1]} | {list[i][2]} {list[i][3]}')
            print('    ---------')
        elif i == 2:
            print(
                f'    {list[i][0]} | {list[i][1]} | {list[i][2]} {list[i][3]}\n')
        else:
            print(
                f'    {list[i][0]}   {list[i][1]}   {list[i][2]} {list[i][3]}')
    print('\n')


def Game(table):
    PrintTableForMove(tableForMove)
    # случайным образом выбирается чей первый ход
    if random.randint(0, 1) == 1:
        firstMove = 1
        print('Первых ход за игроком.')
    else:
        firstMove = 0
        print('Первых ход за компьютером.')
    # случайным образом выбирается кто чем играет (ноликами или крестиками)
    if random.randint(0, 1) == 1:
        userValue = 'X'
        print('Ты ставишь крестики (X).')
        botValue = 'O'
    else:
        userValue = 'O'
        print('Ты ставишь нолики (O).')
        botValue = 'X'

    # задаем начальное количество сделанных ходов, победителя и список доступных ходов
    moves = 0
    winner = None
    listOfMoves = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']

    while len(listOfMoves) > 0:

        if firstMove == 1:  # ходит человек
            move = CheckInput(input('Куда ставим?: '), listOfMoves, table)
            if move == 'a1':
                table[0][0] = userValue
            elif move == 'b1':
                table[0][1] = userValue
            elif move == 'c1':
                table[0][2] = userValue
            elif move == 'a2':
                table[1][0] = userValue
            elif move == 'b2':
                table[1][1] = userValue
            elif move == 'c2':
                table[1][2] = userValue
            elif move == 'a3':
                table[2][0] = userValue
            elif move == 'b3':
                table[2][1] = userValue
            elif move == 'c3':
                table[2][2] = userValue
            listOfMoves.remove(move)  # удаляем из списка ходов сделанный ход
            moves += 1
            firstMove = 0
            PrintTableForMove(table)
            print(f'Ты ставишь крестики ({userValue}).')

            # обработка победителя
            winner = WhoWins(table)
            if winner == userValue:
                print(f'Поздравляю, вы выиграли, играя за -> {winner}')
                return [1, 0]

        elif firstMove == 0:  # ходит бот
            move = random.choice(listOfMoves)
            if move == 'a1':
                table[0][0] = botValue
            elif move == 'b1':
                table[0][1] = botValue
            elif move == 'c1':
                table[0][2] = botValue
            elif move == 'a2':
                table[1][0] = botValue
            elif move == 'b2':
                table[1][1] = botValue
            elif move == 'c2':
                table[1][2] = botValue
            elif move == 'a3':
                table[2][0] = botValue
            elif move == 'b3':
                table[2][1] = botValue
            elif move == 'c3':
                table[2][2] = botValue
            listOfMoves.remove(move)  # удаляем из списка ходов сделанный ход
            moves += 1
            firstMove = 1
            PrintTableForMove(table)
            print(f'Ты ставишь крестики ({userValue}).')

            # обработка победителя
            winner = WhoWins(table)
            if winner == botValue:
                print(
                    f'К сожалению, эту партию выиграл БОТ, играя за -> {winner}')
                return [0, 1]
    print(f'В этот раз ничья.')
    return [0, 0]  # возвращает ничью

# Метод определяющий победителя (X или O) и возвращающий это значение
def WhoWins(table):
    for x in range(0, 3):
        if table[x][0] == table[x][1] == table[x][2] != ' ':
            print('Игра окончена.')
            return table[x][0]
    for y in range(0, 3):
        if table[0][y] == table[1][y] == table[2][y] != ' ':
            print('Игра окончена.')
            return table[0][y]
    if table[0][0] == table[1][1] == table[2][2] != ' ':
        print('Игра окончена.')
        return table[1][1]
    elif table[0][2] == table[1][1] == table[2][0] != ' ':
        print('Игра окончена.')
        return table[1][1]


# Метод который обрабатывает неправильный пользовательский ввод (или не то поле, или в это поле уже поставили)
def CheckInput(userInput, listOfMoves, table):
    if userInput in listOfMoves:
        return userInput
    else:
        print(PrintTableForMove(table))
        print('Не верный ввод. Повторите!')
        newUserInput = input('Куда ставим?: ')
        return CheckInput(newUserInput, listOfMoves, table)


result = Game(tableForMove)
print(f'Результат игры (игрок,бот) = {result}')
