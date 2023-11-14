import tkinter as tk
from tkinter import *
import mysql.connector
MySQL = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'naukaslownictwa')
cursor = MySQL.cursor()

cursor.execute("SELECT * FROM medium1 ORDER BY RAND() LIMIT 20")
words = cursor.fetchall()

MySQL.close()


mediumgame = tk.Tk()
mediumgame.resizable(False, False)
mediumgame.title("NaukaSłownictwa - Pingolingo, poziom: średni")
mediumgame.config(background="white")

window_width = 1000
window_height = 900
screen_width = mediumgame.winfo_screenwidth()
screen_height = mediumgame.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 6
mediumgame.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

bg = tk.PhotoImage(file = "tlo.png")
bg_img = tk.Label(image=bg).place(x=-20, y=0)

def info():
    infor = tk.Toplevel()
    infor.config(bg="white")
    screen_width = infor.winfo_screenwidth()
    screen_height = infor.winfo_screenheight()
    window_width = 1000
    window_height = 650
    x1 = (screen_width - window_width) // 2
    y1 = (screen_height - window_height) // 6
    infor.geometry('{}x{}+{}+{}'.format(window_width, window_height, x1, y1))
    infor.title("Informacje o poziomie średnim - Pingolingo")
    img1 = tk.PhotoImage(file = "tloinfo.png")
    img2 = tk.Label(infor, image=img1)
    inf = tk.Label(infor, text="Poziom średni informacje")
    inf.config(font=("Impact", 26), fg="darkblue", bg="white")
    inf1 = tk.Label(infor, text="Twoim zadaniem jest odpowiedzenie na 20 pytań. \n Do każdego pytania dostaniesz 8 odpowiedzi, \nz czego tylko jedna jest prawidłowa. \n Powodzenia!")
    inf1.config(font=("Impact", 22), bg="white")
    inf.pack()
    inf1.pack()
    img2.pack()
    infor.mainloop()

index = 0 # odpowiada za numer pytania
points = 0 # liczba punktów
mistakes = 0 # liczba pomyłek

question = words[index][0] # słowo po polsku
answer1 = words[index][1] # odpowiedzi od 1
answer2 = words[index][2]
answer3 = words[index][3]
answer4 = words[index][4]
answer5 = words[index][5]
answer6 = words[index][6]
answer7 = words[index][7]
answer8 = words[index][8]# do 8
r_answer = words[index][9] # poprawna odpowiedz

# funkcje do sprawdzania odpowiedzi + do liczenia punktów i pomyłek

def check_answer1():
    global points, mistakes, index
    if words[index][1] == words[index][9]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][9]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer2():
    global points, mistakes, index
    if words[index][2] == words[index][9]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][9]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer3():
    global points, mistakes, index
    if words[index][3] == words[index][9]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][9]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer4():
    global points, mistakes, index
    if words[index][4] == words[index][9]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][9]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer5():
    global points, mistakes, index
    if words[index][5] == words[index][9]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][9]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer6():
    global points, mistakes, index
    if words[index][6] == words[index][9]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][9]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer7():
    global points, mistakes, index
    if words[index][7] == words[index][9]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][9]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()

def check_answer8():
    global points, mistakes, index
    if words[index][8] == words[index][9]:
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][9]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
        update_answers()
    else:
        show_result()
        
# aktualizowanie pytan + liczby punktow + liczby pomyłek

def update_answers():
    global index
    answer1_btn.config(text=f"{words[index][1]}")
    answer2_btn.config(text=f"{words[index][2]}")
    answer3_btn.config(text=f"{words[index][3]}")
    answer4_btn.config(text=f"{words[index][4]}")
    answer5_btn.config(text=f"{words[index][5]}")
    answer6_btn.config(text=f"{words[index][6]}")
    answer7_btn.config(text=f"{words[index][7]}")
    answer8_btn.config(text=f"{words[index][8]}")

def update_gui():
    
    question_label.config(text=f"Jak jest po angielsku: {words[index][0]}?")
    
    score_label.config(text=f"Punkty: {points} | Pomyłki: {mistakes}")

