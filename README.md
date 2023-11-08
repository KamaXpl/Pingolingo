## 1 Nauka Słownictwa - Pingolingo
Aplikacja Pingolingo to program napisany w języku Python przy użyciu biblioteki Tkinter. Aplikacja jest przeznaczona do nauki języka angielskiego na różnych poziomach. Użytkownik zależnie od trybu, ma za zadanie zaznaczyć lub wpisać poprawną odpowiedź.
## 2 Wymagania systemowe
Aby uruchomić aplikację, potrzebujesz zainstalować następujące komponenty:
```
Python 3.x
Tkinter
mysql-connector-python
Pillow
```
Również możesz zainstalować je w terminalu
```
pip install tk
pip install mysql-connector-python
pip install Pillow
```
## 3 Połączenie z bazą danych
Aplikacja łączy się z bazą danych MySQL za pomocą biblioteki mysql.connector. Parametry połączenia są ustawiane na początku programu:
```
(host="localhost",
user="root"
password="",
db="naukaslownictwa")
```
## 4 Zmienne
windowstart - Zmienna reprezentująca główne okno interfejsu Tkinter. Tutaj jest tworzone okno główne gry.

window_width, window_height - Zmienne reprezentujące wielkość okna interfeksu Tkinter.

screen_width, screen_height - Zmienne, które obliczają pozycję okna, aby było ono na środku danego wyświetlacza.

bg - Zmienna odpowiadająca za zdjęcie tła.

bg_img - Zmienna odpowiadająca za ustawienie tła w poprawnym miejscu.

Witaj - Zmienna odpowiadająca początkowemu tekstowi.

Pyt_o_poz - Zmienna, która odpowiada za zapytanie o tryb gry.

pyt1 - Zmienna, odpowiadająca za tekst.

index, points, mistakes - Zmienne odpowiadające za pytanie, punkty i błędy.

question_label - Wyświetla pytanie.

answer1_btn, answer2_btn, answer3_btn, answer4_btn, answer5_btn, answer6_btn - Wyświetla odpowiedzi A-F.

message_label - Wskazuje czy odpowiedź jest poprawna czy błędna.

score_label - Wyświetla końcowy wynik.

easygame, mediumgame, medhardgame, hardgame - Zmienne reprezentujące okna interfejsu Tkinter.

question - Zmienna odpowiadająca polskiemu słowu z bazy danych.

answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8 - Zmienne odpowiadające odpowiedziom na pytania z bazy danych.

r_answer - Zmienna odpowiadająca za poprawną odpowiedź z bazy danych.

entry - Zmienna pozwalająca użytkownikowi na wpisanie odpowiedzi do interfejsu Tkinter.

check_button - Zmienna odpowiadająca przyciskowi do sprawdzenia czy odpowiedź podana przez użytkownika jest poprawna.




## 5 Funkcje
quit() - funkcja, która zamyka aplikację.
```
def quit():
    windowstart.destroy()

```
easy() - funkcja, która przenosi użytkownika do danego trybu gry
```
def easy():
    windowstart.destroy()
    from easy import easygame
```
info() - funkcja, która zawiera informacje na temat poziomu trudności
```
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
    inf.config(font=("Impact", 22))
    inf1 = tk.Label(infor, text="Twoim zadaniem jest odpowiedzenie na 20 pytan \n do kazdego pyt jest")
    inf1.config(font=("Arial", 11))
    inf.pack()
    inf1.pack()
    img2.pack()
    infor.title("Informacje o poziomie łatwym")
    infor.mainloop()

```
check_answer1() - funkcja, której zadaniem jest sprawdzenie czy odpowiedź podana przez użytkownika jest poprawna.
```
def check_answer1():
    global points, mistakes, index
    if words[index][1] == words[index][7]:
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

```
update_answers() - aktualizuje odpowiedzi.
```
def update_answers():
    global index
    answer1_btn.config(text=f"1: {words[index][1]}")
    answer2_btn.config(text=f"2: {words[index][2]}")
    answer3_btn.config(text=f"3: {words[index][3]}")
    answer4_btn.config(text=f"4: {words[index][4]}")
    answer5_btn.config(text=f"5: {words[index][5]}")
    answer6_btn.config(text=f"6: {words[index][6]}")

```
update_gui() - aktualizuje pytanie, punkty i błędy.
```
def update_gui():



    question_label.config(text=f"Co to jest: {words[index][0]}.jpg?")


    
    score_label.config(text=f"Punkty: {points} | Pomyłki: {mistakes}")
```
new_game() - funkcja, która daje możliwość powrotu do lobby gry oraz wybrania innego poziomu.
```
def new_game():
    easygame.destroy()
    from gra import windowstart


```
show_result - funkcja zwraca końcowy wynik uzyskany przez użytkownika
```
def show_result():
    for widget in easygame.winfo_children():
        widget.destroy()
    if points >= 15:
        result_label = tk.Label(easygame, text=f"Gratulacje! Uzyskałeś/aś aż {points} punktów na 20 możliwych. \n Świetnie ci poszło, pingwin Pingo jest z ciebie dumny! Oby tak dalej! \n Well done my friend! Penguin Pingo is really proud of you!", font=("Arial", 24), bg="white", fg="green")
    else:
        result_label = tk.Label(easygame, text=f"Szkoda! Uzyskałeś/aś {points} punktów na 20 możliwych. \n Mamy nadzieję, że nastepnym razem pójdzie ci lepiej! \n A jak nie pingwin Pingo ci pomoże!\n Ahh nice try! \n Penguin Pingo hopes that next time you will do better! ", font=("Arial", 24), bg="white", fg="red")
    result_label.pack(pady=20)
    # wywolanie przycisku by zamknac calkowicie program
    exit_button = tk.Button(easygame, text="Zakończ", font=("Arial", 18), command=easygame.destroy)
    exit_button.pack(pady=20)
    # wywolanie przycisku by zagrac w inny level
    newgame_button= tk.Button(easygame, text="Zagraj w inny poziom trudności", font=("Arial", 18), command=new_game)
    newgame_button.pack(pady=20)
    bg_img = tk.Label(image=bg).pack()
```

## 6 Autorzy
Baza danych Izabela Majcherczyk, Kamila Wydra

Kod aplikacji Izabela Majcherczyk  

Wygląd aplikacji Izabela Majcherczyk 

Dokumentacja Kamila Wydra

Informacje Kamila Wydra

## 7 Źródła
Zdjęcia - Wygenerowane za pomocą sztucznej inteligencji

