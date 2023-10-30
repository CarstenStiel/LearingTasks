"""
AUTHOR
    Tabea Pienkoß

VERSION
    1.0.

Aufgabe C16
"""
# Imports:
import numpy as np
from numpy import sqrt, sin, cos, pi
from scipy.integrate import quad
import matplotlib.pyplot as plt


# Definition der Funktionen:
# Diese Funktion berechnet die Funktion von C(u) für ein spezifisches t.
def fC(t):
    return cos((pi / 2) * pow(t, 2))


# Diese Funktion berechnet C für ein spezifisches x.
def C(x):
    return quad(fC, 0, x)[0]


# Diese Funktion berechnet die Funktion von S(u) für ein spezifisches t.
def fS(t):
    return sin((pi / 2) * pow(t, 2))


# Diese Funktion berechnet S für ein spezifisches x.
def S(x):
    return quad(fS, 0, x)[0]


# Diese Funktion berechnet die Intensität "I" für ein spezielles a und x.
def I(a, x):
    return (1 / 8.) * (pow(2 * C(a * x) + 1, 2) + pow(2 * S(a * x) + 1, 2))


# Zusatz:
# Diese Funktion erweitert die Aufgabe, indem hier nach einem Input gefragt wird für eine Gleitkommazahl mit anpassbarem String.
def input_float(string):  # Übergabe des Anfragestrings als Parameter.
    # Solange der Input nicht korrekt ist, wird die Schleife immer wieder durchlaufen:
    while True:
        userInput = input(string)  # Input vom Nutzer.
        # Überprüfen, ob die Eingabe eine Zahl ist:
        if userInput.isdigit():
            n = float(userInput)  # Nehme den Userinput als n und wandele diesen in einen float Wert um.
            return n  # Rückgabe von n, wenn eine gültige Eingabe gemacht wurde.
        # Wenn es keine Gleitkommazahl war, dann gib Fehler aus und starte die Schleife von neuem:
        else:
            print("Ungültige Eingabe. Bitte geben Sie eine Gleitkommazahl ein.")


# Diese Funktion erweitert die Aufgabe, indem hier nach einem Input gefragt wird für eine ganze Zahl mit anpassbarem String.
def input_int(string):  # Übergabe des Anfragestrings als Parameter.
    # Solange der Input nicht korrekt ist, wird die Schleife immer wieder durchlaufen:
    while True:
        userInput = input(string)  # Input vom Nutzer.
        # Überprüfen, ob die Eingabe eine Zahl ist:
        if userInput.isdigit() and int(userInput) >= 0:
            n = int(userInput)  # Nehme den Userinput als n und wandele diesen in einen Integer Wert um.
            return n  # Rückgabe von n, wenn eine gültige Eingabe gemacht wurde.
        # Wenn es keine positive Ganzzahl war (inklusive 0), dann gib Fehler aus und starte die Schleife von neuem:
        else:
            print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")


# Ausführung der eigentlichen Aufgaben, wenn dieses Skript als "__main__" ausgeführt wird:
if __name__ == "__main__":
    points = input_int("Punkte eingeben:")  # Userinput der Anzahl der Punkt für die x-Werte.
    num = input_int("Wie viele Darstellungen für die Intensität soll es geben (min. 1)?")  # Userinput, wie viele Darstellungen es geben soll.
    start = -1  # Startwert der x-Achse.
    end = 10  # Endwert der x-Achse.
    x = np.arange(start, end, ((end - start) / points))  # Werte der x-Achse.

    plt.figure()  # Erstelle eine Figur.
    # Für jede Darstellung führe Folgendes aus:
    for num in range(1, num + 1, 1):
        lam = input_float("Lambda eingeben:")  # Userinput Lambda "lam".
        z = input_float("z eingeben:")  # Userinput Abstand "z".
        lamz = lam * z  # Berechnung von Lambda z.
        a = sqrt(2 / lamz)  # Term unter der Wurzel von u berechnen.
        intensity_values = []  # Intensitätswerte als leeres Arrays initialisieren.
        # Für jeden x-Wert führe Folgendes aus:
        for x_value in x:
            intensity = I(a, x_value)  # Intensitätsfunktion berechnen.
            intensity_values.append(intensity)  # Wert ans array anfügen.
        plt.plot(x, intensity_values, label=f'lam:{lam}, z:{z}')  # Plotte die Funktion.
    plt.title('Aufgabe C16')  # Titel für den Plot.
    plt.legend()  # Legende anzeigen.
    plt.grid()  # Raster anzeigen.
    plt.show()  # Plot anzeigen.
