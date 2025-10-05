#metodo de mezcla
A=[4,7,2,8,1,12,45,33]
def mez (list):
    if len(list) <=1:
        return list
    mitad=len(list)//2 # el 2 es para dividir en dos partes
    izq=mez(list[:mitad]) #parte izquierda : -> es el elemento a comparar com el mitad que es la parte entera de la lista
    der=mez(list[mitad:]) #parte derecha
    return mezclar(izq,der)
def mezclar(izq,der):
    resultado=[]
    i=j=0 # define como i y j como 0 para tomar el indice 0 de las dos partes y asi ya comparado aumentara el iterador
    while i<len(izq) and j<len(der):#mientras que i y j sean menores que la longitud de izq y der
        if izq[i]<der[j]:# si el elemento de la parte izquierda es menor que el de la parte derecha
            resultado.append(izq[i])# se agregara al resultado de la lista resultado donde izq  sale como un nombre de control y el i es para que vaya avanzando en la parte izquierda
            i+=1
        else:   # el j es para que vaya avanzando en la parte derecha 
            resultado.append(der[j])
            j+=1
    resultado.extend(izq[i:])# el extend es para agregar los elementos que faltan i el i: es para que vaya avanzando en la parte izquierda de iterador porque ya se comparo con la parte derecha
    resultado.extend(der[j:])
    return resultado
print(mez(A))
# el list inicial es para que tome la lista completa y la divida en dos partes
# el // es para que tome la parte entera de la division
#el :mitad es para comparar el primer elemento de la lista con el elemento de la variable mitad
# el mitad: es para que tome desde la mitad hasta el final de la lista ya dividida
# el i y j son para que vayan avanzando en las dos partes de la lista
# el and es para que se cumplan las dos condiciones al mismo tiempo
# el append es para agregar los elementos a la lista resultado
# el while se usa ya que con un for no se puede controlar el avance de los iteradores i y j
# hay dos funciones de recursividad una es la de mez y la otra es la de mezclar 
#una siendo para ir dividiendo la lista en 2 y la otra p[ara definir el orden de los elementos ya divididos 
