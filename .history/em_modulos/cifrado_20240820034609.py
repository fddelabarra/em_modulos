import hashlib
import random

def generate_output(poder_jugador, poder_enemigo):
    turnos = 0
    output = ""
    
    while turnos < 10 and poder_enemigo > 0:
        poder_jugador += random.randint(5, 15)
        poder_enemigo -= random.randint(5, 10)
        output += f"Turno {turnos + 1}:\n"
        output += f"    Poder del jugador: {poder_jugador}\n"
        output += f"    Poder del enemigo: {poder_enemigo}\n"
        turnos += 1
    
    resultado = "Ganaste" if poder_enemigo <= 0 else "Perdiste"
    output += f"Resultado final: {resultado}"
    
    return output

def generate_secret_output(poder_jugador, poder_enemigo):
    output = generate_output(poder_jugador, poder_enemigo)
    str_list = output + "\n"
    hash_md5 = hashlib.md5(str_list.encode()).hexdigest()
    return hash_md5

def create_test_case(name, case_type, seed_value, poder_jugador, poder_enemigo, is_secret=False):
    random.seed(seed_value)
    output = generate_secret_output(poder_jugador, poder_enemigo) if is_secret else generate_output(poder_jugador, poder_enemigo)
    test_case = f"%NAME\n{name}\n%TYPE\n{case_type}\n%PRECODE\nfrom random import seed\nseed({seed_value})\n%INPUT\n{poder_jugador},{poder_enemigo},\n%CODE\n%OUTPUT\n{output}\n"
    return test_case

def generate_test_cases():
    public_cases = [
        (101, 30, 100),
        (202, 50, 150),
        (303, 40, 80),
        (404, 25, 120),
        (505, 35, 90),
        (606, 45, 110),
        (707, 55, 130),
        (808, 60, 140),
        (909, 20, 75),
        (1001, 10, 60)
    ]
    
    secret_cases = [
        (1102, 60, 200),
        (1203, 30, 180),
        (1304, 25, 160),
        (1405, 55, 190),
        (1506, 20, 170),
        (1607, 45, 150),
        (1708, 35, 140),
        (1809, 50, 130),
        (1900, 40, 120),
        (2001, 15, 100)
    ]
    
    test_cases = "%PREG\nPregunta 6\n"
    
    # Public cases
    for i, (seed_value, poder_jugador, poder_enemigo) in enumerate(public_cases, start=1):
        test_cases += create_test_case(f"Case {i}", "publico", seed_value, poder_jugador, poder_enemigo)
    
    # Secret cases
    for i, (seed_value, poder_jugador, poder_enemigo) in enumerate(secret_cases, start=1):
        test_cases += create_test_case(f"Case {i}", "secreto", seed_value, poder_jugador, poder_enemigo, is_secret=True)
    
    return test_cases

# Generate and save the test cases to a .txt file
test_cases = generate_test_cases()
with open("Pregunta6_test_cases.txt", "w") as file:
    file.write(test_cases)

print("Test cases generated and saved to Pregunta6_test_cases.txt")
