import numpy as np
import matplotlib.pyplot as plt
n = int(input("Ingrese el número de ecuaciones: "))

A = []
b = []

for i in range(n):
    fila = input(f"Ingrese los coeficientes de la ecuación {i+1} separados por espacio: ")
    A.append([float(x) for x in fila.split()])
    val = float(input(f"Ingrese el valor de igualdad de la ecuación {i+1}: "))
    b.append(val)

A = np.array(A)
b = np.array(b)

x = np.linalg.solve(A, b)

print("Solución del sistema:", x)


x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()
