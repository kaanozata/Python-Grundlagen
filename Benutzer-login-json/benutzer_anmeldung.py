import json
import time
import os

BASIS_PFAD = os.path.dirname(__file__)
DATEINAME = os.path.join(BASIS_PFAD, "benutzer.json")

def benutzer_laden():
    if not os.path.exists(DATEINAME):
        return {}
    with open(DATEINAME, "r", encoding="utf-8") as f:
        return json.load(f)

def benutzer_speichern(benutzer):
    with open(DATEINAME, "w", encoding="utf-8") as f:
        json.dump(benutzer, f, indent=4)

def neuer_benutzer(benutzer):
    neuer_name = input("Neuer Benutzername: ").strip()
    if neuer_name in benutzer:
        print("Benutzer existiert bereits!")
    else:
        neues_passwort = input("Neues Passwort: ").strip()
        benutzer[neuer_name] = neues_passwort
        benutzer_speichern(benutzer)
        print(f"Benutzer '{neuer_name}' wurde erfolgreich erstellt!")

def anmeldung(benutzer):
    max_versuche = 3

    while True:
        versuche = 0
        while versuche < max_versuche:
            name = input("Benutzername: ").strip()
            passwort = input("Passwort: ").strip()

            if name in benutzer and benutzer[name] == passwort:
                print(f"\nWillkommen, {name}!")
                return
            elif name in benutzer:
                print("Passwort ist falsch.")
            else:
                print("Benutzer existiert nicht.")

            versuche += 1
            verbleibend = max_versuche - versuche
            if verbleibend > 0:
                print(f"Verbleibende Versuche: {verbleibend}\n")

        print("\nDu hast alle Versuche verbraucht!")
        print("Sicherheitszeit: 5 Sekunden... Bitte warte.")
        time.sleep(5)
        print("Du kannst es erneut versuchen.\n")


print("Willkommen beim Anmeldesystem mit JSON!")

benutzer = benutzer_laden()

antwort = input("Hast du schon ein Konto? (ja/nein): ").strip().lower()

if antwort == "ja":
    anmeldung(benutzer)
elif antwort == "nein":
    neuer_benutzer(benutzer)
else:
    print("Ungültige Eingabe. Programm wird beendet.")
