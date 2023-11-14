import tkinter as tk
from tkinter import *
import mysql.connector
from PIL import ImageTk,Image
import os
import random

MySQL = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'naukaslownictwa')
cursor = MySQL.cursor()

cursor.execute("SELECT * FROM easy ORDER BY RAND() LIMIT 20")
words = cursor.fetchall()

MySQL.close()

easygame = tk.Tk()
easygame.resizable(False, False)
easygame.title("NaukaSłownictwa - Pingolingo, poziom: łatwy")
easygame.config(background="white")

window_width = 1000
window_height = 900
screen_width = easygame.winfo_screenwidth()
screen_height = easygame.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 6
easygame.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

bg = tk.PhotoImage(file = "tlo.png")
bg_img = tk.Label(image=bg).place(x=-20, y=0)

def info():
    infor = tk.Toplevel()
    screen_width = infor.winfo_screenwidth()
    screen_height = infor.winfo_screenheight()
    window_width = 1000
    window_height = 650
    x1 = (screen_width - window_width) // 2
    y1 = (screen_height - window_height) // 6
    infor.geometry('{}x{}+{}+{}'.format(window_width, window_height, x1, y1))
    img1 = tk.PhotoImage(file = "tloinfo.png")
    img2 = tk.Label(infor, image=img1)
    inf = tk.Label(infor, text="Poziom łatwy informacje - Pingolingo")
    inf.config(font=("Impact", 26), fg="darkblue")
    inf1 = tk.Label(infor, text="Twoim zadaniem jest odpowiedzenie na 20 pytań.\n W każdym pytaniu zostanie wyświetlony obrazek. \n Twoje zadanie polega na zaznaczeniu słowa odpowiadającego \n danemu obrazkowi w języku angielskim sposród 6 odpowiedzi.\n Powodzenia!")
    inf1.config(font=("Impact", 22), bg="white")
    inf.pack()
    inf1.pack()
    img2.pack()
    infor.title("Informacje o poziomie łatwym")
    infor.mainloop()

pyt1 = tk.Label(text="Wybierz prawidłową odpowiedź", bg="white")
pyt1.config(font=("Impact", 33))
pyt1.pack(side=TOP)

index = 0
points = 0
mistakes = 0
      
def check_answer1():
    global points, mistakes, index
    if words[index][1] == words[index][7]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][7]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer2():
    global points, mistakes, index
    if words[index][2] == words[index][7]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][7]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer3():
    global points, mistakes, index
    if words[index][3] == words[index][7]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][7]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer4():
    global points, mistakes, index
    if words[index][4] == words[index][7]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][7]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer5():
    global points, mistakes, index
    if words[index][5] == words[index][7]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][7]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer6():
    global points, mistakes, index
    if words[index][6] == words[index][7]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][7]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def update_answers():
    global index
    answer1_btn.config(text=f"{words[index][1]}", state="active")
    answer2_btn.config(text=f"{words[index][2]}", state="active")
    answer3_btn.config(text=f"{words[index][3]}", state="active")
    answer4_btn.config(text=f"{words[index][4]}", state="active")
    answer5_btn.config(text=f"{words[index][5]}", state="active")
    answer6_btn.config(text=f"{words[index][6]}", state="active")

## wyswietlenie zdjecia z folderu img, jednoczesnie nazwa tego pliku ma zostac wylosowana z bazy danych wraz z odpowiedziami
## nie dziala wczytywanie i wyswietlanie zdjecia po wylosowaniu
def update_gui():
    script_dir = os.path.dirname(__file__)
    rel_path = f"\img\\"
    print("sciezka relatywna: "+rel_path, script_dir)
    abs_file_path = os.path.join(script_dir, rel_path)
    print("ściezka bezwzgledna: ", "..\\"+rel_path)
    current_file = f"{words[index][0]}"
    print("current file: "+"\""+rel_path+current_file)
    adress = "\".."+rel_path+current_file
    print(adress)

    top = Toplevel()
    window_width = 300
    window_height = 300
    x1 = (screen_width - window_width) // 12
    y1 = (screen_height - window_height) // 4
    top.geometry('{}x{}+{}+{}'.format(window_width, window_height, x1, y1))
    imagea = Image.open(f"img\{words[index][0]}")
    ph = ImageTk.PhotoImage(imagea)
    a=Label(top, image=ph)
    a.image = ph
    a.pack()
    

    question_label.config(text=f"Co to jest? \n <---")
    
    score_label.config(text=f"Punkty: {points} | Pomyłki: {mistakes}")

