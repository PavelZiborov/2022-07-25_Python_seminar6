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


# Метод, который преобразовывает текст в список
def StringToList(text):
    text = ' ' + text
    tempList = []
    temp = ''
    for i in range(0, len(text)):
        # склейка цифр
        if text[i].isdigit() and not text[i-1].isdigit():
            temp = text[i]
            try:
                for j in range(1, 100):
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

# Метод который считает + - * / 
def CalculateSimpleOperations(lst): 
    temp = 0
    # Умножение
    while '*' in lst:
        temp = lst[lst.index('*')-1] * lst[lst.index('*')+1]
        lst.insert(lst.index('*')-1, temp)
        lst.pop(lst.index('*')-1)
        lst.pop(lst.index('*')+1)
        lst.pop(lst.index('*'))
    # Деление
    while '/' in lst:
        temp = lst[lst.index('/')-1] / lst[lst.index('/')+1]
        lst.insert(lst.index('/')-1, temp)
        lst.pop(lst.index('/')-1)
        lst.pop(lst.index('/')+1)
        lst.pop(lst.index('/'))
    # Сложение
    while '+' in lst:
        temp = lst[lst.index('+')-1] + lst[lst.index('+')+1]
        lst.insert(lst.index('+')-1, temp)
        lst.pop(lst.index('+')-1)
        lst.pop(lst.index('+')+1)
        lst.pop(lst.index('+'))
    # Вычитание
    while '-' in lst:
        temp = lst[lst.index('-')-1] - lst[lst.index('-')+1]
        lst.insert(lst.index('-')-1, temp)
        lst.pop(lst.index('-')-1)
        lst.pop(lst.index('-')+1)
        lst.pop(lst.index('-'))
    return lst[0]

# Метод который считает с учетом скобок
def Calculator(lst):
    tempList = []
    if '(' in lst or ')' in lst:
        # переворачивает список что бы найти последнее вхождение
        revers_lst = lst[::-1].index('(')
        index_of_first_parenthesis = len(lst) - 1 - revers_lst
        index_of_second_parenthesis = lst.index(')', index_of_first_parenthesis)
        # добавляет в tempList элементы между скобками, вычисляет, а затем удаляет их
        for i in range(index_of_first_parenthesis+1, index_of_second_parenthesis):
            tempList.append(lst[i])
        lst.insert(index_of_first_parenthesis, CalculateSimpleOperations(tempList))
        del lst[index_of_first_parenthesis+1:index_of_second_parenthesis+2]
        # рекурсия позволяет вычислить и удалить все скобки
        return Calculator(lst)
    else:
        return CalculateSimpleOperations(lst)


text = input('Ведите выражение которое хотите посчитать: ')  # Ответ 11
ListToCalculate = StringToList(text)
result = Calculator(ListToCalculate)
print(f'{text} = {result}')