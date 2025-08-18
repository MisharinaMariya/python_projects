from  tkinter import *
from tkinter import messagebox as mb

def summ():
    s1= e1.get()
    if not s1.isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено число")
        return
    s2= e2.get()
    if not s2.isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return
    s3 = e3.get()
    if not s3.isdigit():
        mb.showerror("Ошибка", "В третье поле должно быть введено число")
        return
    slag_1 = int(s1)
    slag_2 = int(s2)
    slag_3 = int(s3)
    summa = slag_1 + slag_2 + slag_3
    m1['text']= f"{s1}+{s2}+{s3} = {summa}"

def multiply():
    s1 = e1.get()
    s2 = e2.get()
    s3 = e3.get()

    slag_1 = int(s1)
    slag_2 = int(s2)
    slag_3 = int(s3)
    multiply = slag_1 * slag_2 * slag_3
    m1['text'] = f"{s1}*{s2}*{s3} = {multiply}"

    answer = mb.askretrycancel(title="Вопрос",message="Сложить еще 3 числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        m1["text"] = ""
    else:
        window.destroy()

window = Tk()
window.title("Калькулятор")
m = Label(height= 3, text = "Введите 3 числа и нажмите на кнопку для вычисления суммы")
m.pack()
e1= Entry()
e1.pack()
e2= Entry()
e2.pack()
e3= Entry()
e3.pack()

b = Button(text = 'Сложить три числа', command=summ)
b.pack()

b1 = Button(text = 'Умножить три числа', command=multiply)
b1.pack()

m1=Label(height=3)
m1.pack()
window.mainloop()

