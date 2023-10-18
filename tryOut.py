import snTask as sn


# Diese function erweitert die SN Aufgabe, indem hier nach einem Input gefragt wird für N
def inputN():
    # Solange der Input nicht korrekt ist, wird die Schleife immer wieder durchlaufen
    while True:
        userInput = input("Geben Sie eine ganze Zahl größer als 1 ein: ")  # Input vom Nutzer
        # Überprüfen, ob die Eingabe eine Zahl ist
        if userInput.isdigit():
            N = int(userInput)  # Wenn es eine Zahl war, dann wandele in einen Integer wert um
            # Wenn N größer gleich 1, dann gib n zurück
            if N >= 1:
                print(f"Die Eingabe war N = {N}")
                return N  # Rückgabe von N, wenn eine gültige Eingabe gemacht wurde
        # Wenn es keine positive Ganzzahl war, dann gib Fehler aus und starte die Schleife von neuem
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl größer als 1 ein.")
