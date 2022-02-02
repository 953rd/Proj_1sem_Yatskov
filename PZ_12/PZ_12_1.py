import tkinter
from tkinter import *
from tkinter import ttk

root = Tk()
var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
root.title('Регистрация')
root.geometry('900x520')

label1 = Label(root, text='Регистрационная страница Клуба любителей'
                          ' фантастики', font='Arial 20')
label1.place(x=10, y=10)

label2 = Label(root, text='Заполнив анкету, вы сможете пользоваться нашей'
                          ' электронной библиотекой', font='Arial 12')
label2.place(x=10, y=60)

label3 = Label(root, text='Введите регистрационное имя:',font='Arial 12')
label3.place(x=10, y=100)
text1 = Text(root, height=1, width=25, font='Arial 12')
text1.place(x=250, y=100)

label4 = Label(root, text='Введите пароль:', font='Arial 12')
label4.place(x=10, y=125)
text2 = Text(root, height=1, width=25, font='Arial 12')
text2.place(x=250, y=125)

label5 = Label(root, text='Подтвердите пароль:', font='Arial 12')
label5.place(x=10, y=150)
text3 = Text(root, height=1, width=25, font='Arial 12')
text3.place(x=250, y=150)

label6 = Label(root, text='Ваш возраст:', font='Arial 12')
label6.place(x=10, y=200)
rbutton1 = Radiobutton(root, text='До 20', variable=var, value=1)
rbutton1.place(x=115, y=200)
rbutton2 = Radiobutton(root, text='20-30', variable=var, value=2)
rbutton2.place(x=175, y=200)
rbutton3 = Radiobutton(root, text='30-50', variable=var, value=3)
rbutton3.place(x=235, y=200)
rbutton4 = Radiobutton(root, text='Старше 50', variable=var, value=4)
rbutton4.place(x=295, y=200)

label7 = Label(root, text='На каких языках читаете:', font='Arial 12')
label7.place(x=10, y=250)
check1 = Checkbutton(root, text='русский', variable=var1, onvalue=1,
                     offvalue=0)
check1.place(x=200, y=250)
check2 = Checkbutton(root, text='английский', variable=var2, onvalue=1,
                     offvalue=0)
check2.place(x=270, y=250)
check3 = Checkbutton(root, text='французский', variable=var3, onvalue=1,
                     offvalue=0)
check3.place(x=360, y=250)
check4 = Checkbutton(root, text='немецкий', variable=var4, onvalue=1,
                     offvalue=0)
check4.place(x=460, y=250)
label8 = Label(root, text='Какой формат данных является для Вас предпочтительным',
               font='Arial 12')
label8.place(x=10, y=300)
listbox1 = Listbox(root, height=2, width=15, selectmode=SINGLE)
list1 = [u"HTML", u"Plain text"]
for i in list1:
    listbox1.insert(END, i)
listbox1.place(x=10, y=325)

label9 = Label(root,text='Ваши любимые авторы:', font='Arial 12')
label9.place(x=10, y=375)
text4 = Text(root, height=3, width=50, font='Arial 12')
text4.place(x=10, y=400)

button1 = Button(root, text='OK', width=3, height=1, font='Arial 12')
button1.place(x=10, y=475)
button2 = Button(root, text='Отменить', width=7, height=1, font='Arial 12')
button2.place(x=60, y=475)
root.mainloop()