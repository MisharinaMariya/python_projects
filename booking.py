
from tkinter import *
from tkinter import messagebox as mb


def book_seat(event=None):
    s = seat_entry.get()
    try:
        if seats[s]=='Свободно':
            seats[s] = 'Забронировано'
            update_canwas()
            mb.showinfo("Успех", f'Место {s} Успешно забронировано')
        else:
            mb.showinfo('Ошибка', f'Место {s} уже забронировано или не существует')
    except KeyError:
        mb.showinfo('Ошибка', f'Место {s} не существует')


def cancel_booking(event=None):
    s = cancel_seat_entry.get()
    try:
        if seats[s]=='Забронировано':
            seats[s] = 'Свободно'
            update_canwas()
            mb.showinfo("Успех", f'Бронь места {s} успешно отменена')
        else:
            mb.showinfo('Ошибка', f'Место {s} не забронировано или не существует')
    except KeyError:
        mb.showinfo('Ошибка', f'Место {s} не существует')


def update_canwas():
    canvas.delete('all')
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = 'green' if status == 'Свободно' else 'red'
        canvas.create_rectangle(x, y, x+30, y+30, fill=color)
        canvas.create_text(x+15, y+15, text=seat)

def add_description():
    x1 = 120
    y1= 75
    canvas.create_rectangle(60, 60, 90, 90, fill='green')
    canvas.create_rectangle(160, 60, 190, 130, fill='red')
    canvas.create_text(x1,y1, text="Свободно")
    canvas.create_text(x1+95, y1, text="Занято")

window = Tk()
window.title("Бронирование мест")
window.geometry('400x400')


canvas = Canvas(width=400, height=80)
canvas.pack(pady=10)


seats = {f'Б{i}': 'Свободно' for i in range(1,10)}
update_canwas()
add_description()


seat_entry = Entry()
seat_entry.pack(pady=10)
seat_entry.focus()
seat_entry.bind('<Return>', book_seat)

Button(text='Забронировать место', command=book_seat).pack(pady=10)

cancel_seat_entry = Entry()
cancel_seat_entry.pack(pady=10)
cancel_seat_entry.bind('<Return>', cancel_booking)

Button(text='Отменить бронь', command=cancel_booking).pack(pady=10)

window.mainloop()