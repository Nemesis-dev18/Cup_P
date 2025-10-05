
def quick_sort(lista,iteracion=1):
    if len(lista) <= 1:
        return lista#si la longitud de la lista es menor o igual a 1 entonces ya está ordenada y la devuelve tal cual
    pivote = lista[-1]# toma el pivote de el ultimo indice 
    menores = [x for x in lista[:-1] if x < pivote]#el : es para que tome todos los elementos menos el ultimo que es el pivote y crea una sublista con los elementos menores que el pivote
    mayores = [x for x in lista[:-1] if x > pivote]# la primera x es el elemento que se está evaluando en la lista y la segunda x es el valor que se agrega a la nueva lista si cumple la condición de ser mayor que el pivote
    print(f"Iteración {iteracion}: {menores}  {pivote}  {mayores}")
    return quick_sort(menores,iteracion + 1) + [pivote] + quick_sort(mayores)#llama recursivamente a quick_sort para ordenar las sublistas de menores y mayores, y luego concatena los resultados con el pivote en el medio

A = [8,1,5,14,4,15,12,6,2,11,10,7,9]
A_ordenada = quick_sort(A)
print("lista ordenada:", A_ordenada)


