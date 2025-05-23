from calculator import (
    addieren,
    subtrahieren,
    multiplizieren,
    dividieren,
    potenzieren,
    modulo,
    betrag,
    ist_gerade,
    ist_primzahl
)

# Addieren
assert addieren(3, 4) == 7
assert addieren(-5, 5) == 0

# Subtrahieren
assert subtrahieren(10, 3) == 7
assert subtrahieren(0, 5) == -5

# Multiplizieren
assert multiplizieren(2, 4) == 8
assert multiplizieren(-3, 3) == -9

# Dividieren
assert dividieren(8, 2) == 4
assert dividieren(5, 0) == "Fehler: Division durch Null"

# Potenzieren
assert potenzieren(2, 3) == 8
assert potenzieren(5, 0) == 1

# Modulo
assert modulo(10, 3) == 1
assert modulo(5, 5) == 0

# Betrag
assert betrag(-7) == 7
assert betrag(4) == 4

# Ist Gerade
assert ist_gerade(4) == True
assert ist_gerade(7) == False

# Ist Primzahl
assert ist_primzahl(2) == True
assert ist_primzahl(9) == False
assert ist_primzahl(29) == True
assert ist_primzahl(1) == False
