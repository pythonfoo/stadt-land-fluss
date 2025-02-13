# Stadt Land Fluss
# für lokale Spieler
import random
import string
import wikidata

spieler_anzahl = int(input("Wie viele wollen spielen? "))

if spieler_anzahl > 10:
    print("Es können maximal 10 Spieler*innen teilnehmen!")
    exit()

print("Lade Daten...")
städte = wikidata.get_item_names_for_category("Q1549591")  # Großstadt
print(len(städte), "Städte.")
länder = wikidata.get_item_names_for_category("Q6256")  # Land
print(len(länder), "Länder.")
flüsse = wikidata.get_item_names_for_category("Q573344")  # großer Fluss
print(len(flüsse), "Flüsse.")

while True:
    buchstabe = random.choice(string.ascii_uppercase)
    stadt = input("Stadt: ")
              
    land = input("Land: ")

    fluss = input("Fluss: ")
    

