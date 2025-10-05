#bubble sort
def nose(lista):#función que implementa el algoritmo de ordenamiento burbuja (bubble sort) pero la lista que recibe es una lista simple no una matriz
   # z=0
    n = len(lista)#el n es la longitud de la lista
    for i in range(n):
        for j in range(0, n-i-1):#el  rango es desde 0 hasta n-i-1 porque en cada pasada el último elemento ya está en su lugar correcto n es la longitud de la lista y i es el número de pasada actual y -1 es para evitar un índice fuera de rango
            if lista[j] > lista[j+1]:  # intercambia si el elemento encontrado es mayor que el siguiente
                lista[j], lista[j+1] = lista[j+1], lista[j]#intercambio de valores y los guarda en la misma lista
              # #contador de pasos del algoritmo
                #si j es menor que j+1 entonces no hace nada y sigue con el siguiente elemento
              #  print(f"orden {z} = ",lista)#imprime la lista en cada paso del algoritmo
    return lista

nums =[1,5,3,7,2,0]
print("lista original:", nums)
print("orden final= ",nose(nums))#imprime la lista ordenada


# Definimos una lista llamada 'matriz' con algunos valores desordenados
matriz = [5, 3, 1, 2, 6]
lsit = len(matriz)  # Obtenemos la longitud de la lista
l = 0  # Inicializamos el contador de pasos del algoritmo

# Recorremos la lista para aplicar el algoritmo de ordenamiento burbuja
for i in range(lsit):
    # En cada pasada, comparamos elementos adyacentes
    for j in range(0, lsit - i - 1):
        # Si el elemento actual es mayor que el siguiente, los intercambiamos
        if matriz[j] > matriz[j + 1]:
            matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]
            l += 1  # contador de pasos del algoritmo
            print(f"orden {l} = ", matriz)
print("lista ordenada:", matriz)  # Imprimimos la lista ordenada al final
