print('RESTAURANTE El NOVENO CIRCULO')
print('Bienvenido ')
print('ESTE ES EL MENU')
print('Escoje correctamente tu orden')
print('Pero antes que todo ')
print('Dime tu nombre por favor')
nombre_correcto = False
while not nombre_correcto:
    nombre = input()
    print('¿Quedó bien escrito tu nombre así?', nombre)
    print('1 para sí, 2 para no')
    b = input()
    if b == '1':
        nombre_correcto = True
    elif b == '2':
        print('Por favor, ingresa tu nombre nuevamente:') 
    else:
        print('Error, por favor ingresa una opción correcta (1 o 2).')      

ver_menu_de_entradas = input('¿Te gustaría ver el menú de entradas? (S/N): ').lower()
if ver_menu_de_entradas == 's':
    #el menu de entradas
    print('Estas son nuestras entradas disponibles:')
    menu_entradas = {
        
        1: "Empanadas horneadas:",
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
                print(f"Entendido, continuemos con el menú principal.")
                entrada_seleccionada = True
            else:
                print("Por favor, ingresa un número que esté en nuestro menú de entradas.")
        except ValueError:
            print('Error, ingresa un número válido por favor')
if ver_menu_de_entradas == 'n':
    #menu de bebidas
    
 input("Presiona Eenter para ver el menu de bebidas")
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
    9: "jarra de jugo "
}
#menu de licores
print('Seleccion de licores')
menu_licores ={
    10: "Poker",
    11: "Cerveza artesanal",
    12: "Vino tinto",
    13: "Vino blanco",
    14: "Ron añejo",
    15: "Whisky escocés",
    16: "Tequila reposado",
    17: "Gin tonic",
    18: "Vodka premium"
}

for num_bebida, bebida in menu_bebidas.items():
    print(f"{num_bebida}. {bebida}")
for num_licor, licor in menu_licores.items():
    print(f"{num_licor}. {licor}")

    
bebida_seleccionada = False
while not bebida_seleccionada:
    try:
        eleccion_bebida = int(input('Por favor, escribe el número de la bebida que deseas: '))
        if eleccion_bebida in menu_bebidas or eleccion_bebida in menu_licores:
            bebida_seleccionada = True
        else:
            print("Por favor, ingresa un número que esté en nuestro menú de bebidas.")
    except ValueError:
        print('Error, ingresa un número válido por favor')
        
    print('Bueno, vamos a ver el menú principal entonces:')
    input("Presiona Enter para ver el menu principal")
# Aquí empieza el menú principal
input("Presiona Enter para ver el menu Principal")
print('Este es el menú del restaurante:')
menu_principal = {

    1: "Pechuga gratinada""(250gr)",
    2: "Sandwich de atún",
    3: "Arroz con pollo",
    4: "Arroz atollado",
    5: "Lomo saltado""300gr",
    6: "Ceviche de pescado",
    7: "Filete de salmón a la parrilla""(400)",
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

#confirmación de la orden
print(f"Excelente elección, {nombre}. Espero que disfrutes tu {menu_principal[eleccion_plato]} y tu {menu_bebidas.get(eleccion_bebida, menu_licores.get(eleccion_bebida))}.")

orden_correcta = False
while not orden_correcta:
    print('¿Está bien tu orden? (S/N)')
    respuesta = input().lower()
    if respuesta == 's':
        orden_correcta = True
        print('Gracias por tu pedido. ¡Que disfrutes tu comida!')
    elif respuesta == 'n':
        print('Lo siento por la confusión. ¿Qué te gustaría cambiar?')
    else:
        print('Por favor, ingresa una respuesta válida (S/N).')
