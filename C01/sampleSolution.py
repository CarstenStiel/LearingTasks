"""
QUELLEN
W. Hergert: Aufgabendatenbank und Fortran-Programme
O. Natt, Physik mit Python, 2.Aufl. (2019) + Programme in pyth.de
"""

import math
import numpy as np
import matplotlib.pyplot as plt


def test():
    # Input Anzahl der Summanden from console
    N = input('Anzahl der Summanden N = ? ')
    # print(f'N = {N,type(N)}')
    N = int(N)
    # print(f'N = {N,type(N)}')
    # print('----------------------------------------- end input')

    # use "range" and "for"
    # output to console and file

    # float in Python is double precision
    s_1 = 0.0
    s_2 = 0.0
    vz1 = -1.0  # Vorzeichen1 negativ
    vz = vz1  # Vorzeichen2?
    s1_array = np.array([s_1])
    s2_array = np.array([s_2])
    diff_array = np.array([0])  # Unterschied zwischen s1 und s2

    with open("outputSample.txt", "w") as outputfile:  # Schreibe eine extra Datei für die Ausgabewerte
        # for i in range(1, N, 1):
        for i in range(1, N + 1, 1):
            j = 2 * (i - 1) + 1
            ire = float(j)
            term_1 = vz * ire / (ire + 1.0)
            vz = vz * vz1
            term_1 = term_1 + vz * (ire + 1.0) / (ire + 2.0)
            vz = vz * vz1
            s_1 = s_1 + term_1
            s1_array = np.append(s1_array, [s_1])

            ire = float(i)
            term_2 = 1.0 / (2.0 * ire * (2.0 * ire + 1.0))
            s_2 = s_2 + term_2
            s2_array = np.append(s2_array, [s_2])

            diff = abs(s_1 - s_2)
            diff_array = np.append(diff_array, [diff])

            #        print(f'i = {i} s_1 = {s_1:.16f} s_2 = {s_2:.16f} diff = {diff:.16f}')
            outputfile.write(f'{i} {s_1:.16f} {s_2:.16f} {diff:.16f} \n')

    # print('s1_array ==== \n',s1_array)
    # print('s2_array ==== \n',s2_array)
    # print('diff_array ==== \n',diff_array)

    # np.float32 in NymPy is single precision
    s_1_sp = np.float32(0.0)
    s_2_sp = np.float32(0.0)
    vz1 = -1.0
    vz = vz1
    s1_sp_array = np.array([s_1_sp])
    s2_sp_array = np.array([s_2_sp])
    diff_sp_array = np.array([np.float32(0)])

    with open("output32sample.txt", "w") as outputfile:
        # for i in range(1, N, 1):
        for i in range(1, N + 1, 1):
            j = 2 * (i - 1) + 1
            ire = np.float32(j)
            term_1 = np.float32(vz * ire / (ire + 1.0))
            vz = vz * vz1
            term_1 = term_1 + np.float32(vz * (ire + 1.0) / (ire + 2.0))
            vz = vz * vz1
            s_1_sp = s_1_sp + term_1
            s1_sp_array = np.append(s1_sp_array, [s_1_sp])

            ire = np.float32(i)
            term_2 = np.float32(1.0 / (2.0 * ire * (2.0 * ire + 1.0)))
            s_2_sp = s_2_sp + term_2
            s2_sp_array = np.append(s2_sp_array, [s_2_sp])

            diff_sp = abs(s_1_sp - s_2_sp)
            diff_sp_array = np.append(diff_sp_array, [diff_sp])

            #        print(f'i = {i} s_1_sp = {s_1_sp:.8f} s_2_sp = {s_2_sp:.8f} \
            #              diff_sp = {diff_sp:.8f}')
            outputfile.write(f'{i} {s_1_sp:.8f} {s_2_sp:.8f} {diff_sp:.8f} \n')

    # print('s1_sp_array ==== \n',s1_sp_array)
    # print('s2_sp_array ==== \n',s2_sp_array)
    # print('diff_sp_array ==== \n',diff_sp_array)

    # print('----------------------------------------- end for version1')

    """
    # version 2 =========================================
    s_1 = 0.0
    s1_array = np.array([s_1])
    for i in range(1, 2*N, 2):    
        ire=float(i)
        ire1=float(i+1)
        vz=(-1)**i
        vz1=(-1)**(i+1)
        term_1=vz*ire/(ire+1.0)+vz1*ire1/(ire1+1.0)
        s_1=s_1+term_1
        s1_array = np.append(s1_array,[s_1])
    #    print(f'i = {i} s_1 = {s_1:.16f} ')
    
    print('s1_array ==== \n',s1_array)
    print('s1_array round(3) ==== \n',s1_array.round(3))
    print('----------------------------------------- s_1 end for version2')
    
    s_2 = 0.0
    s2_array = np.array([s_2])
    #for j in range(1, N, 1):
    for j in range(1, N+1, 1):    
        jre=float(j)
        term_2=1.0/(2.0*jre*(2.0*jre+1.0))
        s_2=s_2+term_2
        s2_array = np.append(s2_array,[s_2])
    #    print(f'j = {j} s_2 = {s_2:.16f} ')
    
    print('s2_array ==== \n',s2_array)
    print('s2_array round(3) ==== \n',s2_array.round(3))
    print('----------------------------------------- s_2 end for version2')
    
    diff_array = np.array([0])
    for k in range(1, N+1, 1):
        diff = s1_array[k]-s2_array[k]
        diff_array = np.append(diff_array,[diff])
    #    print(f'k = {k} diff = {diff:.16f} diff32 = {diff32:.16f} \
    #          diff64 = {diff64:.16f} diff128 = {diff128:.16f}')
    
    print('diff_array ==== \n',diff_array)
    # print(diff_array.round(10))
    
    print('----------------------------------------- diff end for version2')
    """

    # plot graphs for s1 and s2
    x_plot = np.arange(0, N + 1, 1)
    # print(x_plot)
    # Erzeuge eine Figure und ein Axes-Objekt.
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('N')
    ax.set_ylabel('s1 and s2')
    # ax.set_yscale('log')
    ax.grid()
    # Plotte die Daten
    # ax.plot(x_plot, s1_array, s2_array, marker = 'o')
    ax.plot(x_plot, s1_array, x_plot, s2_array, marker='o')
    # Erzeuge die Legende und zeige die Grafik an.
    ax.legend(['s1', 's2'])
    plt.show()

    # plot graphs for diff and diff_sp, linear scale
    plt.plot(x_plot, diff_array, x_plot, diff_sp_array, marker='o')
    plt.legend(['diff', 'diff_sp'])
    plt.show()

    # another variant to plot graphs for diff and diff_sp, log scale
    X, Y = [], []
    for line in open('outputSample.txt', 'r'):
        values = [float(s) for s in line.split()]
        X.append(values[0])
        Y.append(values[3])

    X_sp, Y_sp = [], []
    for line in open('output32sample.txt', 'r'):
        values = [np.float32(s) for s in line.split()]
        X_sp.append(values[0])
        Y_sp.append(values[3])

    plt.plot(X, Y, marker='o')
    plt.plot(X_sp, Y_sp, marker='x')
    # plt.plot(x_plot, diff_array, x_plot, diff_sp_array, marker = '+')
    plt.yscale('log')
    plt.show()
