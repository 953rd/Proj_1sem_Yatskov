# Сгенерировать матрицу, в которой каждые нечетные
# элементы заменяются на 0.

import random

n = int(input('Введите количество столбцов: '))
m = int(input('Введите количество строк: '))
matr = [[random.randint(1, 10) for x in range(n)]for y in range(m)]
print()
print('Исходная матрица:')
for v in matr:
    print(v)
print()
for i in range(m):
    for j in range(n):
        if matr[i][j] % 2 != 0:
            matr[i][j] = 0
print('Матрица после замены нечетных элементов:')
for v in matr:
    print(v)

