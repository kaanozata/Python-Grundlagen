# Fortgeschrittener Taschenrechner

Ein einfacher, aber leistungsstarker Taschenrechner, der sowohl Grundoperationen als auch erweiterte mathematische Funktionen unterstützt. Dieses Projekt wurde zur Übung von Python-Funktionen und Software-Testing entwickelt.

## Funktionen & Menüoptionen

Das Programm bietet ein einfaches Konsolenmenü zur Interaktion mit dem Nutzer. Der Nutzer kann eine Option auswählen und entsprechende Eingaben machen.

Verfügbare Operationen:

1. Zwei Zahlen addieren  
2. Zwei Zahlen subtrahieren  
3. Zwei Zahlen multiplizieren  
4. Zwei Zahlen dividieren (mit Nullprüfung)  
5. Potenzieren einer Zahl  
6. Modulo-Berechnung  
7. Betrag einer Zahl berechnen  
8. Prüfen, ob eine Zahl gerade ist  
9. Prüfen, ob eine Zahl eine Primzahl ist  
0. Beenden  

## Testsystem (test_calculator.py)

Alle Funktionen werden mit `assert` Anweisungen getestet. Diese befinden sich in der Datei `test_calculator.py`.
Wenn keine Fehlermeldung erscheint, funktionieren alle Funktionen korrekt. Im Fehlerfall wird eine `AssertionError` ausgegeben.

Zum Ausführen des Tests;

```bash
python test_calculator.py