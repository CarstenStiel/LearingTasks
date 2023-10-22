import numpy as np  # Import von Numpy
import matplotlib.pyplot as plt


# Derzeit in Bearbeitung und dient nur als Test!
# Funktion, die aus zwei Dateien (mit extension.py erstellt) ausliest und plottet
def plotting(filename_sp, filename_dp, path):  # Übergabe von Dateinamen für einfache und doppelte Genauigkeit und den Dateipfad
    filepath_sp = path + "/" + filename_sp  # Erstellung des Dateipfades für einfache Genauigkeit
    filepath_dp = path + "/" + filename_dp  # Erstellung des Dateipfades für doppelte Genauigkeit
    N = []  # Initialisiere ein leeres Array für alle N einträge
    cal_sp, cal_dp = [], []  # Initialisiere zwei leere Arrays für die Berechnung der einfachen und doppelten Genauigkeit (|(s1-s2)/s2|)

    # Als Datei für einfache Genauigkeit lesen und array mit Berechnung erstellen
    try:
        with open(filepath_sp, 'r') as file:  # Öffne Datei zum Lesen ("r")
            lines = file.readlines()  # Alle Zeilen speichern
            # Wir beginnen bei Zeile 2 und iterieren über die restlichen Zeilen
            for line in lines[1:]:
                values = [np.float32(s) for s in line.split()]  # Speichere alle Werte als einfache Genauigkeit einer Zeile in einem Array [N, s1, s2, diff]
                diff = values[-1]  # Speichere die Differenz
                s2 = values[-2]  # Speichere s2
                term = np.float32(abs(diff / s2))  # Führe berechnung aus (|(s1-s2)/s2|)
                N = np.append(N, values[0])  # Füge den N wert dem N-Array hinzu
                cal_sp = np.append(cal_sp, term)  # Füge die Berechnung dem Berchnungs-Array hinzu

    # Wenn die Datei nicht gefunden wurde, dann werfe einen Fehler
    except FileNotFoundError:
        print(f'Die Datei {filename_dp} wurde nicht gefunden unter folgendem Verzeichnis: {filepath_dp}.')
    # Wenn ein anderer Fehler aufkommt, dann werfe einen Fehler
    except Exception as e:
        print(f'Ein Fehler ist aufgetreten: {str(e)}')

    # Als Datei für doppelte Genauigkeit lesen und array mit Berechnung erstellen
    try:
        N = []  # Setzte N zurück, damit sich die Einträge nicht doppeln
        with open(filepath_dp, 'r') as file:  # Öffne Datei zum Lesen ("r")
            lines = file.readlines()  # Alle Zeilen speichern
            # Wir beginnen bei Zeile 2 und iterieren über die restlichen Zeilen
            for line in lines[1:]:
                values = [float(s) for s in line.split()]  # Speichere alle Werte als einfache Genauigkeit einer Zeile in einem Array [N, s1, s2, diff]
                diff = values[-1]  # Speichere die Differenz
                s2 = values[-2]  # Speichere s2
                term = abs(diff / s2)  # Führe berechnung aus (|(s1-s2)/s2|)
                N = np.append(N, values[0])  # Füge den N wert dem N-Array hinzu
                cal_dp = np.append(cal_dp, term)  # Füge die Berechnung dem Berchnungs-Array hinzu

    # Wenn die Datei nicht gefunden wurde, dann werfe einen Fehler
    except FileNotFoundError:
        print(f'Die Datei {filename_dp} wurde nicht gefunden unter folgendem Verzeichnis: {filepath_dp}.')
    # Wenn ein anderer Fehler aufkommt, dann werfe einen Fehler
    except Exception as e:
        print(f'Ein Fehler ist aufgetreten: {str(e)}')

    plt.figure(figsize=(10, 6))  # Erstellt und ändert die Größe der Abbildung auf 10 Zoll Breite und 6 Zoll Höhe
    # plt.loglog(N, cal_sp, label="single-Precision", marker='o')   # Zusätzlicher Plot für die einfache Genauigkeit
    plt.loglog(N, cal_dp, label="double-Precision", marker='o')  # Plot für die doppelte Genauigkeit
    plt.ylabel("log10|(s1 - s2) / s2|")  # y-Achse "beschriften"/laben
    plt.xlabel("log10(N)")  # x-Achse "beschriften"/laben
    plt.title("Aufgabe 3")  # Abbildung benennen
    plt.grid()  # Ein Raster bei der Abbildung hinzufügen
    plt.legend()  # Eine Legende bei der Abbildung hinzufügen
    plt.show()  # Abbildung anzeigen
    print("Plotting beendet!")  # Ausgabe, dass der Prozess abgeschlossen ist
