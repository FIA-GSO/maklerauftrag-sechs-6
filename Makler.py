print("Grundflächenberechnung einer Wohnung")
# Erstellen einer Text Datei
with open ("Berechnung.txt", "w", encoding="utf-8") as f:
    f.write("Räume: \n")
Räume = int(input("Anzahl der Räume eingeben: "))
Zähler = 0
Gesamtfläche = 0
while Zähler < Räume:
    Raumname = str(input("Raumname eingeben: "))
    Rechtecke = int(input("In wie viele Rechtecke kann man den Raum unterteilen: "))
    Fläche = 0
    # Berechnung der Fläche eines Raumes
    Zähler1 = 0
    n = 1
    while True:
        print(f"Rechteck: {n}")
        a = int(input("Seite A angeben: "))
        b = int(input("Seite B angeben: "))
        Fläche = (a * b) + Fläche
        Zähler1 += 1
        n += 1
        if Zähler1 >= Rechtecke:
            break
    # Schreiben der Ergebnisse in eine Text Datei
    with open ("Berechnung .txt", "a", encoding="utf=-8") as f:
        f.write(f"Name: {Raumname}\n")
        f.write(f"Raumfläche: {Fläche}\n")
        f.write("\n")
    Gesamtfläche += Fläche
    Zähler = Zähler + 1
with open ("Berechnung .txt", "a", encoding="utf=-8") as f:
    f.write(f"Gesamtfläche der Wohnung: {Gesamtfläche}\n")