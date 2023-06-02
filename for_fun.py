from tkinter import *
from random import randint

root = Tk()


def on_enter(e):
    x = randint(50, 450)
    y = randint(50, 300)
    btn_yes.place_configure(x=x, y=y)


root.title("Зарплата банкира")
root.geometry("500x350")

label = Label(text='Хотите увеличить зарплату?', font=('Arial', 18))
label.pack()

btn_yes = Button(text='Да', font=('Arial', 15))
btn_no = Button(text='Нет', font=('Arial', 15))
btn_yes.place(x=100, y=150)
btn_no.place(x=350, y=150)

btn_yes.bind("<Enter>", on_enter)

root.mainloop()
