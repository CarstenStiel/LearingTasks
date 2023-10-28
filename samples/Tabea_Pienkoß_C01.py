"""
AUTHOR
    Tabea Pienkoß

VERSION
    1.1.1

Aufgabe C01
"""
# Imports
import numpy as np
import matplotlib.pyplot as plt


# Definition der Funktionen:
# Aufgabe 2)
# Hier wird mithilfe von Rekursion ein spezifischer S-Wert berechnet.
# Diese Funktion berechnet SN1 (einfache Genauigkeit) und gibt diesen Wert zurück.
def s1_sp(N, n=1.0):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll.
    # Wenn n größer als 2·N geworden ist, dann gib 0 zurück:
    if n > (2 * N):
        return np.float32(0.0)
    # Wenn n kleiner als 2·N ist, dann führe die Berechnung aus:
    else:
        n = np.float32(n)  # n in float für doppelte Genauigkeit umrechnen.
        cal = np.float32(pow((-1.0), n)) * (n / (n + np.float32(1.0)))  # Berechnung(calculation) = ((-1)^n)*(n / (n + 1)).
        return cal + s1_dp(N, n + 1.0)  # Gibt die Berechnung aus bzw. addiere mit der Nachfolgefunktion (Rekursion mit n+1).


# Diese Funktion berechnet S2 (einfache Genauigkeit) und gibt dies zurück.
def s2_sp(N, n=1.0):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll.
    # Wenn n größer als N geworden ist, dann gib 0 zurück:
    if n > N:
        return np.float32(0.0)
    # Wenn n kleiner als N ist, dann führe die Berechnung aus:
    else:
        n = np.float32(n)  # n in float für doppelte Genauigkeit umrechnen.
        cal = np.float32(1.0) / (np.float32(2.0) * n * ((np.float32(2.0) * n) + np.float32(1.0)))  # Berechnung(calculation).
        return cal + s2_dp(N, n + 1.0)  # Gibt die Berechnung aus bzw. addiere mit der Nachfolgefunktion (Rekursion mit n+1).


# Diese Funktion berechnet SN1 (doppelte Genauigkeit) und gibt dies zurück.
# Wichtig: Die doppelte Genauigkeit ist bei Python von sich aus bei float gegeben und muss NICHT mit float64 erreicht werden
def s1_dp(N, n=1.0):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll.
    # Wenn n größer als 2·N geworden ist, dann gib 0 zurück:
    if n > (2 * N):
        return 0.0
    # Wenn n kleiner als 2·N ist, dann führe die Berechnung aus:
    else:
        n = float(n)  # n in float für doppelte Genauigkeit umrechnen.
        cal = pow((-1.0), n) * (n / (n + 1.0))  # Berechnung(calculation) = ((-1)^n)*(n / (n + 1)).
        return cal + s1_dp(N, n + 1.0)  # Gibt die Berechnung aus bzw. addiere mit der Nachfolgefunktion (Rekursion mit n+1).


# Diese Funktion berechnet S2 (doppelte Genauigkeit) und gibt dies zurück.
def s2_dp(N, n=1.0):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll.
    # Wenn n größer als N geworden ist, dann gib 0 zurück:
    if n > N:
        return 0.0
    # Wenn n kleiner als N ist, dann führe die Berechnung aus:
    else:
        n = float(n)  # n in float für doppelte Genauigkeit umrechnen.
        cal = 1.0 / (2.0 * n * ((2.0 * n) + 1.0))  # Berechnung(calculation).
        return cal + s2_dp(N, n + 1.0)  # Gibt die Berechnung aus bzw. addiere mit der Nachfolgefunktion (Rekursion mit n+1).


