# Сгенерировать словарь вида {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36},
# Удалить из него второй и третий элементы. Отобразить исходный и
# получившийся словарь. Использовать for, range.

d1 = {i: i ** 2 for i in range(7)}
print(d1)
d1.pop(1)
d1.pop(2)
print(d1)
