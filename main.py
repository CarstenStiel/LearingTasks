# Imports aus anderen Dateien und packages(numpy)
import numpy as np  # Import von Numpy
from arangeTask import calculate_steps # Funktion für die arangeTask


# Dies ist die "main" Klasse von der aus das Program gestartet wird
if __name__ == '__main__':
    # Aufgabe arange
    # Mit arange
    arr1 = np.arange(2, 10, 0.5)
    print("Mit arange-Funktion:")
    print(arr1)
    print(len(arr1))

    # Ohne Arange, aber mit der geschriebenen Funktion
    arr2 = calculate_steps(2, 10, 0.5)
    print("Ohne arange-Funktion:")
    print(arr2)
    print(len(arr2))