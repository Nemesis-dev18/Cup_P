#shell sort 
A=[4,7,2,8,1,12,45,33]
def shell (liste):#se define el shell 
    n=len(liste)# se define la longitud de la lista
    intervalo=n//2 # se define el intervalo que es la mitad de la lista para que vaya reduciendo el intervalo en cada pasada
    while intervalo>0:
        for i in range(intervalo,n):
            valor=liste[i]
            j=i
            while j>=intervalo and liste[j-intervalo]>valor:# mientras que j sea igual o mayor que el intervalo y el valor de la lista en la posicion j-intervalo sea mayor que el valor donde j-intervalo es el valor anterior al actual
                liste[j]=liste[j-intervalo]# se mueve el valor mayor a la derecha
                j-=intervalo# el j va disminuyendo en el intervalo
            liste[j]=valor
        intervalo//=2# se vuelve a dividir porque el intervalo se va reduciendo a la mitad en cada pasada
    return liste
print(shell(A))
#teoricamente paso por paso se haria en la linea 2 se define la lista
# en la linea 1 solo es el titulo del ejercicio 
# en la linea 2 se define la lista a operar 
# en la linea 3 se define la funcion shell que toma una lista como argumento
# en la linea 4 se define n como la longitud de la lista
# en la linea 5 se define el intervalo como la mitad de n usando la division entera //
# en la linea 6 se inicia un bucle while que continua mientras el intervalo sea mayor
# en la linea 7 se inicia un bucle for que itera desde el valor del intervalo hasta n
# en la linea 8 se guarda el valor actual de la lista en la variable valor
# en la linea 9 se inicializa j con el valor de i que es el indice actual
# en la linea 10 se inicia otro bucle while que continua mientras j sea mayor o igual al intervalo y el valor en la posicion j-intervalo sea mayor que valor
# en la linea 11 se mueve el valor mayor a la derecha en la posicion j
# en la linea 12 se decrementa j en el valor del intervalo para seguir comparando hacia la izquierda
# en la linea 13 se coloca el valor en la posicion correcta
# en la linea 14 se reduce el intervalo a la mitad usando la division entera // para la siguiente pasada
# en la linea 15 se retorna la lista ordenada
# en la linea 16 se imprime el resultado de llamar a la funcion shell con la lista