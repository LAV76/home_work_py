# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
#
# 5 -> 1 0 1 1 0
# 2

import random

# number_coins = int(input('Введиде количество монет '))
number_coins = random.randint(1, 50)
# coins = []
coins_side = 0
for i in range(number_coins):
    side_coin = random.randint(0, 1)
    # side_coin = int(input('Введиде сторону монеты 1 или 0  '))
    # coins.append(random.randint(0, 1))
    # coins.append(side_coin)
    if side_coin == 0:
        coins_side += 1

print(f'Количество монет, которые нужно перевернуть {coins_side}')
# print(coins)


