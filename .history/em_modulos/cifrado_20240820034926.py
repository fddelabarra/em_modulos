import random

def generar_desplazamiento():
    """Genera un valor de desplazamiento aleatorio para el cifrado."""
    return random.randint(1, 3)

def cifrar_mensaje(mensaje, desplazamiento):
    """Cifra el mensaje desplazando cada letra según el desplazamiento indicado."""
    mensaje_cifrado = []
    for letra in mensaje:
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')
            nueva_letra = chr((ord(letra) - base + desplazamiento) % 26 + base)
            mensaje_cifrado.append(nueva_letra)
        else:
            mensaje_cifrado.append(letra)
    return ''.join(mensaje_cifrado)

def descifrar_mensaje(mensaje_cifrado, desplazamiento):
    """Descifra el mensaje invirtiendo el cambio de cifrado."""
    mensaje_descifrado = []
    for letra in mensaje_cifrado:
        if letra.isalpha():
            base = ord('a') if letra.islower() else ord('A')
            nueva_letra = chr((ord(letra) - base - desplazamiento) % 26 + base)
            mensaje_descifrado.append(nueva_letra)
        else:
            mensaje_descifrado.append(letra)
    return ''.join(mensaje_descifrado)
