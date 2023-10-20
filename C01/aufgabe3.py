import numpy as np  # Import von Numpy
import matplotlib.pyplot as plt


# Derzeit in Bearbeitung und dient nur als Test!
# Nicht verwenden
def plotting(s1, s2, N):
    """
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
    """
    N = np.arange(0, N + 1, 1)
    S_log_array = np.array([])
    N_log_array = np.array([])
    for i in range(1, len(N)):
        N_log = np.log10(N[i])
        N_log_array = np.append(N_log_array, N_log)
        term = abs((s1[i] - s2[i]) / s2[i])
        if term != 0:
            S_log = np.log10(term)
            print(S_log)
            # print(f"{i}: {S_log}")
            S_log_array = np.append(S_log_array, S_log)
        else:
            # print(f"{i}: {np.nan}")
            S_log_array = np.append(S_log_array, np.nan)

    plt.figure()  # Erstellt eine Abbildung
    plt.loglog(N_log_array, S_log_array, label='log10(|(a - b) / b|)', color='blue')
    plt.xlabel('N')
    plt.legend()
    plt.grid()
    plt.show()
