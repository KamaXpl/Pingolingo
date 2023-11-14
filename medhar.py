import tkinter as tk
from tkinter import *
import mysql.connector

MySQL = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'naukaslownictwa')
cursor = MySQL.cursor()

cursor.execute("SELECT * FROM medhar ORDER BY RAND() LIMIT 20")
words = cursor.fetchall()

MySQL.close()

medhargame = tk.Tk()
medhargame.resizable(False, False)
medhargame.title("NaukaSłownictwa - Pingolingo, poziom: średnio-trudny")
medhargame.config(background="white")

window_width = 1000
window_height = 900
screen_width = medhargame.winfo_screenwidth()
screen_height = medhargame.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 6
medhargame.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

bg = tk.PhotoImage(file = "tlo.png")
bg_img = tk.Label(image=bg).place(x=-20, y=0)

def info():
    infor = tk.Toplevel()
    infor.config(bg="white")
    infor.title("Informacje o poziomie średnio-trudnym - Pingolingo")
    screen_width = infor.winfo_screenwidth()
    screen_height = infor.winfo_screenheight()
    window_width = 1000
    window_height = 650
    x1 = (screen_width - window_width) // 2
    y1 = (screen_height - window_height) // 6
    infor.geometry('{}x{}+{}+{}'.format(window_width, window_height, x1, y1))
    img1 = tk.PhotoImage(file = "tloinfo.png")
    img2 = tk.Label(infor, image=img1)
    inf = tk.Label(infor, text="Poziom średnio-trudny informacje")
    inf.config(font=("Impact", 26), fg="darkblue", bg="white")
    inf1 = tk.Label(infor, text="Twoim zadaniem jest odpowiedzenie na 20 pytań. \n W każdym słowie brakuje jakiejś samogłoski. \n Czy dasz radę zgadnąć jakiej? \n Powodzenia!")
    inf1.config(font=("Impact", 22), bg="white")
    inf.pack()
    inf1.pack()
    img2.pack()
    infor.mainloop()

index = 0
points = 0
mistakes = 0

# funkcja do sprawdzania odpowiedzi + do liczenia punktów i pomyłek

def check_answer():
    answer = entry.get()
    entry.delete(0, tk.END)
    global index 
    global points
    global mistakes
    if answer.lower() == words[index][3].lower():
        message_label.config(text=f"Brawo! To jest poprawna odpowiedź. Pełne słowo brzmi {words[index][1]}", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][3]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
    else:
        show_result()

# aktualizowanie pytan + liczby punktow + liczby pomyłek

def update_gui():
    
    question_label.config(text=f"Wpisz do słowa prawidłową literę: \n {words[index][2]}?")
    
    score_label.config(text=f"Punkty: {points} | Pomyłki: {mistakes}")

    translating_label.config(text=f"Tłumaczenie tego słowa to: {words[index][0]} ")

# fukcja aby po wygraniu/przegraniu zagrac w inny level

def new_game():
    medhargame.destroy()
    from gra import windowstart

# pokazywanie wyniku

def show_result():
    for widget in medhargame.winfo_children():
        widget.destroy()
    if points >= 15:
        done = tk.PhotoImage(file="welldone.png")
        result_label = tk.Label(medhargame, text=f"Gratulacje! Uzyskałeś/aś aż {points} punktów na 20 możliwych. \n Świetnie ci poszło, pingwin Pingo jest z ciebie dumny! Oby tak dalej! \n Well done my friend! Penguin Pingo is really proud of you!", font=("Arial", 24), bg="white", fg="green")
    else:
        done = tk.PhotoImage(file="nt.png")
        result_label = tk.Label(medhargame, text=f"Szkoda! Uzyskałeś/aś {points} punktów na 20 możliwych. \n Mamy nadzieję, że nastepnym razem pójdzie ci lepiej! \n A jak nie pingwin Pingo ci pomoże!\n Ahh nice try! \n Penguin Pingo hopes that next time you will do better! ", font=("Arial", 24), bg="white", fg="red")
    result_label.pack(pady=20)
    result_img = Label(image=done)
    result_img.pack()
    # wywolanie przycisku by zamknac calkowicie program
    exit_button = tk.Button(medhargame, text="Zakończ", font=("Arial", 18), bg="white", border=10, command=medhargame.destroy)
    exit_button.pack(pady=20)
    # wywolanie przycisku by zagrac w inny level
    newgame_button= tk.Button(medhargame, text="Zagraj w inny poziom trudności", font=("Arial", 18), bg="white", border=10, command=new_game)
    newgame_button.pack(pady=20)
    bg_img = tk.Label(image=bg).pack()
    widget.mainloop()        

# wywoływanie label, button i entry

question_label = tk.Label(medhargame, text="", font=("Impact", 24), bg="white")
question_label.pack(pady=20)

translating_label = tk.Label(medhargame, text="", font=("Impact", 18), bg="white")
translating_label.pack(pady=20)

# wywołanie wpisywania odpowiedzi ~ entry
entry = tk.Entry(medhargame, font=("Arial", 18), width=20)
entry.pack(pady=20)

# wywołanie sprawdzania odpowiedzi ~ przycisk
check_button = tk.Button(medhargame, text="Sprawdź", font=("Impact", 18), bg="white", border=10, command=check_answer)
check_button.pack(pady=20)

# wywoływanie label

message_label = tk.Label(medhargame, text="", font=("Impact", 18), bg="white")
message_label.pack(pady=20)

score_label = tk.Label(medhargame, text="", font=("Impact", 18), bg="white")
score_label.pack(pady=20)


# wywołanie informacje ~ przycisk

Info = tk.Button(text="Informacje", font=("Impact", 18), bg="lightblue", fg="black", border=5, command=lambda: info())
Info.pack(side="bottom")

update_gui()
medhargame.mainloop()
