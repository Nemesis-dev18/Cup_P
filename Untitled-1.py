print('RESTAURANTE El NOVENO CIRCULO')
print('Bienvenido')
print('ESTE ES EL MENU')
print('Escoje correctamente tu orden')
print('Pero antes que todo')
print('Dime tu nombre por favor')

nombre_correcto = False
while not nombre_correcto:
    nombre = input("Por favor, ingresa tu nombre: ")
    print('¿Quedo bien escrito tu nombre así?', nombre)
    respuesta = input('¿Sí o no?: ').lower()
    if respuesta == 'si' or respuesta == 'sí' or respuesta == 's':
        nombre_correcto = True
    elif respuesta == 'no' or respuesta == 'n':
        print('Por favor, ingresa tu nombre nuevamente:')
    else:
        print('Error, por favor responde con "sí" o "no".')

ver_menu_de_entradas = input('¿Te gustaría ver el menú de entradas? (S/N): ').lower()

if ver_menu_de_entradas == 's':
    # el menu de entradas
    print('Estas son nuestras entradas disponibles:')
    menu_entradas = {
        1: "Empanadas hsaorneadas:",
        2: "Sopa de verduras",
        3: "Rollitos de primavera",
        4: "Bruschetta"
    }
    for num_entrada, entrada in menu_entradas.items():
        print(f"{num_entrada}. {entrada}")
    entrada_seleccionada = False
    while not entrada_seleccionada:
        try:
            eleccion = int(input('Por favor, escribe el número de la entrada que deseas: '))
            if eleccion in menu_entradas:
                print("Entendido, continuemos con el menú principal.")
                entrada_seleccionada = True
            else:
                print("Por favor, ingresa un número que esté en nuestro menú de entradas.")
        except ValueError:
            print('Error, ingresa un número válido por favor')
elif ver_menu_de_entradas == 'n':
    # menu de bebidas
    input("Presiona Enter para ver el menú de bebidas")
    print('Este es el menú de bebidas:')
    menu_bebidas = {
        1: "Agua mineral",
        2: "Refresco de cola",
        3: "Limonada natural",
        4: "Té helado",
        5: "Jugo de naranja natural",
        6: "Café americano",
        7: "Agua de coco",
        8: "Batido de frutas",
        9: "Jarra de jugo"
    }
    for num_bebida, bebida in menu_bebidas.items():
        print(f"{num_bebida}. {bebida}")
    bebida_seleccionada = False
    while not bebida_seleccionada:
        try:
            eleccion_bebida = int(input('Por favor, escribe el número de la bebida que deseas: '))
            if eleccion_bebida in menu_bebidas:
                bebida_seleccionada = True
            else:
                print("Por favor, ingresa un número que esté en nuestro menú de bebidas.")
        except ValueError:
            print('Error, ingresa un número válido por favor')
            break


# Aquí empieza el menú principal
input("Presiona Enter para ver el menú Principal")
print('Este es el menú del restaurante:')
menu_principal = {
    1: "Pechuga gratinada (250gr)",
    2: "Sandwich de atún",
    3: "Arroz con pollo",
    4: "Arroz atollado",
    5: "Lomo saltado (300gr)",
    6: "Ceviche de pescado",
    7: "Filete de salmón a la parrilla (400)",
    8: "Hamburguesa gourmet",
    9: "Pizza margarita"
}
for num_plato, plato in menu_principal.items():
    print(f"{num_plato}. {plato}")

plato_seleccionado = False
while not plato_seleccionado:
    try:
        eleccion_plato = int(input('Por favor, escribe el número del plato principal que deseas: '))
        if eleccion_plato in menu_principal:
            plato_seleccionado = True
        else:
            print("Por favor, ingresa un número que esté en nuestro menú principal.")
    except ValueError:
        print('Error, ingresa un número válido por favor')
        
# menu de bebidas
    input("Presiona Enter para ver el menú de bebidas")
    print('Este es el menú de bebidas:')
    
    menu_bebidas = {
        1: "Agua mineral",
        2: "Refresco de cola",
        3: "Limonada natural",
        4: "Té helado",
        5: "Jugo de naranja natural",
        6: "Café americano",
        7: "Agua de coco",
        8: "Batido de frutas",
        9: "Jarra de jugo"
    }
    for num_bebida, bebida in menu_bebidas.items():
       bebida_seleccionada = print(f"{num_bebida}. {bebida}")

 
while not bebida:
        try:
            eleccion = int(input('Por favor, escribe el número de la bebida que deseas  que deseas: '))
            if eleccion in menu_bebidas:
                print("Entendido, excelente eleccion")
                num_bebida = True
            else:
                print("Por favor, ingresa un número que esté en nuestro menú de bebidas.")
        except ValueError:
            print('Error, ingresa un número válido por favor')
        break
# confirmacion de la orden
if eleccion_plato in menu_principal:
    if ver_menu_de_entradas == 's':
        print(f"Excelente elección, {nombre}. Espero que disfrutes tu {menu_principal[eleccion_plato]} y su {menu_bebidas[num_bebida]}. Mientras tanto, disfruta tus {menu_entradas[eleccion]}.")
else:
    if ver_menu_de_entradas == "n":
        print(f"Excelente elección, {nombre}. Espero que disfrutes tu {menu_principal[eleccion_plato]} y su {menu_bebidas[num_bebida]}. Ya se te traerá tu plato.")
  