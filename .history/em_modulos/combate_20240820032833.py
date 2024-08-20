# Modified Modules

import random

def actualizar_poderes(poder_jugador, poder_enemigo):
    """Actualiza los poderes del jugador y del enemigo en cada turno."""
    incremento_jugador = random.randint(5, 15)
    decremento_enemigo = random.randint(5, 10)
    poder_jugador += incremento_jugador
    poder_enemigo -= decremento_enemigo
    return poder_jugador, poder_enemigo


def resultado_combate(poder_jugador, poder_enemigo):
    """Determina el resultado de la batalla."""
    if poder_enemigo <= 0:
        return "Ganaste"
    else:
        return "Perdiste"
