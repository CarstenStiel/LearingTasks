# Imports aus anderen Dateien und packages
import sys  # Import von Systemspezifischen Parametern und Funktionen
import os  # Import von Bertriebssystem spezifischen Parametern und Funktionen

sys.path.append("C01/")  # Füge das Verzeichnis C01 zum Modul-Suchpfad hinzu
import aufgabe2 as a2  # Import von Aufgabe 2
import aufgabe3 as a3  # Import von Aufgabe 3
import erweiterung as ext  # Import von nicht relevanten Erweiterungen für Aufgabe 2
import sampleSolution as sample  # Import der Musterlösung

# Dies ist die "main Klasse" von der aus das Program gestartet wird
if __name__ == '__main__':
    """
    # Aufgabe arange
    # Mit arange
    arr1 = np.arange(10, 2, -0.5)
    print("Mit arange-Funktion:")
    print(arr1)
    print(len(arr1))

    # Ohne Arange, aber mit der geschriebenen Funktion
    arr2 = calculate_steps(10, 2, -0.5)
    print("Ohne arange-Funktion:")
    print(arr2)
    print(len(arr2))
    """
    """
    # Aufgabe 2, Musterlösung
    os.chdir("C01/")  # Wechseln des Ordners zu C01, damit im ouputverzeichnis die Dateien erstellt werden können
    sample.test()
    os.path.dirname("C:\\Users\\timot\\Desktop\\LearingTasks")  # Wechsel zurück zum ursprünglichem Verzeichnis
    """
    # Aufgabe 2, eigene Lösung.
    # Hier werden Arrays mit den Lösungen der S-Funktionen bis N erstellt und ausgegeben → Zum Beispiel für S1N: [0, S11, S12, S13] für N = 3 (siehe C01/aufgabe2.py).
    # Dies richtet sich nach der Musterlösung!
    # Um ein spezifisches S auszurechnen, siehe C01/erweiterung.py
    N = ext.input_n()  # Eingabe von N mit Userinput (C01/erweiterung.py). Die Input-Funktion kann man auch durch ein selbst gewähltes N ersetzen (z.B. nächste Zeile)
    # N = 5
    print(f"Arrays der einfachen und doppelten Genauigkeit für S1 und S2 mit N = {N}")
    print("Einfache Genauigkeit")
    print(f"S1: {a2.s1_sp(N)}")
    print(f"S2: {a2.s2_sp(N)}")
    print("Doppelte Genauigkeit")
    print(f"S1: {a2.s1_dp(N)}")
    print(f"S2: {a2.s2_dp(N)}")
    # Zusatz, erstellen von den Dateien
    ext.output_file(filename="sp_output", path="C01/output", N=N, s_len=8, s1=a2.s1_sp(N), s2=a2.s2_sp(N))  # Erstellen der Datei für einfache Genauigkeit
    ext.output_file(filename="dp_output", path="C01/output", N=N, s_len=16, s1=a2.s1_dp(N), s2=a2.s2_dp(N))  # Erstellen der Datei für doppelte Genauigkeit
    # Plotten der Daten
    a3.plotting(filename_sp="sp_output.txt", filename_dp="dp_output.txt", path="C01/output")
