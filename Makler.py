def schreibe_ueberschrift(datei, text):
    datei.write(text + "\n")
    datei.write("-" * len(text) + "\n\n")


print("Grundflächenberechnung einer Wohnung")
# Erstellen einer Text Datei
with open ("Berechnung.txt", "w", encoding="utf-8") as f:
    schreibe_ueberschrift(f, "Räume: ")
    f.write("\n")
Räume = int(input("Anzahl der Räume eingeben: "))
Zähler = 0
r = 1
Gesamtfläche = 0
while Zähler < Räume:
    print(f"Raum Nr.{r}")
    r += 1
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
        Fläche += (a * b)
        Zähler1 += 1
        n += 1
        if Zähler1 >= Rechtecke:
            break
    # Schreiben der Ergebnisse in eine Text Datei
    with open ("Berechnung.txt", "a", encoding="utf-8") as f:
        f.write(f"Raumname: {Raumname}\n")
        f.write(f"Raumfläche: {Fläche} m\u00B2\n")
        f.write("\n")
    Gesamtfläche += Fläche
    Zähler = Zähler + 1
with open ("Berechnung.txt", "a", encoding="utf-8") as f:
    f.write(f"Gesamtfläche der Wohnung: {Gesamtfläche} m\u00B2\n")