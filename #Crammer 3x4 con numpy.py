# #Crammer 3x4 con numpy 
# import numpy as np 

# # Inicializamos la opción para entrar al bucle
# opcion = 's'

# while opcion == 's':
#     A=[]
#     b=[]

#     print("Este programa resuelve un sistema de 3 ecuaciones con 3 incógnitas usando la Regla de Cramer.")

#     # Entrada de la matriz A
#     print("\nIngrese los coeficientes de cada ecuación:")
#     for i in range(3):
#         while True:
#             try:
#                 fila = input(f"Ecuación {i+1} (ejemplo: 2 -3 4): ").strip().split()
#                 if len(fila) != 3:
#                     print("❌ Cada fila debe tener exactamente 3 coeficientes.")
#                     continue
#                 fila = [float(x) for x in fila]
#                 A.append(fila)
#                 break
#             except ValueError:
#                 print("❌ Entrada inválida. Use solo números (ej: 2 -3 4).")

#     # Entrada del vector b
#     print("\nIngrese los valores de igualdad:")
#     for i in range(3):
#         while True:
#             try:
#                 val = float(input(f"Resultado de la ecuación {i+1}: "))
#                 b.append(val)
#                 break
#             except ValueError:
#                 print("❌ Entrada inválida. Ingrese un número.")

#     # Convertir a arrays
#     A = np.array(A)
#     b = np.array(b)

#     print("\nMatriz de coeficientes A:\n", A)
#     print("Vector de igualdades b:\n", b)

#     # Determinante principal
#     detA = np.linalg.det(A)

#     if detA == 0:
#         print("\n❌ El sistema no tiene solución única (det(A)=0)")
#     else:
#         # Construcción de matrices para Cramer
#         Ax = A.copy()
#         Ax[:,0] = b

#         Ay = A.copy()
#         Ay[:,1] = b

#         Az = A.copy()
#         Az[:,2] = b

#         # Solución con Cramer
#         x = np.linalg.det(Ax) / detA
#         y = np.linalg.det(Ay) / detA
#         z = np.linalg.det(Az) / detA

#         print("\nSolución del sistema:")
#         print(f"x = {x}, y = {y}, z = {z}")

#     # Preguntar si desea otro sistema
#     opcion = input("\n¿Quiere hacer otro sistema de ecuaciones? (s/n): ").lower()
#     while opcion not in ['s', 'n']:
#         opcion = input("Por favor ingrese 's' para sí o 'n' para no: ").lower()

# print("\nGracias por usar el programa. ¡Hasta luego!")


