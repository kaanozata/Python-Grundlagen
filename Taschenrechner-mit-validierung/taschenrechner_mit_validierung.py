def eingabe_zahl(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")

def eingabe_operation():
    print("\nWelche Operation möchtest du durchführen?")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")

    while True:
        wahl = input("Wähle (1/2/3/4): ").strip()
        if wahl in ['1', '2', '3', '4']:
            return wahl
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2, 3 oder 4.")

def rechne(zahl1, zahl2, op):
    if op == '1':
        return zahl1 + zahl2
    elif op == '2':
        return zahl1 - zahl2
    elif op == '3':
        return zahl1 * zahl2
    elif op == '4':
        if zahl2 == 0:
            return "Division durch Null nicht möglich!"
        return zahl1 / zahl2

# Hauptprogramm
print("Willkommen beim Taschenrechner!")

zahl1 = eingabe_zahl("Gib die erste Zahl ein: ")
zahl2 = eingabe_zahl("Gib die zweite Zahl ein: ")
op = eingabe_operation()

ergebnis = rechne(zahl1, zahl2, op)
print(f"\n Ergebnis: {ergebnis}")