#ejercicio listas 
import random

# Creamos un vector de 50 números consecutivos del 1 al 50
# La primera "i" es el valor que se agrega al vector en cada iteración
# La segunda "i" (en el for) representa el valor que toma en cada vuelta del bucle
vector = [i for i in range(1, 51)]  

# 1. Calcular el promedio de los valores del vector
promedio = sum(vector) / len(vector)

# 2. Crear una lista con los números que son mayores que el promedio
mayores = [num for num in vector if num > promedio]

# 3. Imprimir resultados
print("Promedio:", promedio)
print("Cantidad de números mayores al promedio:", len(mayores))
print("Lista de valores mayores:", mayores)


#ejercicio 2 
# Generar dos vectores A y B con 45 números aleatorios entre 1 y 100
A = [random.randint(1, 100) for i in range(45)]  # randint genera un número aleatorio en el rango dado
B = [random.randint(1, 100) for i in range(45)]  # el for se repite 45 veces para llenar el vector

# Crear un vector C que contiene la suma de los elementos correspondientes de A y B
# Aquí "i" es el índice, entonces A[i] es el valor en la posición i de A, y B[i] el valor en la misma posición de B
C = [A[i] + B[i] for i in range(45)]

print("Vector C:", C)


#ejercicio 3 
# Generar un vector D con 20 números aleatorios entre 1 y 100
D = [random.randint(1,100) for i in range(20)]

# Buscar el valor máximo del vector
mayor = max(D)
print("El valor mayor en D es:", mayor)

# Buscar la posición (índice) donde se encuentra ese valor máximo
posicion = D.index(mayor)   # devuelve la primera posición en la que aparece
print("El valor mayor está en la posición:", posicion)


#ejercicio 4
# Generar un vector E con 500 números aleatorios entre 1 y 200
E = [random.randint(1, 200) for i in range(500)]

# Crear un nuevo vector con los cuadrados de los elementos de E
cuadrados = [x**2 for x in E]

print("Vector E:", E)
print("Vector de cuadrados:", cuadrados)


#ejercicio 5
# Generar un vector F con 300 números aleatorios entre -300 y 300 para que hayan ceros y negativos 
F = [random.randint(-300, 300) for i in range(300)]

# Contar cuántos ceros hay en el vector (aunque en este rango nunca habrá ceros)
cantidad_ceros = F.count(0)
print("Cantidad de ceros:", cantidad_ceros)

# Crear listas vacías para guardar positivos y negativos
positivos = []
negativos = []

# Recorrer cada número y clasificarlo en positivo o negativo
for x in F:
    if x > 0:
        positivos.append(x)
    elif x < 0:
        negativos.append(x)

print("Cantidad de positivos:", len(positivos), "/  Cantidad de negativos:", len(negativos))

# Calcular la suma de todos los positivos y negativos
suma_positivos_y_negativos = sum(positivos) + sum(negativos)
print("Suma de positivos y negativos:", suma_positivos_y_negativos)


#ejercicio 6
# Generar un vector G con 150 números aleatorios entre 1 y 400
G = [random.randint(1, 400) for i in range(150)]

# Crear un nuevo vector H que es el inverso de G (con slicing [::-1])
H = G[::-1]  # [::-1] significa que recorre la lista desde el final hasta el principio
print("Vector G:", G)
print("Vector H (invertido):", H)


#ejercicio 7 
# Generar dos vectores de 100 números aleatorios entre 1 y 500
M = [random.randint(1, 500) for i in range(100)]
N = [random.randint(1, 500) for i in range(100)]

# Comparar si los vectores son exactamente iguales
if M == N:
    print("Los vectores M y N son iguales.")
else:
    print("Los vectores M y N son diferentes.")


#ejercicio 8
# Generar un vector de 200 números aleatorios entre 1 y 600
A = [random.randint(1, 600) for i in range(200)]

# Comprobar si está ordenado de menor a mayor comparándolo con la versión ordenada
if A == sorted(A):
    print("El vector A Sí está ordenado de menor a mayor.")
else:
    print("El vector A No está ordenado de menor a mayor.")


#ejercicio 9
# Generar un vector con 80 números aleatorios entre 1 y 700
X = [random.randint(1, 700) for i in range(80)]

# Pedir número al usuario
num = int(input("Ingrese un número: "))

# Buscar en qué posiciones aparece el número ingresado
# enumerate devuelve (índice, valor) en cada iteración
indices = [i for i, valor in enumerate(X) if valor == num]

if indices:
    print(f"El número {num} se encuentra en el vector X.")
    print(f"Índices: {indices}")
else:
    print(f"El número {num} NO está en el vector X.")


#ejercicio 10
# Definir dos vectores A y B
A = [i for i in range (1,21)]
B = [j for j in range (21,41)]

# Crear una lista vacía para guardar resultados
resultados = []

# Multiplicar en orden:
# primer elemento de A con el último de B,
# segundo de A con el penúltimo de B, etc.
# zip(A, reversed(B)) permite recorrer A normal y B en orden inverso a la vez
for a, b in zip(A, reversed(B)): # la funcion zip hace que recorra dos listas a la vez osea las toma como una sola
    resultados.append(a * b)

print("Resultados:", resultados)