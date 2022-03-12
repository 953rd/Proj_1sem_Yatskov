import random

x = 0
z = 0
a = []
b = []
f1 = open("p.txt", "w", encoding="utf8")
for i in range(10):
    a.append(random.randint(1,10))
    f1.write(str(a[i]))
    f1.write(" ")
    x += 1
f1.close()

f2 = open("o.txt", "w", encoding="utf8")
for i in range(10):
    b.append(random.randint(-10,-1))
    f2.write(str(b[i]))
    f2.write(" ")
    z += 1
f2.close()

f1 = open("p.txt")
s = f1.read()

f2 = open("o.txt")
q = f2.read()

g = a + b
c = s + q
k = x + z

f3 = open("i.txt", "w", encoding="utf8")
f3.write("Элементы первого и втогрого файлов: ")
f3.write(str(c))
f3.write("\n")
f3.write("Количество элементов первого и второго фалов: ")
f3.write(str(k))
f3.write("\n")
f3.write("Элементы первой трети: ")
for i in range(k//3):
    f3.write(str(g[i]))
    f3.write(" ")
f3.write("\n")
f3.write("Минимальный элемент первой трети: ")
f3.write(str(min(g[:k//3])))
