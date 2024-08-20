import random

def actualizar_poderes(poder_jugador, poder_enemigo):
    """Actualiza los poderes del jugador y del enemigo en cada turno."""
    incremento_jugador = random.randint(5, 15)
    decremento_enemigo = random.randint(5, 10)
    poder_jugador += incremento_jugador
    poder_enemigo -= decremento_enemigo
    return poder_jugador, poder_enemigo

def estado_ronda(poder_jugador, poder_enemigo):
    """Devuelve el estado de la ronda actual como una cadena."""
    estado += f"    Poder del jugador: {poder_jugador}\n"
    estado += f"    Poder del enemigo: {poder_enemigo}"
    return estado

def resultado_combate(poder_jugador, poder_enemigo):
    """Determina el resultado de la batalla."""
    if poder_enemigo <= 0:
        return "Resultado final: Ganaste"
    else:
        return "Resultado final: Perdiste"
