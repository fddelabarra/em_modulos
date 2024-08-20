import math

def calcular_altura_maxima(velocidad, angulo):
    angulo_radianes = math.radians(angulo)
    altura_maxima = (velocidad**2 * math.sin(angulo_radianes)**2) / (2 * 9.81)
    return round(altura_maxima, 2)
