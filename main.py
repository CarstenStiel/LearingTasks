import numpy as np  # Import von Numpy


# Diese Funktion berechnet die Schritte und gibt diese als Array zurück
def calculate_steps(start, stop, step):
    arr = []  # Initialisierung eines leeren Arrays
    current = start  # Derzeitiger Schritt initialisiert mit dem Start

    if step <= 0:  # Wenn die Schrittweite kleiner oder gleich Null 0 ist, dann wird ein Fehler geworfen(Exception ValueError)
        raise ValueError("Die Schrittweite darf nicht 0 oder kleiner sein.")
    elif stop <= start:  # Ansonsten, wenn Stop kleiner als der Start ist, soll ein Fehler geworfen werden(Exception ValueError)
        raise ValueError("Start muss größer als Stop sein.")
    else:  # Ansonsten, führe folgende While-Schleife aus
        while current < stop:  # Solange, der derzetige Wert kleiner ist als stop führe Folgendes aus:
            arr.append(current)  # Füge denn derzeitigen Wert hinten das Array an
            current += step  # Erhöhe den derzeitigen Wert und die Schrittweite

    return arr  # Sobald die der derzeitige Wert gleich oder größer dem Stop ist, wird das Array hier zurückgegeben


# Dies ist die "main" Klasse von der aus das Program gestartet wird
if __name__ == '__main__':
    # Mit arange
    arr1 = np.arange(2, 10, 0.5)
    print(arr1)
    print(len(arr1))

    # Ohne Arange, aber mit der geschriebenen Funktion
    arr2 = calculate_steps(2, 10, 0.5)
    print(arr2)
    print(len(arr2))
    print(__name__)