# Test Case Generator für Formulare

Dieses Programm, das automatisch Testszenarien für Formularfelder wie Name, E-Mail und Passwort generiert, wurde entwickelt, um praktische Erfahrungen im Bereich Software-Testing (QA) zu sammeln.

## Was macht das Programm?

Das Programm:

- Fragt den Benutzer nach Name, E-Mail und Passwort
- Erzeugt automatisch 5 typische Testfälle;
  - Gültiger Eintrag
  - Leerer Name
  - Ungültige E-Mail-Adresse
  - Leeres Passwort
  - Zu kurzes Passwort
- Zeigt die Testfälle im Terminal
- Schreibt sie in eine Markdown-Datei `testcases_output.md` im Projektverzeichnis