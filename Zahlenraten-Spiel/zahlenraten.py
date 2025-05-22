import random

def zahlen_raten():
    print("🎯 Willkommen beim Zahlenratespiel!")
    print("Ich habe mir eine Zahl zwischen 1 und 10 ausgedacht.")
    
    geheime_zahl = random.randint(1, 10)
    versuche = 3

    for versuch in range(1, versuche + 1):
        try:
            tipp = int(input(f"\n{versuch}. Versuch: "))
        except ValueError:
            print("❌ Bitte gib eine gültige Zahl ein!")
            continue

        if tipp == geheime_zahl:
            print("🎉 Glückwunsch! Du hast richtig geraten.")
            break
        elif tipp < geheime_zahl:
            print("🔼 Die gesuchte Zahl ist größer.")
        else:
            print("🔽 Die gesuchte Zahl ist kleiner.")

    else:
        print(f"\n😢 Leider verloren! Die Zahl war: {geheime_zahl}")

zahlen_raten()
