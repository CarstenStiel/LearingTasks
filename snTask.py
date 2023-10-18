import numpy as np  # Import von Numpy


# Diese Funktion berechnet SN1 rekursiv und gibt dies zurück
def sn1Recursive(N, n=1):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll
    # Wenn N eine ganze Zahl mindestens der Größe eins ist, dann führe die Berechnung aus
    if isinstance(N, int) and N >= 1:
        # Wenn n größer als 2N geworden ist, dann gib 0 zurück
        if n > (2 * N):
            return 0
        # Wenn n kleiner als 2N ist, dann führe die Berechnung aus
        else:
            cal = pow((-1), n) * (n / (n + 1))  # Berechnung(calculation) = ((-1)^n)*(n / (n + 1))
            return cal + sn1Recursive(N,
                                      n + 1)  # Gibt die Berechung aus und addiere mit der Nachfolgefunktion (Rekursion mit n+1)
    # Wenn N keine ganze Zahl oder kleiner 1 ist, dann wird eine Exception geworfen
    else:
        raise ValueError("N muss eine ganze Zahl mindestens der Größe 1 sein!")


# Diese Funktion berechnet SN1 mit einer For-Schleife und gibt dies zurück
def sn1For(N):  # Nur N als Parameter eingeben
    # Wenn N eine ganze Zahl mindestens der Größe eins ist, dann führe die Berechnung aus
    if isinstance(N, int) and N >= 1:
        res = 0  # Initialisiere das Ergebnis(result) mit dem Wert 0
        for n in range(1, (
                                  2 * N) + 1):  # Für jedes n von 1 bis 2N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
            res += pow((-1), n) * (n / (n + 1))  # Addiere die Berechnung auf das Ergebnis
        return res  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnis zurück
    # Wenn N keine ganze Zahl oder kleiner 1 ist, dann wird eine Exception geworfen
    else:
        raise ValueError("N muss eine ganze Zahl mindestens der Größe 1 sein!")


# Diese Funktion berechnet SN2 rekursiv und gibt dies zurück
def sn2Recursive(N, n=1):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll
    # Wenn N eine ganze Zahl mindestens der Größe eins ist, dann führe die Berechnung aus
    if isinstance(N, int) and N >= 1:
        # Wenn n größer als N geworden ist, dann gib 0 zurück
        if n > N:
            return 0
        # Wenn n kleiner als N ist, dann führe die Berechnung aus
        else:
            cal = 1 / (2 * n * ((2 * n) + 1))  # Berechnung(calculation)
            return cal + sn2Recursive(N,
                                      n + 1)  # Gibt die Berechung aus und addiere mit der Nachfolgefunktion (Rekursion mit n+1)
    # Wenn N keine ganze Zahl oder kleiner 1 ist, dann wird eine Exception geworfen
    else:
        raise ValueError("N muss eine ganze Zahl mindestens der Größe 1 sein!")


# Diese Funktion berechnet SN2 mit einer For-Schleife und gibt dies zurück
def sn2For(N):  # Nur N als Parameter eingeben
    # Wenn N eine ganze Zahl mindestens der Größe eins ist, dann führe die Berechnung aus
    if isinstance(N, int) and N >= 1:
        res = 0  # Initialisiere das Ergebnis(result) mit dem Wert 0
        for n in range(1,
                       N + 1):  # Für jedes n von 1 bis N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
            res += (1 / (2 * n * ((2 * n) + 1)))  # Berechnung(calculation)
        return res  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnis zurück
    # Wenn N keine ganze Zahl oder kleiner 1 ist, dann wird eine Exception geworfen
    else:
        raise ValueError("N muss eine ganze Zahl mindestens der Größe 1 sein!")


# Diese Funktion gibt eine Eingabe in einfacher und doppelter Genauigkeit aus
# Hier kann man ggf auch noch prüfen, ob ein Zahlenwert eingegeben wurde!
def precision(res):
    print(f"Ergebnis: {res}")
    print(f"In einfacher Genauigkeit: {np.float32(res)}")
    print(f"In doppelter Genauigkeit: {np.float64(res)}")


# Diese Funktion gibt ein Ergebnis in einfacher Genauigkeit (32bit) zurück.
# Hier kann man ggf auch noch prüfen, ob ein Zahlenwert eingegeben wurde!
def singlePrecision(res):
    return np.float32(res)  #


# Diese Funktion gibt ein Ergebnis in doppelter Genauigkeit (64 bit) zurück.
# Hier kann man ggf auch noch prüfen, ob ein Zahlenwert eingegeben wurde!
# Diese Funktion dient nur der Vollständigkeit, da der Python Datentyp "float" doppelte Genauigkeit verwendet.
def doublePrecision(res):
    return np.float64(res)
