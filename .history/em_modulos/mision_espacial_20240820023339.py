import random

random.seed(42)

def estado_mision(nivel_energia, muestra, muestras_recolectar):
    """Imprime el estado de la misión según el nivel de energía y las muestras recolectadas."""
    if nivel_energia <= 0:
        print("Estado de la mision: Mision fallida")
    elif muestra < muestras_recolectar:
        print("Estado de la mision: En progreso")
    else:
        print("Estado de la mision: Mision exitosa")

def recolectar_muestra(nivel_energia, muestra, muestras_recolectar):
    """Reduce el nivel de energía de la nave después de recolectar una muestra y verifica el estado de la misión."""
    print(f"Recolectando muestra {muestra}...")
    consumo_energia = random.randint(10, 30)
    nivel_energia -= consumo_energia
    print(f"Nivel de energia actual: {nivel_energia}")
    estado_mision(nivel_energia, muestra, muestras_recolectar)
    return nivel_energia
