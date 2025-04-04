from datetime import datetime
import sys


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

# Función que chequea si una palabra es un palíndromo
def ohce_palindrome(word):
    return word == word[::-1]

# Función que chequea si una palabra es el comando de salida
def ohce_stop(word):
    return word == 'Stop!'

# Función principal que ejecuta el programa
if __name__ == "__main__":
    name = None
    if len(sys.argv) == 2:
        name = sys.argv[1]
    else:
        print("Error: Debe ingresar un nombre como argumento.")
        sys.exit(1)
    print(ohce_greeting(name))
    while True:
        word = input('> ')
        if ohce_stop(word):
            print(f'Adios {name}')
            break
        print(ohce_echo(word))
        if ohce_palindrome(word):
            print('¡Bonita palabra!')