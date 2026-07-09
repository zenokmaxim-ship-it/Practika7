from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Система бесперебойного питания")
root.geometry("400x250")

notebook = ttk.Notebook(root)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Управление")
notebook.add(tab2, text="Информация")
notebook.pack(expand=True, fill="both")

power = BooleanVar(value=True)
generator = BooleanVar(value=True)

def off_power():
    power.set(False)
    status.config(text="Внешнее питание отключено")

Button(tab1, text="Отключить внешнее питание",
       command=off_power).pack(pady=20)

Checkbutton(tab1,
            text="Генератор исправен",
            variable=generator).pack()

status = Label(tab1, text="Внешнее питание включено")
status.pack(pady=20)

Label(tab2, text="Система бесперебойного питания").pack(pady=30)

root.mainloop()