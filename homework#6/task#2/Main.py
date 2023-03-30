# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

num_min, num_max = sorted(random.sample(range(-20, 21), 2))
arr = [random.randint(-20, 20) for i in range(random.randint(1, 20))]
print(num_min, num_max, arr)
for i in range(len(arr)):
    if num_min <= arr[i] <= num_max:
        print(i, end=' ')



