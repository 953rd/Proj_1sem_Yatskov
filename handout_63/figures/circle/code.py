def circle_perimetr(d_r=5):
    a = input("Введите радиус окружности: ")
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            a = d_r
    pi = 3.14
    p = 2*pi*a
    print('Длина окружности = ', p)


def circle_area(d_r=5):
    a = input("Введите радиус окружности: ")
    while type(a) != int:
        try:
            a = int(a)
        except ValueError:
            a = d_r
    pi = 3.14
    s = pi*a**2
    print("Площадь окружности: ", round(s, 2))
