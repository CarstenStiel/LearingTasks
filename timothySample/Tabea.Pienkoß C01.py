import math
import numpy as np
import matplotlib.pyplot as plt


# Aufgabe 2)
# Hier wird anstelle eines Array eine spezifische S-Funktion berechnet mithilfe von Rekursion (doppelte Genauigkeit).
# Diese Funktion berechnet SN1 rekursiv und gibt dies zurück
def s1_dp_recursive(N, n=1.0):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll
    # Wenn n größer als 2N geworden ist, dann gib 0 zurück
    if n > (2 * N):
        return 0.0
    # Wenn n kleiner als 2N ist, dann führe die Berechnung aus
    else:
        n = float(n)  # n in float für doppelte Genauigkeit umrechnen
        cal = pow((-1.0), n) * (n / (n + 1.0))  # Berechnung(calculation) = ((-1)^n)*(n / (n + 1))
        return cal + s1_dp_recursive(N, n + 1.0)  # Gibt die Berechnung aus und addiere mit der Nachfolgefunktion (Rekursion mit n+1)


# Diese Funktion berechnet S2 rekursiv und gibt dies zurück
def s2_dp_recursive(N, n=1.0):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll
    # Wenn n größer als N geworden ist, dann gib 0 zurück
    if n > N:
        return 0.0
    # Wenn n kleiner als N ist, dann führe die Berechnung aus
    else:
        n = float(n)  # n in float für doppelte Genauigkeit umrechnen
        cal = 1.0 / (2.0 * n * ((2.0 * n) + 1.0))  # Berechnung(calculation)
        return cal + s2_dp_recursive(N, n + 1.0)  # Gibt die Berechnung aus und addiere mit der Nachfolgefunktion (Rekursion mit n+1)


# Diese Funktion berechnet SN1 rekursiv und gibt dies zurück
def s1_sp_recursive(N, n=1.0):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll
    # Wenn n größer als 2N geworden ist, dann gib 0 zurück
    if n > (2 * N):
        return np.float32(0.0)
    # Wenn n kleiner als 2N ist, dann führe die Berechnung aus
    else:
        n = np.float32(n)  # n in float für doppelte Genauigkeit umrechnen
        cal = np.float32(pow((-1.0), n)) * (n / (n + np.float32(1.0)))  # Berechnung(calculation) = ((-1)^n)*(n / (n + 1))
        return cal + s1_dp_recursive(N, n + 1.0)  # Gibt die Berechnung aus und addiere mit der Nachfolgefunktion (Rekursion mit n+1)


# Diese Funktion berechnet S2 rekursiv und gibt dies zurück
def s2_sp_recursive(N, n=1.0):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll
    # Wenn n größer als N geworden ist, dann gib 0 zurück
    if n > N:
        return np.float32(0.0)
    # Wenn n kleiner als N ist, dann führe die Berechnung aus
    else:
        n = np.float32(n)  # n in float für doppelte Genauigkeit umrechnen
        cal = np.float32(1.0) / (np.float32(2.0) * n * ((np.float32(2.0) * n) + np.float32(1.0)))  # Berechnung(calculation)
        return cal + s2_dp_recursive(N, n + 1.0)  # Gibt die Berechnung aus und addiere mit der Nachfolgefunktion (Rekursion mit n+1)


# Aufgabe 3 aus C01 mit doppelter und einfacher Genauigkeit Varianten.
# Diese Funktion berechnet SN1 rekursiv und gibt dies zurück
def s1_sp(N):  # N wird als Parameter eingeben
    s1 = np.array([np.float32(0.0)])  # Initialisiere das Ergebnisarray mit dem Wert 0 (0 als einfache Genauigkeit)
    for i in range(1, N + 1):  # Für jedes n(i) von 1 bis N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
        # Da wir nur bis N rechnen, 2N aber benötigt wird, wird hier mit n und n + 1 gerechnet
        n = np.float32(2 * (i - 1) + 1)  # Da wir für 2N rechnen (doppelte berechnung ausführen) folgt → i = 1, dann rechnen wir n = 1 und 2 aus; i = 2, dann rechnen wir n = 3 und 4 aus, etc.
        cal1 = np.float32(np.float32(pow(-1, n)) * n / (n + 1.0))  # Berechnung von S1 für n
        cal2 = cal1 + np.float32(np.float32(pow(-1, n + 1)) * (n + 1.0) / (n + 2.0))  # Berechnung von S1 für n + 1, welches dann auf die vorherige Rechnung addiert wird
        res = s1[-1] + cal2  # Addiere S1 mit n und n + 1 für das nächste kleinere S1 zusammen
        s1 = np.append(s1, res)  # Anhängen des Ergebnisses an das Lösungsarray
    return s1  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnisarray zurück


