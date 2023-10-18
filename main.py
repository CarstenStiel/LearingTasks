# Imports aus anderen Dateien und packages(numpy)
import numpy as np  # Import von Numpy
from arangeTask import calculate_steps  # Funktion für die arange Aufgabe
import snTask as sn  # Import aller Funktionen für die SN Aufgabe
from tryOut import inputN

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
    # Aufgabe SN
    # SN1
    res1Rec = sn.sn1Recursive(6)  # SN1 rekursiv berechnet
    res1For = sn.sn1For(6)  # SN1 mittels For-Schleife berechnet
    print("SN1-Genauigkeiten mit Rekursion:")  # Ausgabe
    print(f"In einfacher Genauigkeit: {sn.singlePrecision(res1Rec)}")  # SN1 (rekursiv) in einfacher Genauigkeit berechnet (siehe snTask) und ausgegeben
    print(f"In doppelter Genauigkeit: {sn.doublePrecision(res1Rec)}")  # SN1 (rekursiv) in doppelter Genauigkeit berechnet (siehe snTask) und ausgegeben
    print("SN1-Genauigkeiten mit For-Schleife:")
    print(f"In einfacher Genauigkeit: {sn.singlePrecision(res1For)}")  # SN1 (For-Schleife) in einfacher Genauigkeit berechnet (siehe snTask) und ausgegeben
    print(f"In doppelter Genauigkeit: {sn.doublePrecision(res1For)}")  # SN1 (For-Schleife) in doppelter Genauigkeit berechnet (siehe snTask) und ausgegeben
    """
    # SN2
    res2Rec = sn.sn2Recursive(2)  # SN2 rekursiv berechnet
    res2For = sn.sn2For(2)  # SN2 mittels For-Schleife berechnet
    print("SN2-Genauigkeiten:")
    sn.precision(res2Rec)  # SN2 (rekursiv) in einfacher und doppelter Genauigkeit ausgeben (siehe snTask)
    sn.precision(res2For)  # SN2 (For-Schleife) in einfacher und doppelter Genauigkeit ausgeben (siehe snTask)
    """
    """
    # SN1 Input
    res1Rec = sn.sn1Recursive(inputN())  # SN1 rekursiv berechnet
    print("SN1-Genauigkeiten mit Rekursion:")  # Ausgabe
    print(f"In einfacher Genauigkeit: {sn.singlePrecision(res1Rec)}")  # SN1 (rekursiv) in einfacher Genauigkeit berechnet (siehe snTask) und ausgegeben
    print(f"In doppelter Genauigkeit: {sn.doublePrecision(res1Rec)}")  # SN1 (rekursiv) in doppelter Genauigkeit berechnet (siehe snTask) und ausgegeben
    """
