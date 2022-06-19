import tkinter
from tkinter import *
from tkinter import messagebox

# class TextField():
def display_code():
    x = code.get()
    print(x)

root = Tk()
root.title("Код пользователя")
root.geometry('400x300')
 
code = StringVar()
 
code_label = Label(text="Введите Ваш код:")
 
code_label.grid(row=0, column=0, sticky="w")
 
code_entry = Entry(textvariable=code, width=30)
 
code_entry.grid(row=0,column=1, padx=5, pady=5)
 
 
message_button = Button(text="Отправить", command=display_code)
message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")
 
root.mainloop()