# funkcja aby po wygraniu/przegraniu zagrac w inny level

def new_game():
    easygame.destroy()
    from gra import windowstart

# pokazywanie wyniku
# problem jest w wyswietlaniu zdjec welldone i nt
def show_result():
    for widget in easygame.winfo_children():
        widget.destroy()
    if points >= 15:
        done = tk.PhotoImage(file="welldone.png")
        result_label = tk.Label(easygame, text=f"Gratulacje! Uzyskałeś/aś aż {points} punktów na 20 możliwych. \n Świetnie ci poszło, pingwin Pingo jest z ciebie dumny! Oby tak dalej! \n Well done my friend! Penguin Pingo is really proud of you!", font=("Arial", 24), bg="white", fg="green")
        result_label.pack(pady=20)
        result_img = tk.Label(image=done)
        result_img.pack()
    else:
        done = tk.PhotoImage(file="nt.png")
        result_label = tk.Label(easygame, text=f"Szkoda! Uzyskałeś/aś {points} punktów na 20 możliwych. \n Mamy nadzieję, że nastepnym razem pójdzie ci lepiej! \n A jak nie pingwin Pingo ci pomoże!\n Ahh nice try! \n Penguin Pingo hopes that next time you will do better! ", font=("Arial", 24), bg="white", fg="red")
        result_label.pack(pady=20)
        result_img = tk.Label(image=done)
        result_img.pack()
   
    # wywolanie przycisku by zamknac calkowicie program
    exit_button = tk.Button(easygame, text="Zakończ", font=("Arial", 18), bg="white", border=10, command=easygame.destroy)
    exit_button.pack(pady=20)
    # wywolanie przycisku by zagrac w inny level
    newgame_button= tk.Button(easygame, text="Zagraj w inny poziom trudności", font=("Arial", 18), bg="white", border=10, command=new_game)
    newgame_button.pack(pady=20)
    bg_img = tk.Label(image=bg).pack()
    

# wywoływanie label i button do odpowiedzi


question_label = tk.Label(easygame, text="", font=("Impact", 24), bg="white")
question_label.pack(pady=20)

answer1_btn = tk.Button(text=f"{words[index][1]}", command=check_answer1, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), border=10)
answer1_btn.place(x= 250, y= 300)
answer2_btn = tk.Button(text=f"{words[index][2]}", command=check_answer2, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), border=10)
answer2_btn.place(x= 450, y= 300) 
answer3_btn = tk.Button(text=f"{words[index][3]}", command=check_answer3, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), border=10)
answer3_btn.place(x= 650, y= 300)
answer4_btn = tk.Button(text=f"{words[index][4]}", command=check_answer4, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), border=10)
answer4_btn.place(x= 250, y= 500)
answer5_btn = tk.Button(text=f"{words[index][5]}", command=check_answer5, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), border=10)
answer5_btn.place(x= 450, y= 500)
answer6_btn = tk.Button(text=f"{words[index][6]}", command=check_answer6, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), border=10)
answer6_btn.place(x= 650, y= 500)

# wywoływanie label

message_label = tk.Label(easygame, text="", font=("Impact", 18), bg="white")
message_label.pack(pady=20)

score_label = tk.Label(easygame, text="", font=("Impact", 18), bg="white")
score_label.pack()

# wywołanie informacje ~ przycisk

Info = tk.Button(text="Informacje", font=("Impact", 18), bg="lightblue", fg="black", border=5, command=lambda: info())
Info.pack(side="bottom")

update_gui()
easygame.mainloop()
