import numpy as np


# Aufgabe C01.) 2)
# Erweiterung durch Rekursion anstelle der For-Schleife
# diese Funktion berechnet SN1 rekursiv und gibt dies zurück
def sn1Recursive(N, n=1):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll
    # Wenn N eine ganze Zahl mindestens der Größe eins ist, dann führe die Berechnung aus
    if isinstance(N, int) and N >= 1:
        # Wenn n größer als 2N geworden ist, dann gib 0 zurück
        if n > (2 * N):
            return 0
        # Wenn n kleiner als 2N ist, dann führe die Berechnung aus
        else:
            cal = pow((-1), n) * (n / (n + 1))  # Berechnung(calculation) = ((-1)^n)*(n / (n + 1))
            return cal + sn1Recursive(N, n + 1)  # Gibt die Berechnung aus und addiere mit der Nachfolgefunktion (Rekursion mit n+1)
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


# Diese Funktion erweitert die SN Aufgabe, indem hier nach einem Input gefragt wird für N
def inputN():
    # Solange der Input nicht korrekt ist, wird die Schleife immer wieder durchlaufen
    while True:
        userInput = input("Geben Sie N ein (>=1): ")  # Input vom Nutzer
        # Überprüfen, ob die Eingabe eine Zahl ist
        if userInput.isdigit():
            N = int(userInput)  # Wenn es eine Zahl war, dann wandele in einen Integer wert um
            # Wenn N größer gleich 1, dann gib n zurück
            if N >= 1:
                print(f"Die Eingabe war N = {N}")
                return N  # Rückgabe von N, wenn eine gültige Eingabe gemacht wurde
        # Wenn es keine positive Ganzzahl war, dann gib Fehler aus und starte die Schleife von neuem
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl größer als 1 ein.")


# Diese Funktion gibt eine Eingabe in einfacher und doppelter Genauigkeit aus
# Hier kann man ggf auch noch prüfen, ob ein Zahlenwert eingegeben wurde!
def precision(res):
    print(f"Ergebnis: {res}")
    print(f"In einfacher Genauigkeit: {np.float32(res)}")
    print(f"In doppelter Genauigkeit: {np.float64(res)}")
