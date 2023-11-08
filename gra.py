import tkinter as tk

from tkinter import *

windowstart= tk.Tk()
windowstart.resizable(False, False)
windowstart.title("NaukaSłownictwa - Pingolingo")


window_width = 1000
window_height = 900

# Obliczenie pozycji okna na środku ekranu

screen_width = windowstart.winfo_screenwidth()
screen_height = windowstart.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 6

# Ustawienie pozycji okna
windowstart.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# tlo

bg = tk.PhotoImage(file = "tlo.png")
bg_img = tk.Label(image=bg).place(x=-20, y=0)

# funkcje do przyciskow

def quit():
    windowstart.destroy()

def easy():
    windowstart.destroy()
    from easy import easygame

def medium():
    windowstart.destroy()
    from medium import mediumgame

def medium_hard():
    windowstart.destroy()
    from medhar import medhargame

def hard():
    windowstart.destroy()
    from hard import hardgame

# napisy

Witaj = tk.Label(text="Witaj w Pingolingo!", bg="white")
Witaj.config(font=("Impact", 44))
Witaj.pack()
Pyt_o_poz = tk.Label(text="W jaki poziom chcesz zagrać?", bg="white")
Pyt_o_poz.config(font=("Impact", 33))
Pyt_o_poz.pack()

# przyciski

Easy = tk.Button(text="łatwy", bg="lightgreen", fg="black", height=2, width=5, command=lambda: easy())
Easy.config(font=("Impact", 20), border=10)
Medium = tk.Button(text="średni", bg="lightyellow", fg="black", height=2, width=5, command=lambda: medium())
Medium.config(font=("Impact", 20), border=10)
Medium_Hard = tk.Button(text="średnio-trudny", bg="orange", fg="black", height=2, width=5, command=lambda: medium_hard())
Medium_Hard.config(font=("Impact", 20), border=10)
Hard = tk.Button(text="trudny", bg="red", fg="black", height=2, width=5, command=lambda: hard())
Hard.config(font=("Impact", 20), border=10)
Quit = tk.Button(text="wyjdź", bg="lightblue", fg="black", command=lambda: quit())
Quit.config(font=("Impact", 20), border=10)

Easy.place(x=50, y=400, height=120, width=200)
Medium.place(x=275, y=400, height=120, width=200)
Medium_Hard.place(x=525, y=400, height=120, width=200)
Hard.place(x=750, y=400, height=120, width=200)
Quit.place(x=475, y=825)

windowstart.mainloop()