import numpy as np  # Import von Numpy
import matplotlib.pyplot as plt


# Aufgabe 2.
# Diese Funktion erweitert die SN Aufgabe, indem hier nach einem Input gefragt wird für N
def input_n():
    # Solange der Input nicht korrekt ist, wird die Schleife immer wieder durchlaufen
    while True:
        userInput = input("Geben Sie N ein (>=1): ")  # Input vom Nutzer
        # Überprüfen, ob die Eingabe eine Zahl ist
        if userInput.isdigit() and int(userInput) >= 1:
            N = int(userInput)  # Wenn es eine Zahl war und diese >=1, dann wandele in einen Integer wert um
            print(f"Die Eingabe war N = {N}")
            return N  # Rückgabe von N, wenn eine gültige Eingabe gemacht wurde
        # Wenn es keine positive Ganzzahl war, dann gib Fehler aus und starte die Schleife von neuem
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl größer als 1 ein.")


# Diese Funktion berechnet S1 mit einer For-Schleife und gibt dies zurück
def s1_dp(N):  # Nur N als Parameter eingeben
    s1 = np.array([0.0])  # Initialisiere das Ergebnis(result) mit dem Wert 0
    for i in range(1, N + 1):  # Für jedes n von 1 bis 2N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
        n = float(2 * (i - 1) + 1)
        cal1 = float(pow(-1.0, n)) * n / (n + 1.0)  # Addiere die Berechnung auf das Ergebnis
        cal2 = cal1 + float(pow(-1.0, n + 1)) * (n + 1.0) / (n + 2.0)
        res = s1[-1] + cal2
        s1 = np.append(s1, [res])
    return s1  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnis zurück


def s2_dp(N):  # Nur N als Parameter eingeben
    s2 = np.array([0.0])  # Initialisiere das Ergebnis(result) mit dem Wert 0
    for i in range(1, N + 1):  # Für jedes n von 1 bis 2N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
        n = float(i)
        res = s2[-1] + 1.0 / (2.0 * n * (2.0 * n + 1.0))  # Addiere die Berechnung auf das Ergebnis
        s2 = np.append(s2, res)
    return s2  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnis zurück


def s1_sp(N):  # Nur N als Parameter eingeben
    s1 = np.array([np.float32(0.0)])  # Initialisiere das Ergebnis(result) mit dem Wert 0
    for n in range(1, N + 1):  # Für jedes n von 1 bis 2N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
        j = np.float32(2 * (n - 1) + 1)
        cal1 = s1[-1] + np.float32(np.float32(pow(-1, j)) * j / (j + 1.0))  # Addiere die Berechnung auf das Ergebnis
        res = cal1 + np.float32(np.float32(pow(-1, j + 1)) * (j + 1.0) / (j + 2.0))
        s1 = np.append(s1, res)
    return s1  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnis zurück


def s2_sp(N):  # Nur N als Parameter eingeben
    s2 = np.array([np.float32(0.0)])  # Initialisiere das Ergebnis(result) mit dem Wert 0
    for n in range(1, N + 1):  # Für jedes n von 1 bis 2N + 1 führe die Berechnung aus (+1, da das Ende von range exklusiv ist)
        j = np.float32(n)
        cal = s2[-1] + np.float32(1.0 / (2.0 * j * ((2.0 * j) + 1.0)))  # Addiere die Berechnung auf das Ergebnis
        s2 = np.append(s2, [cal])
    return s2  # Wenn die For-Schleife durchlaufen wurde, dann gib das Ergebnis zurück


def output_file():
    sp_filename = "sp_output"
    dp_filename = "dp_output"
    N = input_n()
    N_len = len(str(N))
    s1_sp_arr = s1_sp(N)
    s2_sp_arr = s2_sp(N)
    diff_sp_array = np.array([np.float32(0)])
    s1_dp_arr = s1_dp(N)
    s2_dp_arr = s2_dp(N)
    diff_dp_array = np.array([np.float32(0)])
    with open(f"output/{sp_filename}.txt", "w") as outputfile:
        outputfile.write('{:{N_len}s} {:10s} {:10s} {:10s} \n'.format("N", "s1", "s2", "diff", N_len=N_len))
        for n in range(1, N + 1):
            diff_sp = abs(s1_sp_arr[n] - s2_sp_arr[n])
            diff_sp_array = np.append(diff_sp_array, diff_sp)
            outputfile.write(f'{str(n):{N_len}s} {s1_sp_arr[n]:.8f} {s2_sp_arr[n]:.8f} {diff_sp:.8f} \n')
    print(f'Datei "{sp_filename}" für single-precision mit N = {N}, wurde unter dem Verzeichnis "output" erstellt/bearbeitet!')
    with open(f"output/{dp_filename}.txt", "w") as outputfile:
        outputfile.write('{:{N_len}s} {:18s} {:18s} {:18s} \n'.format("N", "s1", "s2", "diff", N_len=N_len))
        for n in range(1, N + 1):
            diff_dp = abs(s1_dp_arr[n] - s2_dp_arr[n])
            diff_dp_array = np.append(diff_dp_array, diff_dp)
            outputfile.write(f'{str(n):{N_len}s} {s1_dp_arr[n]:.16f} {s2_dp_arr[n]:.16f} {diff_dp:.16f} \n')
    print(f'Datei "{dp_filename}" für double-precision mit N = {N}, wurde unter dem Verzeichnis "output" erstellt/bearbeitet!')


def plotting(s1, s2, N):
    print(s2)
    fig = plt.figure()  # Erstellt eine Abbildung
    ax = fig.add_subplot(1, 1, 1)  # Erstellt die Achsen zur Abbildung
    ax.set_xlabel('N')  # X-Achse als "N"
    ax.set_ylabel('s1 and s2')  # Y-Achse als "s1 and s2"
    ax.grid()  # Fügt ein Raster ein
    x_plot = np.arange(0, N + 1, 1)
    ax.plot(x_plot, s1, x_plot, s2)
    ax.legend(['s1', 's2'])
    plt.show()
