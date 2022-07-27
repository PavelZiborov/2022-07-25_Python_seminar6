# 41. Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

#     *Пример:*

#     2+2 => 4;

#     1+2*3 => 7;

#     1-2*3 => -5;

#     Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:*

#     1+2*3 => 7;

#     (1+2)*3 => 9;


import re

text = '(100 + 10) * 5' # 550
#       01234


def StringToList(text):
    tempList = []
    temp = ''
    for i in range(0,len(text)):
        # склейка цифр
        if text[i].isdigit() and not text[i-1].isdigit(): 
            temp = text[i]
            try:
                for j in range(1,100):
                    temp = temp + str(int(text[i+j]))
            except:
                tempList.append(temp)
                temp = ''
        elif text[i] == '+' or text[i] == '-' or text[i] == '*' or text[i] == '/' or text[i] == '(' or text[i] == ')':
            tempList.append(text[i])

    resultList = []
    for i in tempList:
        try:
            resultList.append(int(i))
        except:
            resultList.append(i)

    return resultList


def CaltulateList(list):
    temp = 0
    # Умножение
    while '*' in list:
        temp = list[list.index('*')-1] * list[list.index('*')+1]
        list.insert(list.index('*')-1, temp)
        list.pop(list.index('*')-1)
        list.pop(list.index('*')+1)
        list.pop(list.index('*'))
    # Сложение
    while '+' in list:
        temp = list[list.index('+')-1] + list[list.index('+')+1]
        list.insert(list.index('+')-1, temp)
        list.pop(list.index('+')-1)
        list.pop(list.index('+')+1)
        list.pop(list.index('+'))
    # Вычитание
    while '-' in list:
        temp = list[list.index('-')-1] - list[list.index('-')+1]
        list.insert(list.index('-')-1, temp)
        list.pop(list.index('-')-1)
        list.pop(list.index('-')+1)
        list.pop(list.index('-'))   


    return list



ListToCalculate = StringToList(text)
print(ListToCalculate)
# print(CaltulateList(ListToCalculate))
