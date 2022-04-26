import math

def triangle_perimetr(d_a=7, d_b=2, d_c=8):
    a = input("Введите сторону треугольника: ")
    b = 0
    c = 0
    while type(a) != int:
        try:
            a = int(a)
            if a == int(a):
                b = int(input("Введите сторону треугольника: "))
                c = int(input("Введите сторону треугольника: "))
        except ValueError:
            a = d_a
            b = d_b
            c = d_c
    p = a + b + c
    print('Периметр треугольника = ', p)


def triangle_area(d_a=7, d_b=2, d_c=8):
    a = input("Введите сторону треугольника: ")
    b = 0
    c = 0
    while type(a) != int:
        try:
            a = int(a)
            if a == int(a):
                b = int(input("Введите сторону треугольника: "))
                c = int(input("Введите сторону треугольника: "))
        except ValueError:
            a = d_a
            b = d_b
            c = d_c
    pp = (a + b + c) / 2
    s = math.sqrt(abs(pp*(pp-a)*(pp-b)*(pp-c)))
    print("Площадь теугольника = ", round(s, 2))
