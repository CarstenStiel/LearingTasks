"""
AUTHOR
    Tabea Pienkoß

VERSION
    1.0

Aufgabe C02
"""
# Imports:
import math
import matplotlib.pyplot as plt
import numpy as np


# Definition der Funktionen:
# Berechnungsterm stammt aus der Musterlösung "C02-Computerphysik-Ivanov.py".
# Diese Funktion berechnet das Integral rekursiv und gibt dies als Array aus.
def integral_rekursive_arr(n, arr=None):  # Derzeitiges n und Array als Parameter übergeben (Array soll bei erstmaligem Funktionsaufruf auf dem Defaultwert sein).
    # Wenn die Funktion erstmalig aufgerufen wird, soll ein leeres Array erstellt werden:
    if arr is None:
        arr = []  # Erstelle ein leeres Array, wenn keins übergeben wurde.

    # Wenn n = 0 ist, dann führe folgende Funktion aus:
    if n == 0:
        term = math.atan(1 / math.sqrt(7.0)) / math.sqrt(7.0)  # Berechne: arc-tan(1/√7)/√7.
        arr.append(term)  # Füge die Berechnung dem Array hinzu.
        return arr  # Gebe das Array zurück.
    # Solange n > 0, führe folgende Funktion aus:
    else:
        term = 1.0 / (2.0 * n - 1.0) - 7.0 * integral_rekursive_arr(n - 1, arr)[-1]  # Berechne: 1/(2*(n-1)) - 7 * "Vorgänger"
        arr.append(term)  # Füge die Berechnung dem Array hinzu.
        return arr  # Gebe das Array zurück.


# Zusatz:
# Diese Funktion erweitert die Aufgabe, indem hier nach einem Input gefragt wird für N, solange bis eine Ganzzahl 0 ≤ n < 999 gewählt wurde.
# Das eingegebene n wird auf max. 999 beschränkt, aufgrund der Rekursionstiefe. Da ab n=384 die Berechnung nur inf für n ungerade und -inf für n gerade ausgibt, scheint dies vertretbar.
def input_n():
    # Solange der Input nicht korrekt ist, wird die Schleife immer wieder durchlaufen:
    while True:
        userInput = input("Geben Sie N ein mit 0 <= N < 999: ")  # Input vom Nutzer.
        # Überprüfen, ob die Eingabe eine Zahl ist und 0 ≤ Eingabe < 999:
        if userInput.isdigit() and 0 <= int(userInput) < 999:
            N = int(userInput)  # Nehme den Userinput als N und wandele diesen in einen Integer Wert um.
            print(f"Die Eingabe war N = {N}")  # Ausgabe in der Konsole.
            return N  # Rückgabe von N, wenn eine gültige Eingabe gemacht wurde.
        # Wenn es keine positive Ganzzahl war, dann gib Fehler aus und starte die Schleife von neuem:
        else:
            print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein mit 0 <= N < 999.")


# Diese Funktion erweitert die Aufgabe, indem hier gefragt wird, ob die n-Werte zusätzlich ausgegeben werden sollen.
def show_arr(n, arr):  # Das Array das ggf. angezeigt werden soll, als Parameter übergeben
    # Solange der Input nicht korrekt ist, wird die Schleife immer wieder durchlaufen:
    while True:
        ans = input("n-Werte in Konsole ausgeben[y/n]:")  # Userinput.
        # Wenn Userinput "y" (ja) war, dann gebe die n-Werte aus:
        if ans == "y":
            # Für jedes i (n) gebe die folgende Zeile aus:
            for i in range(0, n + 1):
                print(f"n={i}: {arr[i]}")  # n=(i): n-Wert.
        # Wenn Userinput "n" (nein) war, dann gebe nichts aus:
        elif ans == "n":
            break
        # Falls Userinput ungültig war, dann gebe Fehler aus und wiederhole die Schleife:
        else:
            print("Eingabe überprüfen: 'n' für nein und 'y' für ja")


# Ausführung der eigentlichen Aufgaben, wenn dieses Skript als "__main__" ausgeführt wird:
if __name__ == "__main__":
    n = input_n()  # Eingabe des n-Wertes.
    integral_arr = integral_rekursive_arr(n)
    print(f"Auswertung des Integrals für den n-Wert '{n}': {integral_arr[-1]}")  # Ausgabe des berechnetes Intergrals für den spezifischen n-Wert.

    # User kann sich n-Werte anzeigen lassen.
    show_arr(n, integral_arr)

    # x und y Werte berechnen für die Darstellung des Integrals.
    x_arr = np.arange(0, n + 1, 1)  # x-Werte von 0-N erstellen.
    y_arr = integral_rekursive_arr(n)  # Erstellen der y-Werte.

    # Darstellung des berechneten Intergrals, abhängig von n.
    # Hier wird auf eine Limitierung der y-Achse gesetzt, da ab n >= 19 die Werte zu groß werden.
    plt.figure()  # Erstellung einer Figur.
    plt.plot(x_arr, y_arr, marker='o')  # Plotten der x und y Werte.
    plt.xlabel('n')  # x-Achse mit 'n' Labeln.
    plt.ylabel('y')  # y-Achse mit 'y' Labeln.
    plt.title('Aufgabe C02')  # Der Figur einen Titel geben.
    plt.grid()  # Raster erstellen.
    plt.ylim(-0.1, 0.2)  # Limitieren der y-Werte mit min=-0.1 und max=0.2.
    plt.show()  # Anzeigen des Plots.
