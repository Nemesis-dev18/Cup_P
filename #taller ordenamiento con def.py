#taller ordenamiento con def 
import random as r
A=[]
for i in range(3):
    n=str(input(f"ingrese el nombre numero {i+1}: "))
    A.append(n)
def nose(lista):#función que implementa el algoritmo de ordenamiento burbuja (bubble sort) pero la lista que recibe es una lista simple no una matriz
    n = len(A)#el n es la longitud de la lista
    for i in range(n):
        for j in range(0, n-i-1):#el  rango es desde 0 hasta n-i-1 porque en cada pasada el último elemento ya está en su lugar correcto n es la longitud de la lista y i es el número de pasada actual y -1 es para evitar un índice fuera de rango
            if lista[j] > lista[j+1]:  # intercambia si el elemento encontrado es mayor que el siguiente
                lista[j], lista[j+1] = lista[j+1], lista[j]#intercambio de valores y los guarda en la misma lista     #si j es menor que j+1 entonces no hace nada y sigue con el siguiente elemento
    return lista#imprime la lista en cada paso del algoritmo
nose(A)
print("lista ordenada:", A)  # Imprimimos la lista ordenada al final


#ejercicio 2 
Apelliddos=[]
#definimos las 3 notas de cada estudiante por apellido 
Notas=[]
for i in range(3):
    apellido=str(input(f"ingrese el apellido del estudiante numero {i+1}: "))
    Apelliddos.append(apellido.lower())
    for j in range(3):
        Nota=float(input(f"ingrese la nota {j+1} del estudiante {apellido}: "))
        Notas.append(Nota)
def ordenar_listas(apellidos, notas):
    n = len(apellidos)#el len es la longitud de la lista
    for i in range(n):
        for j in range(0, n-i-1):#el  rango es desde 0 hasta n-i-1 porque en cada pasada el último elemento ya está en su lugar correcto n es la longitud de la lista y i es el número de pasada actual y -1 es para evitar un índice fuera de rango
            if apellidos[j] > apellidos[j+1]:
                apellidos[j], apellidos[j+1] = apellidos[j+1], apellidos[j]
                # Intercambiar las notas correspondientes
                notas[j*3:(j+1)*3], notas[(j+1)*3:(j+2)*3] = notas[(j+1)*3:(j+2)*3], notas[j*3:(j+1)*3]#intercambio de valores y los guarda en la misma lista donde el j*3 es el inicio de las notas del estudiante j y (j+1)*3 es el final de las notas del estudiante j y (j+1)*3 es el inicio de las notas del estudiante j+1 y (j+2)*3 es el final de las notas del estudiante j+1
    return apellidos, notas        
def promedio(notas):
    promedios = []
    for i in range(0, len(notas), 3):
        promedio_estudiante = sum(notas[i:i+3]) / 3#el i:i+3 es para tomar las notas de cada estudiante donde el i es el inicio de las notas del estudiante y i+3 es el final de las notas del estudiante
        promedios.append(promedio_estudiante)
    return promedios
# print("lista de apellidos y notas antes de ordenar:")
# for i in range(3):
#     print(f"Estudiante: {Apelliddos[i]}, Notas: {Notas[i*3:(i+1)*3]}")
ordenar_listas(Apelliddos, Notas)
print("lista de apellidos y notas después de ordenar:")
for i in range(3):
    print(f"Estudiante: {Apelliddos[i]}, Notas: {Notas[i*3:(i+1)*3]} / Promedio: {promedio(Notas)[i]}")

#ejercicio 3 
D=[]
M=[]
Y=[]
for i in range(3):
    d=int(input(f"ingrese el dia {i+1}: "))
    D.append(d)
    m=int(input(f"ingrese el mes {i+1}: "))
    M.append(m)
    y=int(input(f"ingrese el año {i+1}: "))
    Y.append(y)
def validar_fecha(dia, mes, año):
    if año < 0:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if mes == 2 and dia > 29:
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    return True
for i in range(3):
    while not validar_fecha(D[i], M[i], Y[i]):
        print(f"Fecha {D[i]}/{M[i]}/{Y[i]} no es válida. Por favor, ingrese una fecha válida.")
        D[i] = int(input(f"ingrese el dia {i+1}: "))
        M[i] = int(input(f"ingrese el mes {i+1}: "))
        Y[i] = int(input(f"ingrese el año {i+1}: "))
