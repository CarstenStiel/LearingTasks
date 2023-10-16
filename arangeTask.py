#arange Aufgabe: mit und ohne arange (numpy) ein Schrittintervall und Schrittmenge angegeben

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