# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# # круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# # каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# # Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# # выросло различное число ягод – на i-ом кусте выросло ai
# #  ягод.
# # В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# # Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# # Собирающий модуль за один заход, находясь непосредственно перед некоторым
# # кустом, собирает ягоды с этого куста и с двух соседних с ним.
# # Напишите программу для нахождения максимального числа ягод, которое может
# # собрать за один заход собирающий модуль, находясь перед некоторым кустом
# # заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

import random

# n = int(input('Введиде кол-во кустов '))
n = random.randint(1, 10)
i = 0
numbe_berries = list()
while i < n:
    # numbe_berries.append(int(input(f'Введиде кол-во ягод на {i + 1} кусте ')))
    numbe_berries.append(random.randint(1, 5))
    i +=1
sum = list()
for i in range(len(numbe_berries) - 1):
    sum.append(numbe_berries[i-1] + numbe_berries[i] + numbe_berries[i+1])
sum.append(numbe_berries[0] + numbe_berries[-1] + numbe_berries[-2])

print(max(sum))
