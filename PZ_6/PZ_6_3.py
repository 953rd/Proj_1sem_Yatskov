# Дан список размера N, все элементы которого, кроме последнего,
# упорядочены по возрастанию. Сделать список упорядоченным,
# переместив последний элемент на новую позицию.

import random

n = input("Введите размер списка: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Введено неверное значение.")
        n = input("Введите размер списка: ")

L = [random.randint(0, 100) for i in range(n-1)]
L.sort(key=None, reverse=False)
L.append(random.randint(0, 100))
print("Исходный список: ", L)
L.sort(key=None, reverse=False)
print("Конечный спискок: ", L)
