"""
AUTHOR
    Tabea Pienkoß

VERSION
    1.0.

Aufgabe C04a
"""
# Imports:
import math
import numpy as np
from matplotlib import pyplot as plt


# Definition der Funktionen:
# Diese Funktion gibt für ein spezielles x die berechnete Funktion des Integrals zurück.
def integral_func(x):  # Übergebe x als Parameter
    return pow(x, 4) * math.log(x + math.sqrt(pow(x, 2) + 1))


# Diese Funktion berechnet mittels Trapezverfahren den genährten Wert des Integrals.
def trapezoidal_method(i):  # Übergebe die gewünschten Stützstellen "i" als Parameter.
    n = i + 1  # Rechne n (Anzahl der Trapeze) als Stützstellen + 1.
    a = 0.0  # Untere Grenze des Intergrals.
    b = 2.0  # Obere Grenze des Intergrals.
    h = (b - a) / n  # Schrittweite des Trapezverfahren berechnen.
    mid_term = 0.0  # Mittlere Term des Trapezverfahrens (welcher mit 2 multipliziert werden soll) initialisiert mit 0
    # Für jedes Trapez führe Folgendes aus:
    for i in range(1, n, 1):
        x = h * i  # Berechne den benötigten Schritt.
        mid_term += integral_func(x)  # Füge die berechnete Integralfunktion mit dem aktuellen Schritt dem mittleren Term hinzu.
    term = (h / 2) * (integral_func(a) + (2 * mid_term) + integral_func(b))  # Trapezverfahren endgültige Berechnung.

    return term  # Gebe die endgültige Berechnung zurück.


# Diese Funktion berechnet ein Array aller berechneten Trapezverfahren bis n Stützstellen.
def trapezoidal_arr(n):  # Übergebe die Anzahl der Stützstellen.
    arr = []  # Initialisiere ein leeres Ergebnisarray.
    # Für jede Stützstelle führe Folgendes aus:
    for i in range(0, n + 1, 1):
        arr.append(trapezoidal_method(i))  # Füge jede Berechnung für die Stützstelle dem Ergebnisarray hinzu.

    return arr  # Gebe das Ergebnisarray nach beendeter For-Schleife zurück.


# Diese Funktion berechnet ein Array aller der relativen Fehler bis n Stützstellen.
def relative_error_arr(trap_arr, integral):  # Übergebe des Arrays der Trapezverfahren bis n Stützstellen und das zu vergleichende Integral.
    arr = []  # Initialisiere ein leeres Ergebnisarray.
    # Für jede Stützstelle führe Folgendes aus:
    for i in range(0, len(trap_arr), 1):
        rel_error = abs(trap_arr[i] - integral) / integral  # Berechne den relativen Fehler.
        arr.append(rel_error)  # Füge den relativen Fehler dem Ergebnisarray hinzu.

    return arr  # Gebe das Ergebnisarray nach beendeter For-Schleife zurück.


# Zusatz:
# Diese Funktion erweitert die Aufgabe, indem hier nach einem Input gefragt wird für die Anzahl der Stützstellen "n">= 0.
def input_n():
    # Solange der Input nicht korrekt ist, wird die Schleife immer wieder durchlaufen:
    while True:
        userInput = input("Geben Sie die Anzahl der Stützstellen ein: ")  # Input vom Nutzer.
        # Überprüfen, ob die Eingabe eine Zahl ist und Eingabe >= 0:
        if userInput.isdigit() and int(userInput) >= 0:
            n = int(userInput)  # Nehme den Userinput als n und wandele diesen in einen Integer Wert um.
            print(f"Die Eingabe für die Anzahl der Stützstellen war n = {n}")  # Ausgabe in der Konsole.
            return n  # Rückgabe von n, wenn eine gültige Eingabe gemacht wurde.
        # Wenn es keine positive Ganzzahl war (inklusive 0), dann gib Fehler aus und starte die Schleife von neuem:
        else:
            print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl >= 0 ein.")


# Ausführung der eigentlichen Aufgaben, wenn dieses Skript als "__main__" ausgeführt wird:
if __name__ == "__main__":
    n = input_n()  # Anzahl der Stützstellen als Userinput.
    integral = (8.0 - 40.0 * math.sqrt(5.0) + 480.0 * math.asinh(2.0)) / 75.0  # Zu vergleichendes Integral.
    rel_err_arr = relative_error_arr(trapezoidal_arr(n), integral)  # Arrays der relativen Fehler bis zur eingeben Stützstelle.

    # Ausgabe.
    print(f"Für n = {n} lautet die numerisch Berechnung mittels Trapezverfahren: {trapezoidal_method(n)}")

    print(f"Im Vergleich zu I={integral} haben wir hier einen Fehler von:")
    print(f"Absolut:{trapezoidal_method(n) - integral}")
    print(f"Relativ:{rel_err_arr[-1]}")

    # Plotten der relativen Fehler in Abhängigkeit er Stützstellen.
    x_arr = np.arange(0, n + 1, 1)  # x-Achsen Werte (Stützstellen).
    y_arr = rel_err_arr  # y-Achsen Werte (relativer Fehler).

    plt.figure()  # Erstellung einer Figur.
    plt.plot(x_arr, y_arr, marker='o')  # Plotten der x und y Werte.
    plt.xlabel('Stützstellen')  # x-Achse mit 'Stützstellen' Labeln.
    plt.ylabel('relativer Fehler')  # y-Achse mit 'relativer Fehler' Labeln.
    plt.title('Aufgabe C04a')  # Der Figur einen Titel geben.
    plt.grid()  # Raster erstellen.
    plt.show()  # Anzeigen des Plots.
