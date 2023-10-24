import math
import numpy as np
import matplotlib.pyplot as plt


# Aufgabe 1


# Aufgabe 2 aus C01 in 2 verschiedenen Varianten.
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


if __name__ == "__main__":
    N = 100

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
