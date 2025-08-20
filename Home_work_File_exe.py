from tkinter import *
from tkinter import filedialog as fd
import os
import shutil

window = Tk()
window.withdraw()

dir = fd.askdirectory(title="Выберите папку для копирования")
if dir:
    new_dir = dir + "_new"
    if not os.path.exists(new_dir):
        try:
            shutil.copytree(dir, new_dir)
            print(f"Все содержимое из {dir} скопировано в {new_dir}")
        except Exception as e:
            print(f"Ошибка при копировании: {e}")
    else:
        print(f"Папка {new_dir} уже существует.")
else:
    print("Папка не была выбрана.")


window.mainloop()