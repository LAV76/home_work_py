# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны
# N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

# num = int(input('Введиде любое число от -20 до 20 '))
# arr_len = int(input('Введиде длину массива '))
list = []
count = 0
n = random.randint(1, 20)
x = random.randint(1, 50)
list.append(random.randint(1, 50))
min = abs(x - list[0])
for i in range(1, n):
    list.append(random.randint(1, 50))
    count = abs(x - list[i])
    if count < min:
         min = count
         num = list[i]
print(f'Наиболее близкиое число  {num} к задоному числу {x} в массиве: ')
print(list)
