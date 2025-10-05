#ejercicio 1 
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

#--- Fila de resultados ---
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
E = [
    [random.randint(1, 10) for i in range(3)]
    for j in range(3)
]
print() # línea en blanco para separar los ejercicios

for fila in E:
    print(*fila,)# Imprime el elemento seguido de un espacio
# Paso 1: aplanar la matriz en una sola lista
lista = [elemento for fila in E for elemento in fila] # comprensión de listas para aplanar la matriz y asi poder ordenarla porque  las listas anidadas no se pueden ordenar directamente

# Paso 2: ordenar la lista completa
lista.sort()

# Paso 3: reconstruir la matriz ordenada 3x3
E_ordenada = [lista[i:i+3] for i in range(0, len(lista), 3)] # el i:i+3 toma segmentos de 3 elementos para formar las filas de la nueva matriz y el range avanza de 3 en 3 con el lent de la lista 


print("\nMatriz completamente ordenada:")
for fila in E_ordenada:
    print(*fila)
# for fila in : # Itera sobre cada fila de la matriz

print()

#ejercicio 6
D=[
    ["Juan","Perez","Callao"],
    ["Luis","Castro","Lima"],
    ["Maria","Osores","Olivos"]

]
for fila in D:
    print(*fila,)

print()
#ejercicio 7
E=[
    [1,2,3,4,5,6],
    [2,4,6,8,10,12],
    [1,3,5,7,9,11]
]
for fila in E:
    print(*fila,)
print()


#ejercicio 8
F = [  
    [4,7,2],
    [7,8,9],
    [3,9,3]
]
suma_diagonal_principal = sum(F[i][i] for i in range(len(F)))# suma de la diagonal principal con el F[i][i] que recorre los elementos donde fila y columna son iguales
suma_diagonal_secundaria = sum(F[i][len(F)-1-i] for i in range(len(F)))# lo mismo pero para la diagonal secundaria donde la columna es len(F)-1-i hace que recorra desde el final al principio
for i in range(len(F)):#este for es para recorrer las filas 
    for elemento in F[i]:#este for es para recorrer los elementos de cada fila
        print(elemento, end=" ")
    # agregar las sumas en la primera y última fila
    if i == 0:  
        print("= ", suma_diagonal_secundaria, end="")
    if i == len(F)-1: # última fila este if es para que no imprima en la fila del medio
        print("= ", suma_diagonal_principal, end="")#el print de la suma de la diagonal principal
    print()  # salto de línea
#ejercicio 9
print() # línea en blanco para separar los ejercicios
n= int(input("ingrese un numero cualquiera: "))

G =[
    [f"{n}+1", f"{n}+2", f"{n}+3"],
    [f"{n}+4", f"{n}+5", f"{n}+6"],
    [f"{n}+7", f"{n}+8", f"{n}+9"],
]

for fila in G:
    print(*fila,)
print()
#ejercicio 10


#Definimos la matriz de 4x4 con valores fijos
H=[
    [5,9,9,1],
    [4,2,7,4],
    [1,1,2,2],
    [4,6,8,2]
]

# Obtenemos el número de filas y columnas de la matriz
filas = len(H)         # len(H) devuelve cuántas listas internas hay → número de filas
columnas = len(H[0])   # len(H[0]) devuelve cuántos elementos tiene la primera fila → número de columnas

# --- OPERACIONES EN FILAS ---
# Recorremos cada fila con su índice i
for i in range(filas):#este for es para recorrer las filas 
    if i % 2 == 0:  # Si el índice de la fila es PAR (0,2,...) = PRODUCTO
        producto = 1              # inicializamos el producto en 1 (neutro multiplicativo)
        for x in H[i]:            # recorremos cada elemento de la fila i
            producto *= x         # multiplicamos todos los elementos de la fila i y el *= es equivalente a producto = producto * x
        # Mostramos la fila y su producto
        print(" ".join(str(x) for x in H[i]), "=", producto)
    else:  # Si el índice de la fila es IMPAR (1,3,...) = SUMA
        suma = sum(H[i])          # sumamos todos los elementos de la fila i
        # Mostramos la fila y su suma
        print(" ".join(str(x) for x in H[i]), "=", suma)# el join convierte cada elemento en str y los une con espacio

