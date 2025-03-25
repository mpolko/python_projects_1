#simple
a = input("Podaj pierwszą liczbę: ")
operator = input("Podaj operator matematyczny: ")
b = input("Podaj drugą liczbę: ")

if operator == "+":
    wynik = int(a)+int(b)
    print(wynik)
elif operator == "-":
    wynik = int(a)-int(b)
    print(wynik)
elif operator == "*":
    wynik = int(a)*int(b)
    print(wynik)
elif operator == "/":
    wynik = int(a)/int(b)
elif operator:
    print("Bledne dane")