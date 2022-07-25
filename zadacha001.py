# 41. Создайте программу для игры в "Крестики-нолики".

from random import Random, random


table = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
tableForMove = [['0', '1', '2'], ['3', '4', '5'], ['6', '7', '8']]

def PrintTable(list):
    for i in range(0, len(list[0])):
        print(f'{list[i][0]} | {list[i][1]} | {list[i][2]}')
        if i != len(list[0])-1:
            print('---------')
        else: continue

# генерируем i,j
# while pole[i][j] != '-':
#   генерируем i,j заново


print(PrintTable(table))
print(PrintTable(tableForMove))

def Igra (table, firstMove):
    moves = 0
    while moves < 10:
        nextMove = firstMove
        botsMove = int(input())
        if botsMove == '0 0': table[0][0] == '0'
        elif botsMove == '0 X': table[0][0] == 'X'
        elif botsMove == '1 0': table[0][1] == '0'
        elif botsMove == '1 X': table[0][1] == 'X'
        elif botsMove == '2 0': table[0][2] == '0'
        elif botsMove == '2 X': table[0][2] == 'X'
        elif botsMove == '3 0': table[1][0] == '0'
        elif botsMove == '3 X': table[1][0] == 'X'
        elif botsMove == '4 0': table[1][1] == '0'
        elif botsMove == '4 X': table[1][1] == 'X'
        elif botsMove == '5 0': table[1][2] == '0'
        elif botsMove == '5 X': table[1][2] == 'X'
        elif botsMove == '6 0': table[2][0] == '0'
        elif botsMove == '6 X': table[2][0] == 'X'
        elif botsMove == '7 0': table[2][1] == '0'
        elif botsMove == '7 X': table[2][1] == 'X'
        elif botsMove == '8 0': table[2][2] == '0'
        elif botsMove == '8 X': table[2][2] == 'X'
        else: print('Ошибка ввода')

    return table
