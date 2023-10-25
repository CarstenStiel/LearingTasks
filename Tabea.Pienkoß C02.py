#Aufgabe C02
#teilaufgabe 2
import math
def y_n (x, n): #Funktion y_n definieren
    return (x**(2*n))/(7+x**2) #unsere Funktion einsetzen

def recursive_trapezoidal_integration (func, a, b, n):
    if n == 0:
        return 0.5 * (func(a) + func(b)) * (b - a)
    else:
         h = (b - a) / (2 ** n)
         x = a
         sum_result = 0.0
         for i in range(2 ** n):
            sum_result += func(x)
            x += h
         return 0.5 * recursive_trapezoidal_integration(func, a, a + h, n - 1) + 0.5 * recursive_trapezoidal_integration(func, a + h, b, n - 1) + h * sum_result


a = 0.0  # Untere Grenze des Integrals
b = 1.0  # Obere Grenze des Integrals
n = input()  # Anzahl der Subintervalle (rekursive Tiefe)

result = recursive_trapezoidal_integration(lambda x: y_n(x, n), a, b, n)  # Hier wird n = 2 verwendet
print(f"Das Integral von y_n(x) von {a} bis {b} für n = 2 ist etwa {result}")
