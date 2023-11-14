
import tkinter as tk
import mysql.connector

# połaczenie z bazą danych

MySQL = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'naukaslownictwa')
cursor = MySQL.cursor()

cursor.execute("SELECT polish, english FROM words ORDER BY RAND() LIMIT 20")
words = cursor.fetchall()

MySQL.close()

# okno - trudna gra

hardgame = tk.Tk()
hardgame.resizable(False, False)
hardgame.title("NaukaSłownictwa - Pingolingo, poziom: trudny")
hardgame.config(background="white")

window_width = 1000
window_height = 900
screen_width = hardgame.winfo_screenwidth()
screen_height = hardgame.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 6
hardgame.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

bg = tk.PhotoImage(file = "tlo.png")
bg_img = tk.Label(image=bg).place(x=-20, y=0)

# fukcja do informacji

def info():
    infor = tk.Toplevel()
    infor.config(background="white")
    screen_width = infor.winfo_screenwidth()
    screen_height = infor.winfo_screenheight()
    window_width = 1000
    window_height = 650
    x1 = (screen_width - window_width) // 2
    y1 = (screen_height - window_height) // 6
    infor.geometry('{}x{}+{}+{}'.format(window_width, window_height, x1, y1))
    infor.title("Informacje o poziomie trudnym - Pingolingo")
    img1 = tk.PhotoImage(file = "tloinfo.png")
    img2 = tk.Label(infor, image=img1)
    inf = tk.Label(infor, text="Poziom trudny informacje", bg="white")
    inf2 = tk.Label(infor, text="Na tym poziomie dostaniesz słowo napisane w języku polskim. \n Twoim zadaniem jest przetłumaczyć to słowo na język angielski! \n Czy dasz radę to zrobić?\n Powodzenia!")
    inf.config(font=("Impact", 26), fg="darkblue")
    inf2.config(font=("Impact", 22), bg="white")
    inf.pack()
    inf2.pack()
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
    if answer.lower() == words[index][1].lower():
        message_label.config(text="Brawo! To jest poprawna odpowiedź.", fg="green")
        points += 1
    else:
        message_label.config(text=f"Niestety, to nie jest poprawna odpowiedź. Poprawna odpowiedź to: {words[index][1]}.", fg="red")
        mistakes += 1
    index += 1
    if index < 20 and mistakes < 4:
        update_gui()
    else:
        show_result()

# aktualizowanie pytan + liczby punktow + liczby pomyłek

def update_gui():
    
    question_label.config(text=f"Jak jest po angielsku: {words[index][0]}?")
    
    score_label.config(text=f"Punkty: {points} | Pomyłki: {mistakes}")

# fukcja aby po wygraniu/przegraniu zagrac w inny level

def new_game():
    hardgame.destroy()
    from gra import windowstart

# pokazywanie wyniku

def show_result():
    for widget in hardgame.winfo_children():
        widget.destroy()
    if points >= 15:
        done = tk.PhotoImage(file="welldone.png")
        result_label = tk.Label(hardgame, text=f"Gratulacje! Uzyskałeś/aś aż {points} punktów na 20 możliwych. \n Świetnie ci poszło, pingwin Pingo jest z ciebie dumny! Oby tak dalej! \n Well done my friend! Penguin Pingo is really proud of you!", font=("Arial", 24), bg="white", fg="green")
        result_label.pack(pady=20)
        result_img = tk.Label(image=done)
        result_img.pack()
    elif points > 1 and points < 15:
        done = tk.PhotoImage(file="nt.png")
        result_label = tk.Label(hardgame, text=f"Szkoda! Uzyskałeś/aś {points} punktów na 20 możliwych. \n Mamy nadzieję, że nastepnym razem pójdzie ci lepiej! \n A jak nie pingwin Pingo ci pomoże!\n Ahh nice try! \n Penguin Pingo hopes that next time you will do better! ", font=("Arial", 24), bg="white", fg="red")
        result_label.pack(pady=20)
        result_img = tk.Label(image=done)
        result_img.pack()
    else:
        done = tk.PhotoImage(file="nt.png")
        result_label = tk.Label(hardgame, text=f"Szkoda! Uzyskałeś/aś {points} punktów na 20 możliwych. \n Mamy nadzieję, że nastepnym razem pójdzie ci lepiej! \n A jak nie pingwin Pingo ci pomoże!\n Ahh nice try! \n Penguin Pingo hopes that next time you will do better! ", font=("Arial", 24), bg="white", fg="red")
        result_label.pack(pady=20)
        result_img = tk.Label(image=done)
        result_img.pack()
        top3 = tk.Toplevel()
        img = tk.PhotoImage(file="image.png")
        img2 = tk.Label(top3, image=img)
        img2.pack()

   
    # wywolanie przycisku by zamknac calkowicie program
    exit_button = tk.Button(hardgame, text="Zakończ", font=("Arial", 18), bg="white", border=10, command=hardgame.destroy)
    exit_button.pack(pady=20)
    # wywolanie przycisku by zagrac w inny level
    newgame_button= tk.Button(hardgame, text="Zagraj w inny poziom trudności", font=("Arial", 18), bg="white", border=10, command=new_game)
    newgame_button.pack(pady=20)
    bg_img = tk.Label(image=bg).pack()
    top3.mainloop()
    widget.mainloop()

# wywoływanie label, button i entry

question_label = tk.Label(hardgame, text="", font=("Impact", 24), bg="white")
question_label.pack(pady=20)

# wywołanie wpisywania odpowiedzi ~ entry
entry = tk.Entry(hardgame, font=("Arial", 18), width=20)
entry.pack(pady=20)

# wywołanie sprawdzania odpowiedzi ~ przycisk
check_button = tk.Button(hardgame, text="Sprawdź", font=("Impact", 18), bg="white", border=10, command=check_answer)
check_button.pack(pady=20)

# wywoływanie label

message_label = tk.Label(hardgame, text="", font=("Impact", 18), bg="white")
message_label.pack(pady=20)

score_label = tk.Label(hardgame, text="", font=("Impact", 18), bg="white")
score_label.pack(pady=20)

# wywołanie informacje ~ przycisk

Info = tk.Button(text="Informacje", font=("Impact", 18), bg="lightblue", fg="black", border=5, command=lambda: info())
Info.pack(side="bottom")

update_gui()
hardgame.mainloop()