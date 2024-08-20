import random

def estado_mision(nivel_energia, muestra, muestras_recolectar):
    """Prints the mission status based on the energy level and samples collected."""
    if nivel_energia <= 0:
        print("Estado de la misión: Misión fallida")
    elif muestra < muestras_recolectar:
        print("Estado de la misión: En progreso")
    else:
        print("Estado de la misión: Misión exitosa")

def recolectar_muestra(nivel_energia, muestra, muestras_recolectar):
    """Reduces the energy level of the ship after collecting a sample and checks the mission status."""
    print(f"Recolectando muestra {muestra}...")
    consumo_energia = random.randint(10, 30)
    nivel_energia -= consumo_energia
    print(f"Nivel de energía actual: {nivel_energia}")
    estado_mision(nivel_energia, muestra, muestras_recolectar)
    return nivel_energia
