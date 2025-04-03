from datetime import datetime


# Función que devuelve un saludo basado en la hora actual
def ohce_greeting(name):
    hora_actual = datetime.now().hour
    if hora_actual < 12:
        return f"¡Buenos días {name}!"
    else:
        return f"¡Buenas tardes {name}!"