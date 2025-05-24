from generator import generiere_testfälle

def test_generiere_testfälle():
    name = "kaan"
    email = "kaan@mail.com"
    passwort = "kaan1234"

    testfälle = generiere_testfälle(name, email, passwort)

    assert len(testfälle) == 5, "Es sollten 5 Testfälle generiert werden."

    assert testfälle[0]["Erwartung"] == "Erfolgreiche Anmeldung"
    assert testfälle[1]["Name"] == "", "Name sollte leer sein"
    assert testfälle[1]["Erwartung"] == "Fehler: Name erforderlich"
    assert testfälle[2]["E-Mail"] == "ungültigeEmail"
    assert testfälle[2]["Erwartung"] == "Fehler: Ungültige E-Mail-Adresse"
    assert testfälle[3]["Passwort"] == ""
    assert testfälle[3]["Erwartung"] == "Fehler: Passwort erforderlich"
    assert testfälle[4]["Passwort"] == "123"
    assert testfälle[4]["Erwartung"] == "Fehler: Passwort zu kurz"

    print("Alle Tests erfolgreich bestanden.")

test_generiere_testfälle()