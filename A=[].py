#mas corto 
import numpy as np
while True:# el while true 
    print("\n---Sistema 3x3 con Cramer ---")
    # Matriz de coeficientes
    A = [list(map(float, input(f"Ecuación {i+1} (ej: 2 -3 4): ").split())) for i in range(3)]
    # Vector de igualdades
    b = [float(input(f"Resultado ecuación {i+1}: ")) for i in range(3)]#el for es para que vaya guardando las 3 ecuaciones 
    A, b = np.array(A), np.array(b)# el primer 
    detA = np.linalg.det(A)
    if detA == 0:
        print("❌ El sistema no tiene solución única (det(A)=0)")
    else:
        sol = [np.linalg.det(np.column_stack([b if j==i else A[:,j] for j in range(3)])) / detA for i in range(3)]
        print(f"\n Solución: x={sol[0]}, y={sol[1]}, z={sol[2]}")
    if input("\n¿Otro sistema? (s/n): ").lower() != 's':#el usuario decide si si o no y el while true acepta la condicion , si no rompe el ciclo 
        break
