vorname = input("Wie heißt du? ")
nachname = input("Was ist dein Nachname? ")

while True:
    try:
        alter_input = input("Wie alt bist du? ").strip()
        jahre = int(alter_input)
        if 0 < jahre <= 120:
            break
        else:
            print("Bitte gib ein realistisches Alter zwischen 1 und 120 ein.")
    except ValueError:
        print("Bitte gib eine gültige Zahl für dein Alter ein.")

print(f"Hallo {vorname} {nachname}! Du bist {jahre} Jahre alt.")

if 0 <= jahre <= 6:
    print("Hallo Baby :)")
elif 18 <= jahre <= 99:
    print("Kannst du reinkommen? Ja")
else:
    print("Kannst du reinkommen? Nein")
