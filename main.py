from datetime import datetime


# Función que devuelve un saludo basado en la hora actual
def ohce_greeting(name):
    hora_actual = datetime.now().hour
    if  6 <= hora_actual < 12:
        return f"¡Buenos días {name}!"
    elif 12 <= hora_actual < 20:
        return f"¡Buenas tardes {name}!"
    else:
        return f"¡Buenas noches {name}!"

# Función que devuelve una palabra al revés
def ohce_echo(word):
    return word[::-1]