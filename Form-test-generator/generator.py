import os

def generiere_testfälle(name, email, passwort):
    testfälle = []

    # Gültiger Fall
    testfälle.append({
        "Name": name,
        "E-Mail": email,
        "Passwort": passwort,
        "Erwartung": "Erfolgreiche Anmeldung"
    })

    # Leerer Name
    testfälle.append({
        "Name": "",
        "E-Mail": email,
        "Passwort": passwort,
        "Erwartung": "Fehler: Name erforderlich"
    })

    # Ungültige E-Mail
    testfälle.append({
        "Name": name,
        "E-Mail": "ungültigeEmail",
        "Passwort": passwort,
        "Erwartung": "Fehler: Ungültige E-Mail-Adresse"
    })

    # Leeres Passwort
    testfälle.append({
        "Name": name,
        "E-Mail": email,
        "Passwort": "",
        "Erwartung": "Fehler: Passwort erforderlich"
    })

    # Zu kurzes Passwort
    testfälle.append({
        "Name": name,
        "E-Mail": email,
        "Passwort": "123",
        "Erwartung": "Fehler: Passwort zu kurz"
    })

    return testfälle


def zeige_testfälle(testfälle):
    print("Generierte Testfälle:\n")
    for i, fall in enumerate(testfälle, 1):
        print(f"Testfall {i}:")
        for key, value in fall.items():
            print(f"  {key}: {value}")
        print()

def speichere_testfälle_als_md(testfälle):
    ordner = os.path.dirname(os.path.abspath(__file__))
    dateiname = os.path.join(ordner, "testcases_output.md")
    with open(dateiname, "a", encoding="utf-8") as f:
        f.write("# Generierte Testfälle\n\n")
        for i, fall in enumerate(testfälle, 1):
            f.write(f"## Testfall {i}\n")
            for key, value in fall.items():
                f.write(f"- **{key}**: {value}\n")
            f.write("\n")


# Beispielhafte Eingabe
name = input("Gib einen Namen ein: ")
email = input("Gib eine E-Mail-Adresse ein: ")
passwort = input("Gib ein Passwort ein: ")

testfälle = generiere_testfälle(name, email, passwort)
zeige_testfälle(testfälle)
speichere_testfälle_als_md(testfälle)
