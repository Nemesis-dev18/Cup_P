import random
import time 
import emoji



#emojis 
casino_emoji = emoji.emojize(":slot_machine:")
croupier_emoji = emoji.emojize(":man_in_tuxedo:")
player_emoji = emoji.emojize(":person_playing_handball:")


card_emojis = {
    2: emoji.emojize(":two:"),
    3: emoji.emojize(":three:"),
    4: emoji.emojize(":four:"),
    5: emoji.emojize(":five:"),
    6: emoji.emojize(":six:"),
    7: emoji.emojize(":seven:"),
    8: emoji.emojize(":eight:"),
    9: emoji.emojize(":nine:"),
    10: emoji.emojize(":keycap_ten:"),
    11: emoji.emojize(":ace:")
}

print(f"Bienvenido al casino de Kingdice {casino_emoji}.")
print(f"Vamos a jugar blackjack {casino_emoji}.")
print(f"Iniciemos {casino_emoji}.")


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
print("bueno, iniciemos el juego")

# Juego ahora
cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
randuno = random.randint(0, 12)
randdos = random.randint(0, 12)
carta_1 = cartas[randuno]
carta_2 = cartas[randdos]
total = carta_1 + carta_2
print("Revolvamos el mazo")
time.sleep(3)
print(f"Primera carta: {card_emojis[carta_1]}")
time.sleep(2)
print("Y ahora la segunda es:")
time.sleep(2)
print(f"Segunda carta: {card_emojis[carta_2]}")

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
    time.sleep(3)

toda_carta = [carta_1, carta_2]
totalEX = sum(toda_carta)
time.sleep(3)
print(f"Estas son tus cartas: {toda_carta}")
print(f"Tu total oficial es: {totalEX}")
time.sleep(3)

# Jugador pide cartas adicionales
while totalEX < 21:
    decision = input("¿Quieres pedir otra carta? (s/n): ")
    if decision.lower() == 's':
        nueva_carta = cartas[random.randint(0, 12)]
        toda_carta.append(nueva_carta)
        totalEX += nueva_carta
        print(f"Te ha salido un {card_emojis[nueva_carta]}. Tu nuevo total es {totalEX}.")
    else:
        break

# La casa juega
carta_casa_1 = cartas[random.randint(0, 12)]
print(f"La carta descubierta de la casa es: {card_emojis[carta_casa_1]}")
time.sleep(3)
carta_casa_2 = cartas[random.randint(0, 12)]
print("La casa tiene una carta tapada.")
time.sleep(3)
todas_casa = [carta_casa_1, carta_casa_2]
total_casa = sum(todas_casa)

while total_casa <= 16:
    rand_otracasa = cartas[random.randint(0, 12)]
    time.sleep(3)
    otra_casa = cartas[rand_otracasa]
    todas_casa.append(otra_casa)
    total_casa += otra_casa
    print(f"La casa quiere otra y obtiene: {otra_casa}")
    time.sleep(3)

print(f"La carta tapada de la casa era: {card_emojis[carta_casa_2]}")
print(f"El total de la casa es {total_casa}")

# Resultados de quién ganó
if (totalEX > 21 and total_casa > 21) or (totalEX == total_casa and totalEX <= 21):
    dinero += bet
    print("Empate")
elif totalEX <= 21 < total_casa or (totalEX <= 21 and totalEX > total_casa):
    win = bet * 2
    dinero += win
    print(f"Tú ganas: {win}")
else:
    print("Tú pierdes")
print(f"Dinero restante: {dinero}")
