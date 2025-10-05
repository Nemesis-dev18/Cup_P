# #ejercicio 1 
import random
A = [ # Definición de una matriz (lista de listas)
    [1,1,1],
    [1,2,2],
    [1,2,3]
]
for fila in A: # Itera sobre cada fila de la matriz
    for elemento in fila:# Itera sobre cada elemento de la fila
        print(elemento, end=" ")# Imprime el elemento seguido de un espacio
    print()

# ejercicio 2 
print() # línea en blanco para separar los ejercicios
B = [  
    [1,2,3],
    [1,2,3],
    [1,2,3]
]
filas = len(B)
columnas = len(B[0])# número de columnas basado en la primera fila

# --- Sumas de filas ---

for i in range(filas):
    suma_fila = sum(B[i])
    # imprimimos cada fila y al final su suma
    print(" ".join(str(x) for x in B[i]), "=", suma_fila)

# --- Sumas de columnas ---
resultados = []   # lista vacía para guardar las sumas

for j in range(columnas):       # recorre cada columna
    suma_columna = 0 # inicializa la suma de la columna
    for i in range(filas):      # recorre cada fila
        suma_columna += B[i][j]#  suma el elemento de la fila i y columna j
    resultados.append(suma_columna)# guarda la suma en la lista resultados

# --- Fila de resultados ---
print("= " * columnas)          # imprime los "=" como fila 4 
print(" ".join(str(x) for x in resultados))# el join convierte cada elemento en str y los une con espacio

# ejercicio 3
print() # línea en blanco para separar los ejercicios
C = [ # Definición de una matriz (lista de listas)
    [1,1,1],
    [2,2,2],
    [3,3,3]
]
for fila in C: # Itera sobre cada fila de la matriz
    for elemento in fila:# Itera sobre cada elemento de la fila
        print(elemento, end=" ")# Imprime el elemento seguido de un espacio
    print()

# ejercicio 4
print() # línea en blanco para separar los ejercicios
D = [ # Definición de una matriz (lista de listas)
    [4,3,2,1],
    [4,3,2,1],
    [4,3,2,1],
]
for fila in D: # Itera sobre cada fila de la matriz
    for elemento in fila:# Itera sobre cada elemento de la fila
        print(elemento, end=" ")# Imprime el elemento seguido de un espacio
    print()

#ejercicio 5
print() # línea en blanco para separar los ejercicios
E= [
    [random.randint(1, 500) for i in range(3)],
    [random.randint(1, 500) for i in range(3)],
    [random.randint(1, 500) for i in range(3)]
]
for fila in : # Itera sobre cada fila de la matriz
    for elemento in fila:# Itera sobre cada elemento de la fila
        print(elemento, end=" ")# Imprime el elemento seguido de un espacio
    print()