# Из заданной строки отобразить только символы нижнего регистра.
# Использовать библиотеку string. Строка 'In PyCharm,
# you can specify third-party standalone applications and run
# them as External Tools'

import string

fs = 'In PyCharm, you can specify third-party standalone' \
     ' applications and run them as External Tools'
ps = list()
for i in fs:
    for d in string.ascii_lowercase:
        if i == d:
            ps.append(i)
print(fs)
print(" ".join(ps))