# 41. Создайте программу для игры в "Крестики-нолики".

from random import Random, random


table = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
tableForMove = [['0', '1', '2', '  1'], ['3', '4', '5', '  2'], ['6', '7', '8', '  3'], ['a', 'b', 'c', ' ']]


def PrintTable(list):
    for i in range(0, len(list[0])):
        print(f'{list[i][0]} | {list[i][1]} | {list[i][2]}')
        if i != len(list[0])-1:
            print('---------')
        else: continue


def PrintTableForMove(list):
    for i in range(0, len(list)):
        print(f'{list[i][0]} | {list[i][1]} | {list[i][2]} {list[i][3]}')
        if i != 1 or i != 3:
            print('---------')
        else: continue


# генерируем i,j
# while pole[i][j] != '-':
#   генерируем i,j заново

def Igra (table, Move):
    moves = 0
    while moves < 10:

        Move = int(input())
        if Move == '0 0': table[0][0] == '0'
        elif Move == '0 X': table[0][0] == 'X'
        elif Move == '1 0': table[0][1] == '0'
        elif Move == '1 X': table[0][1] == 'X'
        elif Move == '2 0': table[0][2] == '0'
        elif Move == '2 X': table[0][2] == 'X'
        elif Move == '3 0': table[1][0] == '0'
        elif Move == '3 X': table[1][0] == 'X'
        elif Move == '4 0': table[1][1] == '0'
        elif Move == '4 X': table[1][1] == 'X'
        elif Move == '5 0': table[1][2] == '0'
        elif Move == '5 X': table[1][2] == 'X'
        elif Move == '6 0': table[2][0] == '0'
        elif Move == '6 X': table[2][0] == 'X'
        elif Move == '7 0': table[2][1] == '0'
        elif Move == '7 X': table[2][1] == 'X'
        elif Move == '8 0': table[2][2] == '0'
        elif Move == '8 X': table[2][2] == 'X'
        else: print('Ошибка ввода')

    return table

PrintTableForMove(tableForMove)
# PrintTable(table)
