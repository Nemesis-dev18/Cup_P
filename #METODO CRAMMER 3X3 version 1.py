#METODO CRAMMER 3X3 version 1.0 ( teoricamente son 3x4 pero meh )

import sys
import copy 
listax = []
lista_original=[copy.deepcopy(listax)]
D=0
X=0
Y=0
Z=0
n=len(listax)
print("Ingrese los valores de la matriz A (3x3) donde el 4to valor es la igualdad , separados por espacios:")
listax = list(map(int, input().strip().split()))
lista_original=copy.deepcopy(listax)
if len(listax) != 12:
    print("Debes ingresar exactamente 12  valores. ( 3 de las variables y 1 de la igualdad )")
else:
    for fila in lista_original:
        fila.insert(3, "=")
    print("Matriz 3x3:")
    for fila in lista_original:
        print(" ".join(map(str, fila)))

        