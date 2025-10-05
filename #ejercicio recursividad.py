n = int(input("Ingrese un número: "))

def fibonacci(n):
    if n < 0:
        print("El número debe ser mayor o igual a 0.")
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):# el 2 ahi esta porque ya tenemos los 2 primeros numeros 
            suma = a + b
            print(f"{a} + {b} = {suma}",end="' -> '")
            a, b = b, suma
        return b

print(f"Resultado final: {fibonacci(n)}")
