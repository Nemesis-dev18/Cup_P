#explciacion del def 

# Esta función no hace nada, pero sirve como ejemplo para explicar la palabra clave 'def' en Python.
# La palabra clave 'def' se utiliza para definir una función en Python. 
# Una función es un bloque de código reutilizable que realiza una tarea específica.

# La sintaxis básica para definir una función es:

# def nombre_de_la_funcion(parametros):
#     # cuerpo de la función
#     instrucciones
#     return valor_de_retorno
# Donde:
# - 'def' es la palabra clave que indica el inicio de la definición de una función
# - 'nombre_de_la_funcion' es el nombre que le das a la función (debe seguir las reglas de nomenclatura de Python)
# - 'parametros' son los valores que la función puede recibir (opcional)
# - El cuerpo de la función contiene las instrucciones que se ejecutan cuando se llama a la función
# - 'return' es una palabra clave opcional que se utiliza para devolver un valor desde la función
# valor de retorno es el valor que la función devuelve cuando se completa su ejecución. 
# def ejemplo():
#     print("Hola, esta es una función de ejemplo.")  
# # Llamar a la función para ver su efecto
# ejemplo()

# def factorial(n):
# #"""Calcula el factorial de un número n."""
#     if n == 0 or n == 1:
#         return 1 # el retur 1 es para que la funcion retorne un valor de 1 cuando n es 0 o 1
#     else:
#         return n * factorial(n - 1)




def mensaje(n, mensaje="hola"):
    if n == 0:
        print(mensaje)
        return 1

# Ejemplo de uso de la función
mensaje(1)
