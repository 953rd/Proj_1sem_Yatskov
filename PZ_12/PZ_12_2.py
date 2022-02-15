import tkinter
from tkinter import *
from tkinter import ttk


def triangle(event):
    t = 0

    n1 = int(num1.get())
    n2 = int(num2.get())
    n3 = int(num3.get())

    if n1 == n2 or n1 == n3 or n2 == n3:
        t = t + 1
    else:
        t = 0

    if t == 1:
        positive['text'] = " Треугольник равнобедренный "
    else:
        negative['text'] = " Треугольник неравнобедренный "


root = Tk()
root.title('Треугольник')
root.geometry('500x200')

label1 = Label(root, text="Введите длину 1-й стороны: ", font='Arial 12')
label1.place(x=25, y=20)
num1 = Entry()
num1.place(x=275, y=25)

label2 = Label(root, text="Введите длину 2-й стороны: ", font='Arial 12')
label2.place(x=25, y=45)
num2 = Entry()
num2.place(x=275, y=50)

label3 = Label(root, text="Введите длину 3-й стороны: ", font='Arial 12')
label3.place(x=25, y=70)
num3 = Entry()
num3.place(x=275, y=75)

button1 = Button(text="Обработать")
button1.place(x=200, y=115)

positive = Label()
positive.place(x=150, y=150)

negative = Label()
negative.place(x=150, y=150)

button1.bind('<Button-1>', triangle)

root.mainloop()
