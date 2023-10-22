import numpy as np  # Import von Numpy
import matplotlib.pyplot as plt


# Derzeit in Bearbeitung und dient nur als Test!
def plotting(filename_sp, filename_dp, path):
    filepath_sp = path + "/" + filename_sp
    filepath_dp = path + "/" + filename_dp
    N = []
    cal_sp, cal_dp = [], []

    try:
        with open(filepath_sp, 'r') as file:
            lines = file.readlines()
            # Wir beginnen bei Zeile 2 und iterieren über die restlichen Zeilen
            for line in lines[1:]:
                values = [np.float32(s) for s in line.split()]
                diff = values[-1]
                s2 = values[-2]
                term = np.float32(abs(diff / s2))
                N = np.append(N, values[0])
                cal_sp = np.append(cal_sp, term)

    except FileNotFoundError:
        print(f'Die Datei {filename_dp} wurde nicht gefunden unter folgendem Verzeichnis: {filepath_dp}.')
    except Exception as e:
        print(f'Ein Fehler ist aufgetreten: {str(e)}')

    try:
        N = []
        with open(filepath_dp, 'r') as file:
            lines = file.readlines()
            # Wir beginnen bei Zeile 2 und iterieren über die restlichen Zeilen
            for line in lines[1:]:
                values = [float(s) for s in line.split()]
                diff = values[-1]
                s2 = values[-2]
                term = abs(diff / s2)
                N = np.append(N, values[0])
                cal_dp = np.append(cal_dp, term)

    except FileNotFoundError:
        print(f'Die Datei {filename_dp} wurde nicht gefunden unter folgendem Verzeichnis: {filepath_dp}.')
    except Exception as e:
        print(f'Ein Fehler ist aufgetreten: {str(e)}')

    plt.figure(figsize=(10, 6))  # Ändert die Größe der Abbildung auf 10 Zoll Breite und 6 Zoll Höhe
    # Erstellt eine Abbildung
    # plt.loglog(N, cal_sp, label="single-Precision", marker='o')
    plt.loglog(N, cal_dp, label="double-Precision", marker='o')
    plt.ylabel("log10|(s1 - s2) / s2|")
    plt.xlabel("log10(N)")
    plt.title("Aufgabe 3")
    plt.grid()
    plt.legend()
    plt.show()
    print("Plotting beendet!")
