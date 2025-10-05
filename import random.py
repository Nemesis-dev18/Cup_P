import random
import time 

print("Bienvenido al casino de Kingdice.")
time.sleep(2)
print("Vamos a jugar blackjack.")
time.sleep(2)
print("Iniciemos")
time.sleep(2)

# Variables
dinero = int(input("¿Cuánto dinero quieres destinar para apostar?: "))

while True:
    print(f"Este es tu dinero: {dinero}")
    time.sleep(1)
    bet = int(input("¿Cuánto quieres apostar?: "))
    if dinero >= bet > 0:
        dinero -= bet
        break
    elif dinero < bet:
        print("El monto es más de lo que tienes.")
        time.sleep(1)
    elif bet <= 0:
        print("No puedes apostar eso.")
        time.sleep(1)

time.sleep(2)

# Juego ahora
cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
randuno = random.randint(0, 12)
randdos = random.randint(0, 12)
carta_1 = cartas[randuno]
carta_2 = cartas[randdos]
print("Revolvamos el mazo")
time.sleep(2)
print(f"Primera carta: {carta_1}")
time.sleep(2)
print("Y ahora la segunda es:")
time.sleep(2)
print(f"Segunda carta: {carta_2}")

# Verificación de As
if carta_1 == 11:
    total_1 = 1 + carta_2
    total_2 = 11 + carta_2
    print(f"Sacaste un As. Estos son tus dos posibles resultados: {total_1} o {total_2}")
    carta_1 = int(input("¿Qué valor quieres darle al As? (1 o 11): "))
if carta_2 == 11:
    total_1 = 1 + carta_1
    total_2 = 11 + carta_1
    print(f"Sacaste un As. Estos son tus dos posibles resultados: {total_1} o {total_2}")
    carta_2 = int(input("¿Qué valor quieres darle al As? (1 o 11): "))
    time.sleep(2)

toda_carta = [carta_1, carta_2]
totalEX = sum(toda_carta)
print(f"Estas son tus cartas: {toda_carta}")
time.sleep(2)
print(f"Tu total oficial es: {totalEX}")
time.sleep(2)

while totalEX <= 21:
    nueva_carta = input("¿Quieres otra carta? (si o no): ").lower()
    if nueva_carta == 'si' or nueva_carta == 's':
        rand_otra = random.randint(0, 12)
        otra_carta = cartas[rand_otra]
        toda_carta.append(otra_carta)
        totalEX += otra_carta
        print(f"Tu nueva carta es: {otra_carta}")
        time.sleep(2)
        print(f"Estas son tus cartas: {toda_carta}")
        time.sleep(2)
        print(f"Tu total es: {totalEX}")
        time.sleep(2)
        if totalEX > 21:
            print("Te pasaste")
            time.sleep(2)
            print("Veamos si la casa también pierde")
            break
    elif nueva_carta == 'no' or nueva_carta == 'n':
        break
    else:
        print("Respuesta no válida. Escribe 'si' o 'no'.")

time.sleep(2)
print("Ahora va a jugar la casa. Veamos tu suerte.")

# La casa juega
carta_casa_1 = random.randint(0, 12)
casa_carta1 = cartas[carta_casa_1]
print(f"La primera carta de la casa es: {casa_carta1}")
time.sleep(2)
carta_casa_2 = random.randint(0, 12)
casa_carta2 = cartas[carta_casa_2]
print(f"La segunda carta de la casa es: {casa_carta2}")
time.sleep(2)
todas_casa = [casa_carta1, casa_carta2]
total_casa = casa_carta1 + casa_carta2
time.sleep(2)

while total_casa <= 16:
    rand_otracasa = random.randint(0, 12)
    otra_casa = cartas[rand_otracasa]
    todas_casa.append(otra_casa)
    total_casa += otra_casa
    print(f"La casa quiere otra y obtiene: {otra_casa}")
    time.sleep(2)
    if total_casa > 21:
        print("La casa se pasó, tú ganas.")
        break

print(f"Tu resultado es {totalEX} y el de la casa es {total_casa}")

# Resultados de quién ganó
if totalEX > 21 and total_casa > 21:
    dinero += bet
    print("Empate, ambos se pasaron")
elif totalEX == total_casa:
    dinero += bet
    print("Empate")
elif totalEX <= 21 < total_casa or (totalEX <= 21 and totalEX > total_casa):
    win = bet * 2
    dinero += win
    print(f"Tú ganas: {win}")
else:
    print("Tú pierdes")

print(f"Dinero restante: {dinero}")
