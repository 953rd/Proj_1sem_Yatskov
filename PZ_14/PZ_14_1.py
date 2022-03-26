# Из исходного текстового файла (price.txt) выбрать все цены.
# Подсчитать количество полученных элементов.

import re

c = 0
p = re.compile(r"[0-9]+.[руб.]+.[0-9]+.[коп.]+")
with open('price.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print("Выбранные цены:")
print(p.findall(text))
print("Количество элементов", len(p.findall(text)))

