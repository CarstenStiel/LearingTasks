 #Schrittweite ohne Numpy
import numpy as np


# Diese Funktion berechnet die Schritte und gibt diese als Array zurück
def calculate_steps(start, stop, step):
    arr = []  # Initialisierung eines leeren Arrays
    current = start  # Derzeitiger Schritt initialisiert mit dem Start

    if step <= 0 and start <= stop:  # Fehler bei negativer Schrittweite und start kleiner stop
        raise ValueError("Die Schrittweite darf nicht 0 oder kleiner sein.")
    elif step >= 0 and stop <= start:  # Fehler bei postiver Schrittweite und stop kleiner start
        raise ValueError("Start muss größer als Stop sein.")
    else:  # Ansonsten, führe folgende While-Schleife aus
        while not current == stop:  # Solange, der derzeitige Wert kleiner ist als stop führe Folgendes aus:
            arr.append(current)  # Füge denn derzeitigen Wert hinten das Array an
            current += step  # Erhöhe den derzeitigen Wert und die Schrittweite

    return arr  # Sobald die der derzeitige Wert gleich oder größer dem Stop ist, wird das Array hier zurückgegeben
if __name__ == '__main__':
 arr2 = calculate_steps(10, 2, -0.5)
 print("Ohne arange-Funktion:")
 print(arr2)
 print(len(arr2))


#Schrittweite mit Numpy
arr1 = np.arange (start = 2, stop = 1000, step = 0.7)
print("Mit arange-Funktion")
print(arr1)
print(len(arr1))

