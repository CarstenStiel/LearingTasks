import math
import numpy as np
import matplotlib.pyplot as plt
#Aufgabe 2 aus C01 in 2 verschiedenen Varianten
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
            return cal + sn1Recursive(N, n + 1)  # Gibt die Berechnung aus und addiere mit der Nachfolgefunktion (Rekursion mit n+1)
    # Wenn N keine ganze Zahl oder kleiner 1 ist, dann wird eine Exception geworfen
    else:
        raise ValueError("N muss eine ganze Zahl mindestens der Größe 1 sein!")


# Diese Funktion berechnet SN1 mit einer For-Schleife und gibt dies zurück
def sn1For(N):  # Nur N als Parameter eingeben
    # Wenn N eine ganze Zahl mindestens der Größe eins ist, dann führe die Berechnung aus
    if isinstance(N, int) and N >= 1:
        res = 0  # Initialisiere das Ergebnis(result) mit dem Wert 0
        for n in range(1, (2 * N) + 1):  # Für jedes n von 1 bis 2N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
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
        for n in range(1, N + 1):  # Für jedes n von 1 bis N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
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
    return np.float32(res)


# Diese Funktion gibt ein Ergebnis in doppelter Genauigkeit (64 bit) zurück.
# Hier kann man ggf auch noch prüfen, ob ein Zahlenwert eingegeben wurde!
# Diese Funktion dient nur der Vollständigkeit, da der Python Datentyp "float" doppelte Genauigkeit verwendet.
def doublePrecision(res):
    return np.float64(res)

    # Aufgabe SN
    # SN1


res1Rec = sn1Recursive(6)
res1For = sn1For(6)
print("SN1-Genauigkeiten mit Rekursion:")  # Ausgabe
print(f"In einfacher Genauigkeit: {singlePrecision(res1Rec)}")  # SN1 (rekursiv) in einfacher Genauigkeit berechnet (siehe snTask) und ausgegeben
print(f"In doppelter Genauigkeit: {doublePrecision(res1Rec)}")  # SN1 (rekursiv) in doppelter Genauigkeit berechnet (siehe snTask) und ausgegeben
print("SN1-Genauigkeiten mit For-Schleife:")
print(f"In einfacher Genauigkeit: {singlePrecision(res1For)}")  # SN1 (For-Schleife) in einfacher Genauigkeit berechnet (siehe snTask) und ausgegeben
print(f"In doppelter Genauigkeit: {doublePrecision(res1For)}")  # SN1 (For-Schleife) in doppelter Genauigkeit berechnet (siehe snTask) und ausgegeben

# SN2
res2Rec = sn2Recursive(2)  # SN2 rekursiv berechnet
res2For = sn2For(2)  # SN2 mittels For-Schleife berechnet
print("SN2-Genauigkeiten:")
precision(res2Rec)  # SN2 (rekursiv) in einfacher und doppelter Genauigkeit ausgeben (siehe snTask)
precision(res2For)  # SN2 (For-Schleife) in einfacher und doppelter Genauigkeit ausgeben (siehe snTask)
# SN1 Input
res1Rec = sn1Recursive(6)  # SN1 rekursiv berechnet
print("SN1-Genauigkeiten mit Rekursion:")  # Ausgabe
print(f"In einfacher Genauigkeit: {singlePrecision(res1Rec)}")  # SN1 (rekursiv) in einfacher Genauigkeit berechnet (siehe snTask) und ausgegeben
print(f"In doppelter Genauigkeit: {doublePrecision(res1Rec)}")  # SN1 (rekursiv) in doppelter Genauigkeit berechnet (siehe snTask) und ausgegeben

#Aufgabe 3 aus C01: Graph Plot
#df = pd.DataFrame({'x' : ([abs((((-1), n) * (n / (n + 1))-(1 / (2 * n * ((2 * n) + 1))))/(1 / (2 * n * ((2 * n) + 1))))],
                   #'y' : [N])})

# Funktionen definieren
def SN1(N):
    if isinstance(N, int) and N >= 1:
        # Wenn n größer als N geworden ist, dann gib 0 zurück
        if n > N:
            return 0
        # Wenn n kleiner als N ist, dann führe die Berechnung aus
        else:
            cal = 1 / (2 * n * ((2 * n) + 1))  # Berechnung(calculation)
            return cal + sn2Recursive(N,n + 1)
def SN2 (N):
    if isinstance(N, int) and N >= 1:
        res = 0  # Initialisiere das Ergebnis(result) mit dem Wert 0
        for n in range(1, N + 1):  # Für jedes n von 1 bis N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
            res += (1 / (2 * n * ((2 * n) + 1)))  # Berechnung(calculation)
        return res

N_values = np.arange(1, 1000001, 1) #Liste von N werten erzeugen

#Werte berechnen für log10(|(SN1-SN2)/SN2|)
def log_ratios(): np.log10(np.abs((SN1(N_values) - SN2(N_values))/SN2(N_values)))
#log-log-Plot erstellen
plt.loglog(N_values, log_ratios, label='log10(|SN1 - SN2)/SN2|)')
#Legende und Achsentitel
plt.legend()
plt.xlabel('log10(N)')
plt.ylabel('log10(|SN1 - SN2)/SN2|)')

#Plot anzeigen
plt.grid()
plt.show()