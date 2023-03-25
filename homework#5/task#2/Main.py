# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

def math_sum(a: int, b: int) -> int:
    return math_sum(a+1, b-1) if b > 0 else a

print(math_sum(3, 3))