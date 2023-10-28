#Aufgabe C02
#teilaufgabe 2
import numpy as np
import matplotlib as plt
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
n = 5   # Anzahl der Subintervalle (rekursive Tiefe)

result = recursive_trapezoidal_integration(lambda x: y_n(x, 2), a, b, n)  # Hier wird n = 2 verwendet
print(f"Das Integral von y_n(x) von {a} bis {b} für n = 2 ist etwa {result}")

#C02 Teilaufgabe 3
def y_n(x, n):
    return (x**(2*n)) / (7 + x**2)

# Erzeugung von x-Werten von 0 bis 1
x = np.linspace(0, 1, 100)

# Erzeugung von n-Werten
n_values = [1, 2, 3, 4, 5]

# Erzeugung einer Grafik für jede n-Wert
for n in n_values:
    y = y_n(x, n)
    plt.plot(x, y, label=f'n={n}')

plt.xlabel('x')
plt.ylabel('y_n(x)')
plt.title('y_n(x) für verschiedene n')
plt.legend()
plt.grid(True)
plt.show()

#funktioniert net ganz