# Aufgabe 3)
# Idee und teile der Umsetzung für die Array-Funktion stammen von @V. Ivanov (die eigene Funktion mittels Rekursion für die Array erstellung, wurde aus Performance gründen nicht gewählt).
# Berechne S1 und S2 mit einfacher und doppelter Genauigkeit als Array (für die Funktionswerte) und plotte die Funktion.
# Diese Funktion berechnet das SN1-Array (einfache Genauigkeit) und gibt dies zurück.
def s1_sp_arr(N):  # N wird als Parameter eingeben.
    s1 = np.array([np.float32(0.0)])  # Initialisiere das Ergebnisarray mit dem Wert 0 (0 als einfache Genauigkeit).
    # Für jedes n(i) von 1 bis N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist):
    for i in range(1, N + 1):
        # Da wir nur bis N rechnen, 2·N aber benötigt wird, wird hier mit n und n + 1 gerechnet.
        n = np.float32(2 * (i - 1) + 1)  # Da wir für 2·N rechnen (doppelte berechnung ausführen) folgt → i = 1, dann rechnen wir n = 1 und 2 aus; i = 2, dann rechnen wir n = 3 und 4 aus, etc.
        cal1 = np.float32(np.float32(pow(-1, n)) * n / (n + 1.0))  # Berechnung von S1 für n.
        cal2 = cal1 + np.float32(np.float32(pow(-1, n + 1)) * (n + 1.0) / (n + 2.0))  # Berechnung von S1 für n + 1, welches dann auf die vorherige Rechnung addiert wird.
        res = s1[-1] + cal2  # Addiere S1 mit n und n + 1 für das nächste kleinere S1 zusammen.
        s1 = np.append(s1, res)  # Anhängen des Ergebnisses an das Lösungsarray.
    return s1  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnisarray zurück.


# Diese Funktion berechnet das SN2-Array (einfache Genauigkeit) und gibt dies zurück.
def s2_sp_arr(N):  # N wird als Parameter eingeben.
    s2 = np.array([np.float32(0.0)])  # Initialisiere das Ergebnisarray mit dem Wert 0 (0 als einfache Genauigkeit).
    # Für jedes n(i) von 1 bis 2N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist):
    for i in range(1, N + 1):
        n = np.float32(i)  # n in einfache Genauigkeit umrechnen.
        res = s2[-1] + np.float32(1.0 / (2.0 * n * ((2.0 * n) + 1.0)))  # Berechnung auf das Ergebnis nächst kleinere S2 addieren.
        s2 = np.append(s2, res)  # Anhängen des Ergebnisses an das Lösungsarray.
    return s2  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnisarray zurück.


# Diese Funktion berechnet das SN1-Array (doppelte Genauigkeit) und gibt dies zurück.
def s1_dp_arr(N):  # N wird als Parameter eingeben.
    s1 = np.array([0.0])  # Initialisiere das Ergebnisarray(result) mit dem Wert 0.
    # Für jedes n(i) von 1 bis N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist):
    for i in range(1, N + 1):
        # Da wir nur bis N rechnen, 2·N aber benötigt wird, wird hier mit n und n + 1 gerechnet.
        n = float(2 * (i - 1) + 1)  # Da wir für 2·N rechnen (doppelte berechnung ausführen) folgt → i = 1, dann rechnen wir n = 1 und 2 aus; i = 2, dann rechnen wir n = 3 und 4 aus, etc.
        cal1 = float(pow(-1.0, n)) * n / (n + 1.0)  # Berechnung von S1 für n.
        cal2 = cal1 + float(pow(-1.0, n + 1)) * (n + 1.0) / (n + 2.0)  # Berechnung von S1 für n + 1 und addiere diese zusammen.
        res = s1[-1] + cal2  # Addiere S1 mit n und n + 1 für das nächste kleinere S1 zusammen.
        s1 = np.append(s1, [res])  # Anfügen des S1 an das Ergebnisarray.
    return s1  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnisarray zurück.


# Diese Funktion berechnet das SN2-Array (doppelte Genauigkeit) und gibt dies zurück.
def s2_dp_arr(N):  # N als Parameter eingeben.
    s2 = np.array([0.0])  # Initialisiere das Ergebnisarray mit dem Wert 0 (0 als einfache Genauigkeit).
    # Für jedes n(i) von 1 bis 2*N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist):
    for i in range(1, N + 1):
        n = float(i)  # Umrechnen von n in float für doppelte Genauigkeit.
        res = s2[-1] + 1.0 / (2.0 * n * (2.0 * n + 1.0))  # Berechnung auf das Ergebnis nächst kleinere S2 addiere.
        s2 = np.append(s2, res)  # Anfügen des S2 an das Ergebnisarray.
    return s2  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnisarray zurück.


