def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b

def multiplizieren(a, b):
    return a * b

def dividieren(a, b):
    if b == 0:
        return "Fehler: Division durch Null"
    return a / b

def potenzieren(a, b):
    return a ** b

def modulo(a, b):
    return a % b

def betrag(a):
    return abs(a)

def ist_gerade(n):
    return n % 2 == 0

def ist_primzahl(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def menü():
    print("Willkommen beim erweiterten Taschenrechner!")
    print("1. Addieren")
    print("2. Subtrahieren")
    print("3. Multiplizieren")
    print("4. Dividieren")
    print("5. Potenzieren")
    print("6. Modulo")
    print("7. Betrag")
    print("8. Ist Gerade?")
    print("9. Ist Primzahl?")
    print("0. Beenden")

    while True:
        wahl = input("\nWähle eine Option (0-9): ")
        
        if wahl == "0":
            print("Programm beendet.")
            break
        
        try:
            if wahl in ["1", "2", "3", "4", "5", "6"]:
                a = float(input("Gib die erste Zahl ein: "))
                b = float(input("Gib die zweite Zahl ein: "))
            elif wahl in ["7", "8", "9"]:
                a = int(input("Gib eine Zahl ein: "))
        except ValueError:
            print("Ungültige Eingabe!")
            continue

        if wahl == "1":
            print("Ergebnis:", addieren(a, b))
        elif wahl == "2":
            print("Ergebnis:", subtrahieren(a, b))
        elif wahl == "3":
            print("Ergebnis:", multiplizieren(a, b))
        elif wahl == "4":
            print("Ergebnis:", dividieren(a, b))
        elif wahl == "5":
            print("Ergebnis:", potenzieren(a, b))
        elif wahl == "6":
            print("Ergebnis:", modulo(a, b))
        elif wahl == "7":
            print("Betrag:", betrag(a))
        elif wahl == "8":
            print("Ist gerade:", ist_gerade(a))
        elif wahl == "9":
            print("Ist Primzahl:", ist_primzahl(a))
        else:
            print("Ungültige Auswahl!")
menü()
