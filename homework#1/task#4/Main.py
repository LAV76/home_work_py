# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один
# разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Ведите первую сторону шоколадки: '))
m = int(input('Ведите вторую сторону шоколадки: '))
k = int(input('Сколько долек нам нужно: '))

if (k < n * m) and ((k % n == 0) or (k % m == 0)):
    print(f'n: {n}, m: {m}, k: {k} yes')
else:
    print(f'n: {n}, m: {m}, k: {k} no')