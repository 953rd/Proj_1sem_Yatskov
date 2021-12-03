# Дан список A размера N. Сформировать новый список B того же размера по
# следующему правилу: элемент Bk равен среднему арифметическому элементов
# списка A с номерами от 1 до K.

import random

n = input("Введите размер списка: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Введено неверное значение.")
        N = input("Введите размер списка: ")

a, b = [random.randint(0, 100) for i in range(n)], []
print("Исходный список: ", a)
t = 1
i = 1
while t < n:
    s = 0
    while i < n:
        s += a[i]
        i += 1
        b.append(s / (n - t))
        t += 1
        i = t
print("Конечный список: ", b)
