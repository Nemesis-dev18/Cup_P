import itertools
import re

# Diccionario de conversión de símbolos lógicos a Python
SIMBOLOS_A_PYTHON = {
    "¬": "not ",  # Negación con ¬
    "~": "not ",  # Negación con ~
    "^": " and ",  # Conjunción (AND)
    "∧": " and ",  # Conjunción con ∧
    "v": " or ",  # Disyunción (OR)
    "∨": " or ",  # Disyunción alternativa (OR)
    "→": " <= ",  # Implicación (not p or q)
    "->": " <= ",
    "<-": " => ",
    "<->": " == ",
    "↔": " == ",  # Bicondicional (p ↔ q)
    " ⊕ ": " != ",  # XOR (p ⊕ q)
    " oplus ": " != ",  # Alternativa para XOR
}

def convertir_a_python(expresion):
    """Convierte una expresión lógica con símbolos a su equivalente en Python."""
    for simbolo, python_equivalente in SIMBOLOS_A_PYTHON.items():
        expresion = expresion.replace(simbolo, python_equivalente)
    
    # Convertir correctamente las implicaciones
    expresion = re.sub(r"(\w+)\s*<=\s*(\w+)", r"not \1 or \2", expresion)
    
    return expresion

def obtener_variables(expresion):
    """Extrae las variables únicas de una expresión lógica, excluyendo 'V' y 'v'."""
    variables = sorted(set(re.findall(r"[a-zA-Z]", expresion)))
    return [var for var in variables if var not in ['V', 'v']]  # Filtra 'V' y 'v'

def obtener_subexpresiones(expresion):
    """Extrae las subexpresiones con paréntesis primero y negaciones después."""
    subexpresiones = {}
    
    # Extraer subexpresiones entre paréntesis primero
    operadores_regex = r"\(([^()]+)\)"
    partes = re.findall(operadores_regex, expresion)
    for parte in partes:
        subexpresiones[f"({parte})"] = convertir_a_python(parte)
    
    # Extraer negaciones después de los operadores
    negaciones = re.findall(r"[¬~]\w", expresion)
    for neg in negaciones:
        subexpresiones[neg] = neg.replace("¬", "not ").replace("~", "not ")
    
    return subexpresiones

def generar_tabla_verdad(expresion):
    """Genera y muestra o guarda la tabla de verdad para una expresión lógica."""
    try:
        expresion_python = convertir_a_python(expresion)
        variables = obtener_variables(expresion)
        subexpresiones = obtener_subexpresiones(expresion)
        combinaciones = list(itertools.product([True, False], repeat=len(variables)))

        # Crear encabezado con pasos intermedios
        encabezado = " | ".join([var.center(3) for var in variables] + 
                                [key.center(7) for key in subexpresiones.keys()] + 
                                ["ALL".center(7)])
        separador = "-" * len(encabezado)

        # Si hay más de 10 variables, guardar en archivo en vez de mostrar en consola
        guardar_en_archivo = len(variables) > 10
        salida = []

        # Agregar encabezado
        salida.append(f"\nTabla de Verdad para: {expresion}\n")
        salida.append(encabezado)
        salida.append(separador)

        for valores in combinaciones:
            contexto = dict(zip(variables, valores))  # Crea {p: True, q: False, ...}
            resultados_intermedios = {expr: eval(code, {}, contexto) for expr, code in subexpresiones.items()}
            resultado_final = eval(expresion_python, {}, contexto)

            # Convertir valores booleanos a "V" o "F" y centrar cada valor
            valores_str = " | ".join([str("V" if v else "F").center(3) for v in valores])
            pasos_str = " | ".join([str("V" if v else "F").center(7) for v in resultados_intermedios.values()])
            resultado_final_str = str("V" if resultado_final else "F").center(7)

            # Agregar la fila con los resultados de cada sub-expresión y el resultado final
            salida.append(f"{valores_str} | {pasos_str} | {resultado_final_str}")

        if guardar_en_archivo:
            with open("tabla_verdad.txt", "w", encoding="utf-8") as archivo:
                archivo.write("\n".join(salida))
            print(f"⚠️ La tabla de verdad es demasiado grande. Se ha guardado en 'tabla_verdad.txt'.")
        else:
            print("\n".join(salida))

    except Exception as e:
        print(f"Error: La expresión lógica es inválida o mal formada. Detalle del error: {e}")

# Pedir la expresión lógica al usuario
expresion_usuario = input("Ingresa la expresión lógica usando símbolos (¬, ~, ^, ∧, v, ∨, →, ↔, ⊕ ): ")

# Generar la tabla de verdad con los pasos intermedios
generar_tabla_verdad(expresion_usuario)
