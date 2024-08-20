import random

def estado_mision(nivel_energia, muestra, muestras_recolectar):
    """Devuelve el estado de la misión según el nivel de energía y las muestras recolectadas."""
    if nivel_energia <= 0:
        return "Estado de la mision: Mision fallida"
    elif muestra < muestras_recolectar:
        return "Estado de la mision: En progreso"
    else:
        return "Estado de la mision: Mision exitosa"

def recolectar_muestra(nivel_energia, muestra, muestras_recolectar):
    """Reduce el nivel de energía de la nave después de recolectar una muestra y verifica el estado de la misión."""
    consumo_energia = random.randint(10, 30)
    nivel_energia -= consumo_energia
    return nivel_energia