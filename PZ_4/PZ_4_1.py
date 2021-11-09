# Дано вещественное число A и целое число N (>0).
# Найти A в степени N: AN = AA ... •A (числа A перемножаются N раз).

a = input("Введите число a: ")
while type(a) != float:    # Обработка исключений
    try:
        a = float(a)
    except ValueError:
        print("Введено неверное число!")
        a = input("Введите число a: ")

n = input("Введите число n: ")
while type(n) != int:    # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print("Введено неверное число!")
        a = input("Введите число n: ")
    try:
        while n <= 0:    # Ограничение: n - положительное число
            print("Введено неверное число!")
            a = input("Введите число n: ")
    except TypeError:
        continue

k = 1
an = a
while k < n:    # Пока счетчик меньше n число будет перемножаться само на себя
    an *= a
    k += 1
print(an)