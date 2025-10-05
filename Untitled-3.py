import copy
import re
# Verifica que el token ingresado sea válido:
# - Ejemplo: 2x, -3y, 5z (coeficiente con variable)
# - O un número entero (para el término independiente)
def es_valido(item):
    return re.match(r"^-?\d+[xyz]$", item) or re.match(r"^-?\d+$", item)


print("Ingrese los valores de la matriz A (3x3) donde el 4to valor es la igualdad:")
print("Ejemplo: 2x -3y 4z 10   (que significa 2x - 3y + 4z = 10)")


# Entrada de datos: 3 filas con 4 elementos cada una

listax = []
for i in range(3):
    fila = input(f"escribe los numeros de la fila {i+1}/3: ").strip().split()
    if len(fila) != 4:
        print("Cada fila debe tener exactamente 4 valores.")
        exit()
    listax.extend(fila)

# Validamos que sean 12 datos
if len(listax) != 12:
    print("Error: Debes ingresar exactamente 12 valores (3 filas × 4 columnas).")
    exit()

# Verificar que cada valor sea válido
for token in listax:
    if not es_valido(token):
        print(f"Error: '{token}' no es válido. Debe ser un número entero o un valor como 2x, -3y, 4z")
        exit()

# Reorganizamos en matriz 3x4
matriz = [listax[i:i+4] for i in range(0, 12, 4)]


# Normalizar filas: siempre en orden [x, y, z, resultado]

normalizada = []
for fila in matriz:
    nueva_fila = ["0x", "0y", "0z", fila[-1]]  # valores por defecto
    for var in ["x", "y", "z"]:
        for item in fila[:-1]:
            if item.endswith(var):
                if var == "x":
                    nueva_fila[0] = item
                elif var == "y":
                    nueva_fila[1] = item
                elif var == "z":
                    nueva_fila[2] = item
    normalizada.append(nueva_fila)


# Mostrar matriz original con las variables y el "="

lista_original = copy.deepcopy(normalizada)
for fila in lista_original:
    fila.insert(3, "=")

print("\nMatriz original :")
for fila in lista_original:
    print(" ".join(fila))

print("\n------------------\n")


# Extraer coeficientes numéricos (matriz de 3x3) y vector resultado

matriz_coef = []  # matriz de coeficientes
vector_res = []   # vector de resultados

for fila in normalizada:
    coef_fila = []
    for item in fila[:3]:  # solo coeficientes de x, y, z
        coef = item[:-1]   # quitamos la letra final
        if coef == '' or coef == '+':
            coef = '1'
        elif coef == '-':
            coef = '-1'
        coef_fila.append(int(coef))
    matriz_coef.append(coef_fila)
    vector_res.append(int(fila[3]))

print("Matriz de coeficientes (3x3):")
for fila in matriz_coef:
    print(" ".join(map(str, fila)))
print("\n------------------\n")
print("Vector de igualdades:")
print(" ".join(map(str, vector_res)))



# Función para calcular determinante 3x3 (con debug opcional)

def determinante_3x3(m, debug=False, nombre="D"):
    grupo1 = (m[0][0] * m[1][1] * m[2][2] +
              m[0][1] * m[1][2] * m[2][0] +
              m[0][2] * m[1][0] * m[2][1])

    grupo2 = (m[0][2] * m[1][1] * m[2][0] +
              m[0][0] * m[1][2] * m[2][1] +
              m[0][1] * m[1][0] * m[2][2])

    det = grupo1 - grupo2

    if debug:
        print(f"\nDeterminante {nombre}:")
        print("  Grupo 1 (diagonales principales):", grupo1)
        print("  Grupo 2 (diagonales secundarias):", grupo2)
        print(f"  {nombre} = {grupo1} - {grupo2} = {det}")

    return det



# Reemplaza una columna de la matriz por el vector de resultados

def reemplazar_columna(m, col_index, nueva_col):
    m_copy = copy.deepcopy(m)
    for i in range(3):
        m_copy[i][col_index] = nueva_col[i]
    return m_copy



# Cálculo de determinantes para Cramer

D  = determinante_3x3(matriz_coef, debug=True, nombre="D")
if D == 0:
    print("\nEl sistema no tiene solución única (determinante es 0).")
    exit()

Dx = determinante_3x3(reemplazar_columna(matriz_coef, 0, vector_res), debug=True, nombre="Dx")
Dy = determinante_3x3(reemplazar_columna(matriz_coef, 1, vector_res), debug=True, nombre="Dy")
Dz = determinante_3x3(reemplazar_columna(matriz_coef, 2, vector_res), debug=True, nombre="Dz")


# Cálculo de soluciones finales

x = Dx / D
y = Dy / D
z = Dz / D

print("\n------------------\n")
print()
print("Soluciones del sistema:")
print(f"x = {x:.2f}")
print(f"y = {y:.2f}")
print(f"z = {z:.2f}")

input("\nPresiona ENTER para salir...")
