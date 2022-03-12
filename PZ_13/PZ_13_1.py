import random

n = input("Введите размер последовательности: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Введен неверный размер.")
        n = input("Введите размер последовательности: ")

a = [random.randint(1, 10) for i in range(n)]
print("Исходная последовательность:", a)
c = 0
s = 0
b = []
for i in a:
    if i % 2 == 0:
        i *= i
        b.append(i)
        s += i
        c += 1
print("Итоговая последовательность:", b)
print("Сумма элементов итоговой последовательности:", c)
print("Среднее арифметическое итоговой последовательности:", s/c)
