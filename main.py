# Stadt Land Fluss
# für lokale Spieler
import random
import string
import wikidata

while True:
    try:
        spieler_anzahl = int(input("Wie viele wollen spielen? "))
    except ValueError:
        print("Du musst eine Zahl eingeben!")
        continue

    if spieler_anzahl > 10:
        print("Es können maximal 10 Spieler*innen teilnehmen!")
        continue
    if spieler_anzahl <= 0:
        print("Gib bitte eine positive Zahl ein!")
        continue
    
    break

print("Lade Daten...")
städte = [
    s.casefold()
    for s in wikidata.get_item_names_for_category("Q1549591")  # Großstadt
]
print(len(städte), "Städte.")

länder = [
    l.casefold()
    for l in wikidata.get_item_names_for_category("Q6256")
]
print(len(länder), "Länder.")

flüsse = [
    f.casefold()
    for f in wikidata.get_item_names_for_category("Q1267889")  # Waterway
]
print(len(flüsse), "Flüsse.")

while True:
    buchstabe = random.choice(string.ascii_lowercase)
    städte_mit_buchstabe = [s for s in städte if s.startswith(buchstabe)]
    while True:
        if not städte_mit_buchstabe:
            print("Es gibt keine Stadt mit diesem Buchstaben, deshalb kriegtst du hier nen kostenlosen Punkt ;)")
            break
        stadt = input(f"Stadt mit {buchstabe.upper()} ('-' zum Aufgeben): ").casefold()
        if stadt == "-":
            break
        if stadt in städte_mit_buchstabe:
            print("Richtig!")
            break
        print("Falsch! Probier's nochmal!")

    länder_mit_buchstabe = [l for l in länder if l.startswith(buchstabe)]
    while True:
        if not länder_mit_buchstabe:
            print("Es gibt keine Länder mit diesem Buchstaben, deshalb kriegtst du hier nen kostenlosen Punkt ;)")
            break
        land = input(f"Land mit {buchstabe.upper()}  ('-' zum Aufgeben): ").casefold()
        if land == "-":
            break
        if land in länder_mit_buchstabe:
            print("Richtig!")
            break
        print("Falsch! Probier's nochmal!")

    flüsse_mit_buchstabe = [f for f in flüsse if f.startswith(buchstabe)]
    while True:
        if not flüsse_mit_buchstabe:
            print("Es gibt keine Flüsse mit diesem Buchstaben, deshalb kriegtst du hier nen kostenlosen Punkt ;)")
            break
        fluss = input(f"Fluss mit {buchstabe.upper()} ('-' zum Aufgeben): ").casefold()
        if fluss == "-":
            break
        if fluss in flüsse_mit_buchstabe:
            print("Richtig!")
            break
        print("Falsch! Probier's nochmal!")