# Esto solo imprime una fila con tantos "=" como columnas haya en la matriz
print("= " * columnas)

# --- OPERACIONES EN COLUMNAS ---
resultados = []  # aquí guardaremos los resultados de cada columna

# Recorremos cada columna con su índice j
for j in range(columnas):
    if j % 2 == 0:  # Si la columna es PAR (0,2,...) → SUMA
        suma_col = sum(H[i][j] for i in range(filas))  # sumamos todos los elementos de la columna
        resultados.append(suma_col)                    # lo guardamos en la lista
    else:  # Si la columna es IMPAR (1,3,...) → PRODUCTO
        prod_col = 1                                   # inicializamos el producto en 1
        for i in range(filas):                         # recorremos todas las filas en la columna j
            prod_col *= H[i][j]                        # multiplicamos cada elemento de esa columna
        resultados.append(prod_col)                    # lo guardamos en la lista

# Mostramos los resultados de columnas como una "última fila"
print(" ".join(str(x) for x in resultados))
print()

#ejercicio 11
K=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#crear la matriz con el orden inverso pero sin mover el orden de las filas  osea que la primera fila siga siendo la primera pero invertida y asi
L = [fila[::-1] for fila in K] # el [::-1] invierte cada fila individualmente
print("Matriz K:")
for fila in K:
    print(*fila,)
print("\nMatriz L (K invertida):")
for fila in L:
    print(*fila,)
print()
#ejercicio 12
X=[
    [random.randint(1, 10) for i in range(3)]
    for j in range(3)
]
Z=[
    [random.randint(1, 10) for i in range(3)]
    for j in range(3)
]
filasX = len(X)
columnasX = len(X[0])# número de columnas basado en la primera fila

#--- Sumas de columnas ---
resultadosX= []   # lista vacía para guardar las sumas

for j in range(columnasX):       # recorre cada columna
    suma_columna = 0 # inicializa la suma de la columna
    for i in range(filasX):      # recorre cada fila
        suma_columna += X[i][j]#  suma el elemento de la fila i y columna j
    resultadosX.append(suma_columna)# guarda la suma en la lista resultados

filasZ = len(Z)
columnasZ = len(Z[0])# número de columnas basado en la primera fila

#--- Sumas de columnas ---
resultadosZ= []   # lista vacía para guardar las sumas

for j in range(columnasZ):       # recorre cada columna
    suma_columna = 0 # inicializa la suma de la columna
    for i in range(filasZ):      # recorre cada fila
        suma_columna += Z[i][j]#  suma el elemento de la fila i y columna j
    resultadosZ.append(suma_columna)# guarda la suma en la lista resultados
#Creamos la matriz ZX con las sumas de columnas de X y Z
ZX = [ #esta lista es para crear la matriz ZX que contiene las sumas de las columnas de X y Z
    resultadosX,# suma de columnas de X
    resultadosZ# suma de columnas de Z
]

#Calculamos la suma de las filas anteriores (suma total de columnas)
sumaZX = [resultadosX[i] + resultadosZ[i] for i in range(len(resultadosX))]

#Agregamos esa nueva fila a la matriz ZX
ZX.append(sumaZX)

print("Matriz X:")# imprime la matriz X
for fila in X:# imprime cada fila de la matriz X
    print(*fila,)
print("suma de columnas:", resultadosX)# imprime la suma de las columnas de la matriz X
print()
print("\nMatriz Z:")
for fila in Z:
    print(*fila,)
print("suma de columnas:", resultadosZ)# imprime la suma de las columnas de la matriz Z
print()#es un salto de linea para que se vea mejor 
print("\nMatriz ZX (suma de columnas de X y Z):")
for fila in ZX:
    print(*fila,)
print()
