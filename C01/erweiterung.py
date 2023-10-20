import numpy as np
import aufgabe2 as a2


# Aufgabe 2)
# Hier wird anstelle eines Array eine spezifische S-Funktion berechnet mithilfe von Rekursion (doppelte Genauigkeit).
# Diese Funktion berechnet SN1 rekursiv und gibt dies zurück
def s1_dp_recursive(N, n=1.0):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll
    # Wenn N eine ganze Zahl mindestens der Größe eins ist, dann führe die Berechnung aus
    if isinstance(N, int) and N >= 1:
        # Wenn n größer als 2N geworden ist, dann gib 0 zurück
        if n > (2 * N):
            return 0
        # Wenn n kleiner als 2N ist, dann führe die Berechnung aus
        else:
            n = float(n)  # n in float für doppelte Genauigkeit umrechnen
            cal = pow((-1.0), n) * (n / (n + 1.0))  # Berechnung(calculation) = ((-1)^n)*(n / (n + 1))
            return cal + s1_dp_recursive(N, n + 1.0)  # Gibt die Berechnung aus und addiere mit der Nachfolgefunktion (Rekursion mit n+1)
    # Wenn N keine ganze Zahl oder kleiner 1 ist, dann wird eine Exception geworfen
    else:
        raise ValueError("N muss eine ganze Zahl mindestens der Größe 1 sein!")


# Diese Funktion berechnet S2 rekursiv und gibt dies zurück
def s2_dp_recursive(N, n=1.0):  # Nur N als Parameter eingeben, da n beim Start 1 bleiben soll
    # Wenn N eine ganze Zahl mindestens der Größe eins ist, dann führe die Berechnung aus
    if isinstance(N, int) and N >= 1:
        # Wenn n größer als N geworden ist, dann gib 0 zurück
        if n > N:
            return 0
        # Wenn n kleiner als N ist, dann führe die Berechnung aus
        else:
            n = float(n)  # n in float für doppelte Genauigkeit umrechnen
            cal = 1.0 / (2.0 * n * ((2.0 * n) + 1.0))  # Berechnung(calculation)
            return cal + s2_dp_recursive(N, n + 1.0)  # Gibt die Berechnung aus und addiere mit der Nachfolgefunktion (Rekursion mit n+1)
    # Wenn N keine ganze Zahl oder kleiner 1 ist, dann wird eine Exception geworfen
    else:
        raise ValueError("N muss eine ganze Zahl mindestens der Größe 1 sein!")


# Weitere Funktionen:
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


# Diese Funktion berechnet für einen N wert, alle S-Funktionen und erstellt für diese zwei Dateien in der diese gespeichert werden
def output_files(sp_filename, dp_filename, path, N):  # Übergabe der Namen und des Pfades und die Namen für die Dateien der einfachen und doppelten Genauigkeit
    sp_filepath = path + "/" + sp_filename  # Erstellung des Pfades für die Datei der einfachen Genauigkeit
    dp_filepath = path + "/" + dp_filename  # Erstellung des Pfades für die Datei der doppelten Genauigkeit
    N_len = len(str(N))  # Länge der eingegebenen Zahl, damit die N-Spalte der Datei das richtige Format hat
    s1_sp_arr = a2.s1_sp(N)  # Array für die S1 Funktion der einfachen Genauigkeit
    s2_sp_arr = a2.s2_sp(N)  # Array für die S2 Funktion der einfachen Genauigkeit
    diff_sp_array = np.array([np.float32(0)])  # Array für die Differenz von S1 und S2 mit einfacher Genauigkeit
    s1_dp_arr = a2.s1_dp(N)  # Array für die S1 Funktion der doppelten Genauigkeit
    s2_dp_arr = a2.s2_dp(N)  # Array für die S1 Funktion der doppelten Genauigkeit
    diff_dp_array = np.array([0.0])  # Array für die Differenz von S1 und S2 mit doppelter Genauigkeit
    # Erstellen/bearbeiten der Datei für die einfache Genauigkeit
    with open(f"{sp_filepath}.txt", "w") as outputfile:  # Öffnen/erstellen einer Textdatei(.txt) im angegebenen Pfad
        outputfile.write('{:{N_len}s} {:10s} {:10s} {:10s} \n'.format("N", "s1", "s2", "diff", N_len=N_len))  # In die erste Zeile werden die "Überschriften" geschrieben
        # Für jeden Eintrag von N
        for n in range(1, N + 1):
            diff_sp = abs(s1_sp_arr[n] - s2_sp_arr[n])  # Berechne den Betrag (|s1-s2|) von s1 und s2
            diff_sp_array = np.append(diff_sp_array, diff_sp)  # Füge die Berechnung der Differenz dem Differenzarray hinzu
            outputfile.write(f'{str(n):{N_len}s} {s1_sp_arr[n]:.8f} {s2_sp_arr[n]:.8f} {diff_sp:.8f} \n')  # Schreibe die Werte in die Datei
    print(f'Datei "{sp_filename}" für single-precision mit N = {N}, wurde unter {sp_filepath} erstellt/bearbeitet!')  # Ausgabe in der Konsole, wenn die For-Schleife erfolgreich beendet wurde
    # Erstellen/bearbeiten der Datei für die doppelte Genauigkeit
    with open(f"{dp_filepath}.txt", "w") as outputfile:  # Öffnen/erstellen einer Textdatei(.txt) im angegebenen Pfad
        outputfile.write('{:{N_len}s} {:18s} {:18s} {:18s} \n'.format("N", "s1", "s2", "diff", N_len=N_len))  # In die erste Zeile werden die "Überschriften" geschrieben
        # Für jeden Eintrag von N
        for n in range(1, N + 1):
            diff_dp = abs(s1_dp_arr[n] - s2_dp_arr[n])  # Berechne den Betrag (|s1-s2|) von s1 und s2
            diff_dp_array = np.append(diff_dp_array, diff_dp)  # Füge die Berechnung der Differenz dem Differenzarray hinzu
            outputfile.write(f'{str(n):{N_len}s} {s1_dp_arr[n]:.16f} {s2_dp_arr[n]:.16f} {diff_dp:.16f} \n')  # Schreibe die Werte in die Datei
    print(f'Datei "{dp_filename}" für double-precision mit N = {N}, wurde unter {dp_filepath} erstellt/bearbeitet!')  # Ausgabe in der Konsole, wenn die For-Schleife erfolgreich beendet wurde
