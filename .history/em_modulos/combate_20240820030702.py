import random

def actualizar_poderes(poder_jugador, poder_enemigo):
    """Actualiza los poderes del jugador y del enemigo en cada turno."""
    incremento_jugador = random.randint(5, 15)
    decremento_enemigo = random.randint(5, 10)
    poder_jugador += incremento_jugador
    poder_enemigo -= decremento_enemigo
    print(f"Turno {actualizar_poderes.turno}:")
    print(f"    Poder del jugador: {poder_jugador}")
    print(f"    Poder del enemigo: {poder_enemigo}")
    actualizar_poderes.turno += 1
    return poder_jugador, poder_enemigo

# Initialize the turn counter
actualizar_poderes.turno = 1

def resultado_combate(poder_jugador, poder_enemigo):
    """Determina el resultado de la batalla."""
    if poder_enemigo <= 0:
        print("Resultado final: Ganaste")
        return "Ganaste"
    else:
        print("Resultado final: Perdiste")
        return "Perdiste"