def ordenar_fechas(dias, meses, años):
    n = len(dias)
    for i in range(n):
        for j in range(0, n-i-1):#el rango es desde 0 hasta n-i-1 porque en cada pasada el último elemento ya está en su lugar correcto n es la longitud de la lista y i es el número de pasada actual y -1 es para evitar un índice fuera de rango
            if (años[j], meses[j], dias[j]) > (años[j+1], meses[j+1], dias[j+1]):
                años[j], años[j+1] = años[j+1], años[j]
                meses[j], meses[j+1] = meses[j+1], meses[j]
                dias[j], dias[j+1] = dias[j+1], dias[j]
    return dias, meses, años
ordenar_fechas(D, M, Y)
print("Fechas ordenadas:")
for i in range(3):
    print(f"{D[i]:02d}/{M[i]:02d}/{Y[i]}")
#el :02d es para que el dia y el mes siempre tengan 2 dígitos, agregando un 0 delante si es necesario
#el f es para que sea una cadena formateada y se puedan usar las llaves {} para insertar variables dentro de la cadena
#el / es para separar el dia, mes y año
#el print es para imprimir en pantalla
#el for es para repetir el proceso 3 veces
#el range es para generar una secuencia de números desde 0 hasta 3 (no incluye el 3)
#el input es para pedir al usuario que ingrese un valor
#el int es para convertir el valor ingresado por el usuario en un número entero
#el append es para agregar un elemento al final de una lista
#ejercicio 4 

nombres=[]
apellidos=[]

for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ").capitalize()
    apellido = input(f"Ingrese el apellido de la persona {i+1}: ").capitalize()
    nombres.append(nombre),apellidos.append(apellido)
def ordenar_nombres_apellidos(apellido,nombre):
    n = len(apellido)
    for i in range(n):
        for j in range(0, n-i-1):#el rango es desde 0 hasta n-i-1 porque en cada pasada el último elemento ya está en su lugar correcto n es la longitud de la lista y i es el número de pasada actual y -1 es para evitar un índice fuera de rango
            if (apellido[j], nombre[j]) > (apellido[j+1], nombre[j+1]):
                apellido[j], apellido[j+1] = apellido[j+1], apellido[j]
                nombre[j], nombre[j+1] = nombre[j+1], nombre[j]
    return apellido, nombre
apellidos, nombres = ordenar_nombres_apellidos(apellidos, nombres)
print("ordenados por apellido y nombre:")
print()
for i in range(3):
    print(f"{apellidos[i]} {nombres[i]} ")
    
#el capitalize es para que la primera letra del nombre y apellido sea mayúscula y las demás minúsculas
#el f es para que sea una cadena formateada y se puedan usar las llaves {} para insertar variables dentro de la cadena
# ejercicio 5
import random as r

usuarios = int(input("Ingrese el número de usuarios que desea crear: "))
user = [input(f"Ingrese el usuario {i+1}: ") for i in range(usuarios)]
codigo = [r.randint(1000, 9999) for _ in range(usuarios)]

print("\nMENU DE OPCIONES")
print("1. Ingresar usuario")
print("2. Listar usuarios")
print("3. Salir")

opcion = int(input("Ingrese la opción que desea realizar: "))

while opcion != 3:
    match opcion:
        case 1:
            cod = int(input("Ingrese un código de 4 dígitos para saber si existe: "))
            if cod in codigo:
                print(f"El código {cod} existe y es del usuario {user[codigo.index(cod)]}")
            else:
                print(f"El código {cod} no existe")

        case 2:
            def ordenar_usuarios_x_codigo(usuarios, codigos):
                n = len(codigos)
                for i in range(n):
                    for j in range(0, n-i-1):#el rango es desde 0 hasta n-i-1 porque en cada pasada el último elemento ya está en su lugar correcto n es la longitud de la lista y i es el número de pasada actual y -1 es para evitar un índice fuera de rango
                        if codigos[j] > codigos[j+1]:
                            codigos[j], codigos[j+1] = codigos[j+1], codigos[j]
                            usuarios[j], usuarios[j+1] = usuarios[j+1], usuarios[j]
                return usuarios, codigos
            user, codigo = ordenar_usuarios_x_codigo(user, codigo)
            print("\nLista de usuarios ordenados por codigo :")
            for i in range(usuarios):
                print(f"Usuario: {user[i]} - Código: {codigo[i]}")

        case 3:
            print("Saliendo del programa...")
            break

        case _:
            print("Opción no válida")

    print("\nMENU DE OPCIONES")
    print("1. Ingresar usuario")
    print("2. Listar usuarios")
    print("3. Salir")
    opcion = int(input("Ingrese la opción que desea realizar: "))
