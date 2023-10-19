import numpy as np  # Import von Numpy
import matplotlib.pyplot as plt
import math
from decimal import Decimal


# Aufgabe 2
# Im Folgenden werden die SN Funktionen mit einer For-Schleife berechnet → für rekursion, siehe extensions.py.
# Diese Funktion berechnet SN1 mit einer For-Schleife und gibt dies zurück
def sn1For(N):  # Nur N als Parameter eingeben
    # Wenn N eine ganze Zahl mindestens der Größe eins ist, dann führe die Berechnung aus
    if isinstance(N, int) and N >= 1:
        res = 0.0  # Initialisiere das Ergebnis(result) mit dem Wert 0
        for n in range(1, (2 * N) + 1, 1):  # Für jedes n von 1 bis 2N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
            term1 = float(n) / (float(n) + 1.0)
            res += float(pow((-1), n)) * term1  # Addiere die Berechnung auf das Ergebnis
        return res  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnis zurück
    # Wenn N keine ganze Zahl oder kleiner 1 ist, dann wird eine Exception geworfen
    else:
        raise ValueError("N muss eine ganze Zahl mindestens der Größe 1 sein!")


# Diese Funktion berechnet SN2 mit einer For-Schleife und gibt dies zurück
def sn2For(N):  # Nur N als Parameter eingeben
    # Wenn N eine ganze Zahl mindestens der Größe eins ist, dann führe die Berechnung aus
    if isinstance(N, int) and N >= 1:
        res = 0  # Initialisiere das Ergebnis(result) mit dem Wert 0
        for n in range(1, N + 1):  # Für jedes n von 1 bis N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
            res += (1 / (2 * n * ((2 * n) + 1)))  # Berechnung(calculation)
        return res  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnis zurück
    # Wenn N keine ganze Zahl oder kleiner 1 ist, dann wird eine Exception geworfen
    else:
        raise ValueError("N muss eine ganze Zahl mindestens der Größe 1 sein!")


# Diese Funktion gibt ein Ergebnis in einfacher Genauigkeit (32bit) zurück.
# Hier kann man ggf auch noch prüfen, ob ein Zahlenwert eingegeben wurde!
def singlePrecision(res):
    return np.float32(res)


# Diese Funktion gibt ein Ergebnis in doppelter Genauigkeit (64 bit) zurück.
# Hier kann man ggf auch noch prüfen, ob ein Zahlenwert eingegeben wurde!
# Diese Funktion dient nur der Vollständigkeit, da der Python Datentyp "float" doppelte Genauigkeit verwendet.
def doublePrecision(res):
    return np.float64(res)


# Aufgabe 3
def snPlot(start, stop):
    if isinstance(start, int) and isinstance(stop, int) and 1 <= start <= stop:
        xpoints = np.array([])
        ypoints = np.array([])
        for N in range(start, stop + 1):
            x = math.log10(N)
            y = math.log10(abs((sn1For(N) - sn2For(N)) / sn2For(N)))  # Fall 0 oder negativ, ist kein log möglich
            xpoints = np.append(xpoints, x)
            ypoints = np.append(ypoints, y)
        plt.plot(xpoints, ypoints)
        plt.show()
    else:
        raise ValueError("Ungültige Argumente: 'start' und 'stop' müssen Ganzzahlen sein, mit 1 <= start <= stop.")


def test(start, stop):
    for N in range(start, stop + 1):
        print(abs((sn1For(N) - sn2For(N))))