# S2 mit einfacher Genauigkeit (single precision) berechnen → die einzelnen Variabelen muss mit float32 in einfache Genauigkeit umgerechnet werden!
def s2_sp(N):  # N wird als Parameter eingeben
    s2 = np.array([np.float32(0.0)])  # Initialisiere das Ergebnisarray mit dem Wert 0 (0 als einfache Genauigkeit)
    for i in range(1, N + 1):  # Für jedes n(i) von 1 bis 2N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
        n = np.float32(i)  # n in einfache Genauigkeit umrechnen
        res = s2[-1] + np.float32(1.0 / (2.0 * n * ((2.0 * n) + 1.0)))  # Berechnung auf das Ergebnis nächst kleinere S2 addieren
        s2 = np.append(s2, res)  # Anhängen des Ergebnisses an das Lösungsarray
    return s2  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnisarray zurück


# Wichtig: Die doppelte Genauigkeit ist bei Python von sich aus gegeben und muss NICHT mit float64 erreicht werden
# S1 mit doppelter Genauigkeit (double precision) berechnen
def s1_dp(N):  # N wird als Parameter eingeben
    s1 = np.array([0.0])  # Initialisiere das Ergebnisarray(result) mit dem Wert 0
    for i in range(1, N + 1):  # Für jedes n(i) von 1 bis N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
        # Da wir nur bis N rechnen, 2N aber benötigt wird, wird hier mit n und n + 1 gerechnet
        n = float(2 * (i - 1) + 1)  # Da wir für 2N rechnen (doppelte berechnung ausführen) folgt → i = 1, dann rechnen wir n = 1 und 2 aus; i = 2, dann rechnen wir n = 3 und 4 aus, etc.
        cal1 = float(pow(-1.0, n)) * n / (n + 1.0)  # Berechnung von S1 für n
        cal2 = cal1 + float(pow(-1.0, n + 1)) * (n + 1.0) / (n + 2.0)  # Berechnung von S1 für n + 1 und addiere diese zusammen
        res = s1[-1] + cal2  # Addiere S1 mit n und n + 1 für das nächste kleinere S1 zusammen
        s1 = np.append(s1, [res])  # Anfügen des S1 an das Ergebnisarray
    return s1  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnisarray zurück


# S2 mit doppelter Genauigkeit (double precision) berechnen → die einzelnen Variabelen muss mit float32 in einfache Genauigkeit umgerechnet werden!
def s2_dp(N):  # N als Parameter eingeben
    s2 = np.array([0.0])  # Initialisiere das Ergebnisarray mit dem Wert 0 (0 als einfache Genauigkeit)
    for i in range(1, N + 1):  # Für jedes n(i) von 1 bis 2N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
        n = float(i)  # Umrechnen von n in float für doppelte Genauigkeit
        res = s2[-1] + 1.0 / (2.0 * n * (2.0 * n + 1.0))  # Berechnung auf das Ergebnis nächst kleinere S2 addiere
        s2 = np.append(s2, res)  # Anfügen des S2 an das Ergebnisarray
    return s2  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnisarray zurück


# Werte berechnen für log10(|(SN1-SN2)/SN2|)
def ratios(s1_array, s2_array):
    func = np.array([])
    if len(s2_array) == len(s1_array):
        for i in range(1, len(s1_array)):
            term = np.abs(((s1_array[i] - s2_array[i]) / s2_array[i]))
            func = np.append(func, term)
        return func
    else:
        raise ValueError("Länge der Arrays nicht gleich!")


# Diese Funktion erweitert die SN Aufgabe, indem hier nach einem Input gefragt wird für N
def input_n():
    # Solange der Input nicht korrekt ist, wird die Schleife immer wieder durchlaufen
    while True:
        userInput = input("Geben Sie N ein (>=1): ")  # Input vom Nutzer
        # Überprüfen, ob die Eingabe eine Zahl ist und größer 0
        if userInput.isdigit() and int(userInput) >= 1:
            N = int(userInput)  # Nehme den Userinput als N und wandele diesen in einen Integer Wert um
            print(f"Die Eingabe war N = {N}")
            return N  # Rückgabe von N, wenn eine gültige Eingabe gemacht wurde
        # Wenn es keine positive Ganzzahl war, dann gib Fehler aus und starte die Schleife von neuem
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl größer als 1 ein.")


if __name__ == "__main__":
    N = input_n()

    print(f"Einfache Genauigkeit für N = {N}:")
    print(f"S1:{s1_sp_recursive(N)}")
    print(f"S2:{s2_sp_recursive(N)}")
    print(f"Doppelte Genauigkeit für N = {N}:")
    print(f"S1:{s1_dp_recursive(N)}")
    print(f"S2:{s2_dp_recursive(N)}")
    N_values = np.arange(1, N + 1, 1)  # Liste von N werten erzeugen

    # log-log-Plot erstellen
    plt.loglog(N_values, ratios(s1_dp(N), s2_dp(N)), label='doppelte Genauigkeit')
    # Legende und Achsentitel
    plt.legend()
    plt.xlabel('log10(N)')
    plt.ylabel('log10(|SN1 - SN2)/SN2|)')
    plt.title('Aufgabe3')

    # Plot anzeigen
    plt.grid()
    plt.show()
