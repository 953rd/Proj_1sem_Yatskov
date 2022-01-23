# Из предложенного текстового файла (text18-31.txt) вывести на экран
# его содержимое, количество символов, принадлежащих к группе букв.
# Сформировать новый файл, в который поместить строку наименьшей длины.

f1 = open("18-31.txt", "r", encoding="utf8")
p = ["!", ";", ":", "?", ",", ".", "/", "\\", "-", "_", '…', '—', ' ', '\n']
L = 0
s = []
v = str()

rf = f1.read()
print('Содержимое документа: ')
print()
print(rf)

for si in rf:
    for i in p:
        if i in si:
            si = si.replace(i, '')
    v += si
print()
print('Количество буквенных символов в документе: ', len(v)-1)

f1.close()

f2 = open("tmss.txt", "w", encoding="utf8")

for i in open("18-31.txt", "r", encoding="utf8"):
    s.append(len(i))
t = min(s)
for i in open("18-31.txt", "r", encoding="utf8"):
    if t == len(i):
        f2.write(i)

f2.close()