import time
while True:
    num = input("Ingresa un número para saber si es par o impar: ")
    time.sleep(2)
    try:
        num=int(num)    
    except ValueError:
        print("tu numero no es entero, no podemos seguir. Por favor ingresa un numero entero ")
    else:
        if num % 2 == 0 :
            print(f"tu numero es par")
        else:
            print(f"tu numero es impar")
    while True:
        repetir = input("¿Quieres repetir la prueba? (S/N): ").strip().lower()
        if repetir not in ['s', 'n']:
            print("Entrada no válida. Por favor, ingresa 'S' para sí o 'N' para no.")
        else:
            break
    
    if repetir == 'n':
        break