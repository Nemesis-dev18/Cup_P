#ejercicios de def
import random

# def listado(lista):
#     for i in lista:
#             if i==lista[2]:
#                 print("el elemento de la lista en la posicion 3 es:",i)
#                 print("la lista original es :",lista)
# A=[random.randint(1,100) for i in range(10)]   
# listado(A)

# # ejercicio 2
# def lista_extremos():
#     B=[random.randint(1,100) for i in range(10)]
#     print("la lista original es :",B)
#     return (B[0],B[-1])
# print(lista_extremos())
# print()

# # ejercicio 3
# def contador_que_devuelve_T(lista,valor):
#     contador=0
#     for i in lista:
#         if i==valor:
#             contador+=1
#     if contador>1:
#         return "T"


# #ejercicio 4
# def agregar_si_no_existe(lista,valor):
#     if valor not in lista:
#         lista.append(valor)
#     return lista
# D=[random.randint(1,10) for i in range(10)]
# print("la lista original es :",D)
# intento=int(input("ingrese un numero del 1 al 10:"))
# print("la nueva lista es :",agregar_si_no_existe(D,intento))
# print()

# #ejercicio 5
def tempeuratura(lista):
        for i in lista:
            if i<0 :
                return "HELADO"
            if i>=0 and i<10:
                return "FRIO"
            if i>=10 and i<20:
                return "CALIDO"
            if i>=20 and i<30:
                return "SOFOCANTE"
            if i>=30:
                return "ABRASIVO"
E=[1,2,3,4,5,-6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print(tempeuratura(E))