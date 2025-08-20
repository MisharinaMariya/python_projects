from tkinter import *
from tkinter import filedialog as fd
import os
import  shutil
# Создание и скрытие основного окна
window = Tk()
window.withdraw()
# Открытие диалогового окна для выбора папки
direct = fd.askdirectory(title="Выберите папку c форматами .doc и .docx")
# Создание новой папки с суффиксом "_new"
if direct:
    new_dir = direct + "_new"
    if not os.path.exists(new_dir): os.makedirs(new_dir)
    # Перебор файлов в исходной папке
    for file in os.listdir(direct):
        if file.lower().endswith((".doc", ".docx")):
            source_file = os.path.join(direct, file)
            destination_file = os.path.join(new_dir, file)
            try:
                shutil.move(source_file, destination_file)
                print(f"Файл {file} перемещен.")
            except Exception as e:
                print(f"Ошибка при перемещении файла {file}: {e}")
    print(f"Все файлы из {direct} скопированы в {new_dir}")
else:
        print("Папка не была выбрана.")
window.mainloop()