"""
AUTHOR
    Tabea Pienkoß

VERSION
    1.1

Aufgabe C00
"""
# Imports
import numpy as np


# Definition der Funktionen.
# Diese Funktion berechnet die Schritte zwischen einem Start und Endpunkt mittels Schrittweite und gibt diese als Array zurück.
def calculate_steps(start, stop, step):  # Übergabe von Startpunkt, Endpunkt und Schrittweite.
    # Wenn die Parameter numerisch sind, dann führe die Funktion aus:
    if isinstance(start, (int, float)) and isinstance(stop, (int, float)) and isinstance(step, (int, float)):
        arr = []  # Initialisierung eines leeren Arrays für die Schritte.
        current = start  # Derzeitiger Schritt, initialisiert mit dem Start.

        # Bei positiver Schrittweite und Startpunkt ≤ Endpunkt:
        if step > 0 and start <= stop:
            # Solange der derzeitige Schritt den Endpunkt nicht überschreitet oder gleich ist:
            while not current >= stop:
                arr.append(current)  # Füge denn derzeitigen Schritt hinten das Array an.
                current += step  # Erhöhe den derzeitigen Schritt um die Schrittweite.

            return arr  # Sobald die Schleife beendet wurde, wird das Array zurückgegeben.
        # Bei negativer Schrittweite und Endpunkt ≤ Startpunkt:
        elif step < 0 and stop <= start:
            # Solange der derzeitige Schritt den Endpunkt nicht unterschreitet oder gleich ist:
            while not current <= stop:
                arr.append(current)  # Füge denn derzeitigen Schritt hinten das Array an.
                current += step  # Verringere den derzeitigen Schritt um die Schrittweite.

            return arr  # Sobald die Schleife beendet wurde, wird das Array zurückgegeben.
        # Ansonsten, gebe einen der folgenden Fehler zurück:
        else:
            # Fehler, wenn die Schrittweite 0 ist:
            if step == 0:
                raise ValueError("Die Schrittweite darf nicht 0 sein!")
            # Fehler bei negativer Schrittweite und Startpunkt < Endpunkt:
            elif start < stop:
                raise ValueError("Wenn der Startpunkt < Endpunkt ist, dann muss die Schrittweite positiv sein!")
            # Fehler bei positiver Schrittweite und Endpunkt < Startpunkt:
            else:
                raise ValueError("Wenn der Endpunkt < Startpunkt ist, dann muss die Schrittweite negativ sein!")
    # Wenn die Parameter nicht numerisch sind, dann werfe eine Fehlermeldung:
    else:
        raise TypeError("Nur numerische Werte als Parameter erlaubt!")


# Ausführung der eigentlichen Aufgabe:
if __name__ == '__main__':
    # Schritte und Schritte insgesamt mit Numpy.
    steps1 = np.arange(start=0, stop=30, step=3)  # Berechnung und Speicherung des Arrays mit den Schritten
    steps1_count = len(steps1)  # Berechnung und Speicherung der Schritte insgesamt, indem die Länge des Arrays betrachtet wird.
    # Ausgabe
    print("Mit arange-Funktion")
    print(f"Die ersten 5 Schritte: {steps1[:5]}")
    print(f"Schritte insgesamt: {steps1_count}")

    # Schritte und Schritte insgesamt ohne Numpy.
    steps2 = calculate_steps(start=0, stop=30, step=3)  # Berechnung und Speicherung des Arrays mit den Schritten.
    steps2_count = len(steps2)  # Berechnung und Speicherung der Schritte insgesamt, indem die Länge des Arrays betrachtet wird.
    # Ausgabe
    print("Ohne arange-Funktion:")
    print(f"Die ersten 5 Schritte: {steps2[:5]}")
    print(f"Schritte insgesamt: {steps2_count}")
