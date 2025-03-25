from tkinter import *
#123
# Tworzenie okna kalkulatora
me = Tk()
me.geometry("345x460")
me.title("CALCULATOR")
melabel = Label(me, text="CALCULATOR", fg="White", bg='black', font=("Times", 30, 'bold'))
melabel.pack(side=TOP)
me.config(background='Black')

textin = StringVar()
operator = ""

# Funkcja obsługująca kliknięcia przycisków
def clickbut(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)

# Funkcja wykonująca obliczenia
def equlbut():
    global operator
    try:
        result = str(eval(operator, {"__builtins__": None}, {"pow": pow, "abs": abs}))
        textin.set(result)
    except:
        textin.set("Error")
    operator = ''

# Funkcja czyszcząca pole tekstowe
def clrbut():
    global operator
    operator = ""
    textin.set('')

# Pole tekstowe do wyświetlania wprowadzonych danych i wyników
metext = Entry(me, font=("Courier New", 12, 'bold'), textvar=textin, width=25, bd=5, bg='powder blue')
metext.pack()

# Definicja przycisków dla liczb i operatorów
buttons = [
    ('1', 10, 100), ('2', 10, 170), ('3', 10, 240),
    ('4', 75, 100), ('5', 75, 170), ('6', 75, 240),
    ('7', 140, 100), ('8', 140, 170), ('9', 140, 240),
    ('0', 10, 310), ('.', 75, 310), ('+', 205, 100),
    ('-', 205, 170), ('*', 205, 240), ('/', 205, 310),
    ('(', 270, 240), (')', 270, 310)
]

for (text, x, y) in buttons:
    Button(me, padx=14, pady=14, bd=4, bg='white', text=text,
           command=lambda t=text: clickbut(t), font=("Courier New", 16, 'bold')).place(x=x, y=y)

# Przycisk wartości bezwzględnej
butabs = Button(me, padx=8, pady=18, bd=4, bg='white', text="|x|",
                command=lambda: clickbut("abs("), font=("Courier New", 12, 'bold'))
butabs.place(x=140, y=310)

# Przycisk czyszczący
butclear = Button(me, padx=8, pady=49, bd=4, bg='light yellow', text="CE", command=clrbut,
                  font=("Courier New", 16, 'bold'))
butclear.place(x=270, y=100)

# Przycisk "=" do wykonywania obliczeń
butequal = Button(me, padx=144, pady=14, bd=4, bg='white', text="=", command=equlbut,
                  font=("Courier New", 16, 'bold'))
butequal.place(x=10, y=380)

me.mainloop()