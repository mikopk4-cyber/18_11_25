import os
import shutil
from threading import Thread
from tkinter import Tk, messagebox, filedialog
from tkinter.ttk import Frame, Label, Entry, Button, Style
import tkinter as tk
import tkinter.font as tkfont



def copy_file(source_file_path, copy_file_path):
    try:
        shutil.copy(source_file_path, copy_file_path)
        messagebox.showinfo( f'Well Done!!!',f'Has been saved here {copy_file_path}')
    except Exception as e:
        messagebox.showerror("Error!" , str(e))




    Thread(target=copy_file, args=(source_file_path, copy_file_path)).start()

def choose_file(text_widget):
    file_path = filedialog.askopenfilename(title="Choose a file")
    text_widget.delete(0, tk.END)
    text_widget.insert(0, file_path)

def choose_dir(text_widget_1, text_widget_2):
    file_path = filedialog.askdirectory(title="Choose a directory")
    file_path = f"{file_path}/copy_{os.path.basename(text_widget_1.get())}"
    text_widget_2.delete(0, tk.END)
    text_widget_2.insert(0, file_path)


# Вікно
root = Tk()
root.title("Coping Files")
root.geometry("850x210")
root.resizable(True, True)
# Рамка всередині вікна
frame = Frame(root, padding=12)
frame.pack(fill="both", expand=True)
# Шрифт
FONT = tkfont.Font(family="Segoe UI", size=12)
style = Style()
style.configure("TButton", font=FONT)
style.configure("TLabel", font=FONT)
# Підпис
label1 = Label(frame, text="You're current file:")
label1.grid(row=0, column=0, sticky="w", pady=(0, 6))
# Текстове поле 1
entry1 = Entry(frame, width=60, font=FONT)
entry1.grid(row=1, column=0, sticky="w", padx=(0, 6))
# Кнопка 1
btn1 = Button(frame, text="     Choose the file     ", command=lambda: choose_file(entry1))
btn1.grid(row=1, column=2, sticky="e")
# Підпис
label2 = Label(frame, text="Road to another directory:")
label2.grid(row=2, column=0, sticky="w", pady=(0, 6))
# Текстове поле 2
entry2 = Entry(frame, width=60, font=FONT)
entry2.grid(row=3, column=0, sticky="w", padx=(0, 6))
# Кнопка 2
btn2 = Button(frame, text="Choose the directory", command=lambda: choose_dir(entry1, entry2))
btn2.grid(row=3, column=2, sticky="e")
# Кнопка 3
btn3 = Button(frame, text="Copy", command=lambda: copy_file(entry1.get(), entry2.get()))
btn3.grid(row=4, column=0, sticky="w", pady=(24, 0))
root.mainloop()