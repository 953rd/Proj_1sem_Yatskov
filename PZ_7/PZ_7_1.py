# Даны строки S и S0. Проверить, содержиться ли строка S0 в строке S.
# Если содержится вывести True, если не содержится, то вывести False.

S = "AKjl1safdkKAJFijwf34lerj5409"
print("Исходная строка:", S)
S0 = input("Введите строку: ")

if S0 in S:
    print("True")
else:
    print("False")
