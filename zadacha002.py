# Узнав, что ДНК не является случайной строкой,
# только что поступившие в Институт биоинформатики студенты группы
# информатиков предложили использовать алгоритм сжатия,
# который сжимает повторяющиеся символы в строке.

# Кодирование осуществляется следующим образом:
# s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов
# исходной строки заменяются на этот символ и количество его повторений в этой позиции строки.

# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом
# и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

# Sample Input 1:
# aaaabbcaa
# Sample Output 1:
# a4b2c1a2

# Sample Input 2:
# abc
# Sample Output 2:
# a1b1c1


S = input("Введите текст: ")

def Coding (text):
    lists = [text[i] for i in range(len(text))]
    

    return lists


# lists = [text[i] for i in range(len(text))]

# S = input("Введите текст: ")

# def coding(text):
#     count = 1
#     A = ''
#     for i in range(len(text)-1):
#         if text[i] == text[i+1]:
#             count += 1
#         else:
#             A = A + str(count) + text[i]
#             count = 1
#     return A

# def decoding(text):
#     number = ''
#     A = ''
#     for i in range(len(text)):
#         if not text[i].isalpha():
#             number += text[i]
#         else:
#             A = A + text[i] * int(number)
#             number = ''
#     return A

# print(f"Кодирование: {coding(S)}")
# print(f"Декодирование: {decoding(coding(S))}")



# def Coding(code):
#     ls_decoding = ''
#     previous = code[0]
#     for i in code:
#         count = 1
#         if i == previous:
#             count += 1
#         ls_decoding.append(f'{i}{count}')
#         previous = i
#     print(ls_decoding)


# Coding(code)

# ls_decoding = ls_decoding+f'{i}{count}'