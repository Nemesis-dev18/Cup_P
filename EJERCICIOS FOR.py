
# EJERCICIO 1

# Pedimos la edad al usuario
edad = int(input("¿Cuántos años tienes?: "))

# Recorremos desde 1 hasta la edad ingresada
# range(1, edad+1) → incluye el número final
for i in range(1, edad+1):
    # Mostramos todas las edades cumplidas
    print(f"Has cumplido {i} años")


# ALGORITMO 2

# Pedimos un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Recorremos desde 1 hasta n inclusive
for j in range(1, n+1):
    # Imprimimos cada número en la misma línea, separados por comas
    print(j, end=", ")


# ALGORITMO 3

# Pedimos un número entero positivo
n2 = int(input("Introduce un número entero positivo: "))

# Recorremos hacia atrás desde n2 hasta 0 (con paso -1)
for q in range(n2, -1, -1):
    # Imprimimos los números en la misma línea
    print(q, end=", ")

# ALGORITMO 4

# Pedimos la altura del triángulo
n3 = int(input("Introduce la altura del triángulo (positivo): "))

# Recorremos desde 1 hasta la altura
for w in range(1, n3+1):
    # En cada fila imprimimos tantos * como el número de la fila
    for e in range(w):
        print("*", end="")  # end="" evita saltos de línea entre *
    print()  # salto de línea al terminar cada fila


# ALGORITMO 5

# Pedimos un número mayor que 2
n4 = int(input("Introduce un número entero positivo mayor que 2: "))

# Si el número no es válido, mostramos un mensaje
if n4 <= 2:
    print("El número es menor o igual que 2, vuelva a intentarlo.")
else:
    # Suponemos que es primo al inicio
    es_primo = True

    # Probamos divisores desde 2 hasta n4-1
    for t in range(2, n4):
        # Si encontramos un divisor exacto, no es primo
        if n4 % t == 0:
            es_primo = False
            break  # salimos del bucle para ahorrar tiempo

    # Verificamos el resultado
    if es_primo:
        print(n4, "es primo")
    else:
        print(n4, "no es primo")



# ALGORITMO 6

# Pedimos el tamaño de la palabra (número de letras que tendrá)
n5 = int(input("Introduce el tamaño de la palabra: "))

# Creamos una lista vacía para ir guardando las letras
palabra = []

# Recorremos desde 0 hasta n5-1
for y in range(n5):
    # Pedimos la letra número (y+1) para que el usuario entienda que empieza desde 1
    letra = input(f"Introduce la letra número {y+1}: ")
    # Con .append() agregamos la letra a la lista
    palabra.append(letra)

# Usamos join() para convertir la lista en una cadena
# Ejemplo: ['h','o','l','a'] → "hola"
print("La palabra es:", "".join(palabra))

# Usamos [::-1] para invertir la lista
# Ejemplo: ['h','o','l','a'][::-1] → ['a','l','o','h']
# Y nuevamente join() para mostrarlo como una cadena
print("La palabra al revés es:", "".join(palabra[::-1]))
#echo por Jean Paul Delgadillo Moreno en media paranoia a las 11:59 pm 