import tkinter
from tkinter import ttk


window = tkinter.Tk()
window.title('Hello world app')
window.geometry('200x200')


def say_hello() -> None:
    print("Привет!")


hello_button = ttk.Button(window, text="Say hello", command=say_hello)
hello_button.pack()

# Здесь приложение блокируется
window.mainloop()