# Diese Funktion berechnet die Funktionswerte.
def ratios(s1_array, s2_array):  # Übergabe der Arrays von S1 und S2 als Parameter.
    func = np.array([])  # Initialisierung eines leeren Ergebnis-Arrays.
    # Wenn beide Arrays gleich viele einträge haben, dann führe die Berechnung aus:
    if len(s2_array) == len(s1_array):
        # Für jeden Eintrag des Arrays, beginnend ab 1 (der 0te Eintrag diente nur der Berechnung und hat keine weitere Relevanz), führe die Berechnung aus:
        for i in range(1, len(s1_array)):
            term = np.abs(((s1_array[i] - s2_array[i]) / s2_array[i]))  # Berechne die Funktionswerte nach |(SN1-SN2)/SN2|.
            func = np.append(func, term)  # Füge die Funktionswerte dem Ergebnis-Array an.
        return func  # Gebe das Ergebnis-Array zurück.
    # Wenn die Arrays nicht gleich lang waren, dann werfe einen Fehler:
    else:
        raise ValueError("Länge der Arrays nicht gleich!")


# Zusatz:
# Diese Funktion erweitert die S Aufgabe, indem hier nach einem Input gefragt wird für N, solange bis eine Ganzzahl N >= 1 gewählt wurde.
def input_N():
    # Solange der Input nicht korrekt ist, wird die Schleife immer wieder durchlaufen:
    while True:
        userInput = input("Geben Sie N ein (>=1): ")  # Input vom Nutzer.
        # Überprüfen, ob die Eingabe eine Zahl ist und größer 0:
        if userInput.isdigit() and int(userInput) >= 1:
            N = int(userInput)  # Nehme den Userinput als N und wandele diesen in einen Integer Wert um.
            print(f"Die Eingabe war N = {N}")  # Ausgabe in der Konsole.
            return N  # Rückgabe von N, wenn eine gültige Eingabe gemacht wurde.
        # Wenn es keine positive Ganzzahl war, dann gib Fehler aus und starte die Schleife von neuem:
        else:
            print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl >= 1 ein.")


# Ausführung der eigentlichen Aufgaben, wenn dieses Skript als "__main__" ausgeführt wird:
if __name__ == "__main__":
    N = input_N()  # Eingabe von N als Userinput.

    # Aufgabe 2)
    # Ausgabe der einfachen und doppelten Genauigkeit für ein spezifisches S1 und S2.
    print(f"Einfache Genauigkeit für N = {N}:")
    print(f"S1:{s1_sp(N)}")
    print(f"S2:{s2_sp(N)}")
    print(f"Doppelte Genauigkeit für N = {N}:")
    print(f"S1:{s1_dp(N)}")
    print(f"S2:{s2_dp(N)}")

    # Aufgabe 3)
    # X Werte erstellen
    N_values = np.arange(1, N + 1, 1)  # Liste von N-Werten erzeugen

    # log-log-Plot erstellen
    plt.loglog(N_values, ratios(s1_sp_arr(N), s2_sp_arr(N)), label='einfache Genauigkeit')  # Für einfache Genauigkeit
    plt.loglog(N_values, ratios(s1_dp_arr(N), s2_dp_arr(N)), label='doppelte Genauigkeit')  # Für doppelte Genauigkeit
    # Plot bearbeiten
    plt.legend()  # Legende anzeigen
    plt.xlabel('log10(N)')  # x-Achse labeln
    plt.ylabel('log10(|SN1 - SN2)/SN2|)')  # y-Achse labeln
    plt.title('Aufgabe3')  # Dem Plot einen Titel geben
    plt.grid()  # Dem Plot ein Gitter hinzufügen
    plt.show()  # Plot anzeigen
