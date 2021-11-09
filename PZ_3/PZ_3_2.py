# Даны три числа. Найти сумму двух наибольших из них.

a = input("Введите 1-ое число: ")
while type(a) != float:  # Обработка исключений
    try:
        a = float(a)
    except ValueError:
        print("Введено не число!")
        a = input("Введите 1-ое число: ")

b = input("Введите 2-ое число: ")
while type(b) != float:  # Обработка исключений
    try:
        b = float(b)
    except ValueError:
        print("Введено не число!")
        b = input("Введите 2-ое число: ")

c = input("Введите 3-е число: ")
while type(c) != float:  # Обработка исключений
    try:
        c = float(c)
    except ValueError:
        print("Введено не число!")
        c = input("Введите 3-е число: ")

if (a > b > c):
    print("Сумма двух наибольших чисел равна:", a + b)
elif (a > c > b):
    print("Сумма двух наибольших чисел равна:", a + c)
else:
    print("Сумма двух наибольших чисел равна:", b + c)