# fukcja aby po wygraniu/przegraniu zagrac w inny level

def new_game():
    mediumgame.destroy()
    from gra import windowstart

# pokazywanie wyniku

def show_result():
    for widget in mediumgame.winfo_children():
        widget.destroy()
    if points >= 15:
        done = tk.PhotoImage(file="welldone.png")
        result_label = tk.Label(mediumgame, text=f"Gratulacje! Uzyskałeś/aś aż {points} punktów na 20 możliwych. \n Świetnie ci poszło, pingwin Pingo jest z ciebie dumny! Oby tak dalej! \n Well done my friend! Penguin Pingo is really proud of you!", font=("Arial", 24), bg="white", fg="green")
    else:
        done = tk.PhotoImage(file="nt.png")
        result_label = tk.Label(mediumgame, text=f"Szkoda! Uzyskałeś/aś {points} punktów na 20 możliwych. \n Mamy nadzieję, że nastepnym razem pójdzie ci lepiej! \n A jak nie pingwin Pingo ci pomoże!\n Ahh nice try! \n Penguin Pingo hopes that next time you will do better! ", font=("Arial", 24), bg="white", fg="red")
    result_label.pack(pady=20)
    result_img = Label(image=done)
    result_img.pack()
    # wywolanie przycisku by zamknac calkowicie program
    exit_button = tk.Button(mediumgame, text="Zakończ", font=("Arial", 18), bg="white", border=10, command=mediumgame.destroy)
    exit_button.pack(pady=20)
    # wywolanie przycisku by zagrac w inny level
    newgame_button= tk.Button(mediumgame, text="Zagraj w inny poziom trudności", font=("Arial", 18), bg="white", border=10, command=new_game)
    newgame_button.pack(pady=20)
    bg_img = tk.Label(image=bg).pack()

# wywoływanie label i button do odpowiedzi 

question_label = tk.Label(mediumgame, text="", font=("Impact", 24), bg="white")
question_label.pack(pady=20)

answer1_btn = tk.Button(text=f"{words[index][1]}", command=check_answer1, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), bg="#d9f1ff", border=10)
answer1_btn.place(x= 150, y= 300)
answer2_btn = tk.Button(text=f"{words[index][2]}", command=check_answer2, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), bg="#d9f1ff", border=10)
answer2_btn.place(x= 350, y= 300) 
answer3_btn = tk.Button(text=f"{words[index][3]}", command=check_answer3, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), bg="#d9f1ff", border=10)
answer3_btn.place(x= 550, y= 300)
answer4_btn = tk.Button(text=f"{words[index][4]}", command=check_answer4, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), bg="#d9f1ff", border=10)
answer4_btn.place(x= 750, y= 300)
answer5_btn = tk.Button(text=f"{words[index][5]}", command=check_answer5, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), bg="#d9f1ff", border=10)
answer5_btn.place(x= 150, y= 500)
answer6_btn = tk.Button(text=f"{words[index][6]}", command=check_answer6, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), bg="#d9f1ff", border=10)
answer6_btn.place(x= 350, y= 500)
answer7_btn = tk.Button(text=f"{words[index][7]}", command=check_answer7, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), bg="#d9f1ff", border=10)
answer7_btn.place(x= 550, y= 500)
answer8_btn = tk.Button(text=f"{words[index][8]}", command=check_answer8, highlightthickness=2, width = 12, height= 4, font=('Arial', 10, 'bold'), bg="#d9f1ff", border=10)
answer8_btn.place(x= 750, y= 500)

# wywoływanie label

message_label = tk.Label(mediumgame, text="", font=("Impact", 18), bg="white")
message_label.pack(pady=20)

score_label = tk.Label(mediumgame, text="", font=("Impact", 18), bg="white")
score_label.pack(pady=20)

# wywołanie informacje ~ przycisk

Info = tk.Button(text="Informacje", font=("Impact", 18), bg="lightblue", fg="black", border=5, command=lambda: info())
Info.pack(side="bottom")

update_gui()
mediumgame.mainloop()




