import random

# Son los puntos para hacer game/juego.
puntos_uno = 0
puntos_dos = 0

# Son los juegos para marcar un set.
juegos_uno = 0
juegos_dos = 0

# Son los sets del juego.
set_uno = 0
set_dos = 0

# Variable game para controlar el flujo del juego.
game = True

# Variable global punto.
punto = 0

# "Volado" a ver que jugador saca primero.
aleatorio = random.randint(0,1)

# Nombres de los jugadores.
nombres_jugadores = []


# Función que pide y guarda los nombres de los jugadores.
def pide_nombres():
    nombres = []
    nombre_uno = input("Escribe el nombre del primer jugador: ")
    nombres.append(nombre_uno)
    nombre_dos = input("Escribe el nombre del segundo jugador: ")
    nombres.append(nombre_dos)
    return nombres


# Función que regresa quien saca la pelota.
def saque():
    global nombres_jugadores
    print("El saque es para: "+nombres_jugadores[aleatorio % 2]+"\n")


# Función que avisa cuando hay cambio de cancha.
def cambio_cancha():
    if (juegos_uno + juegos_dos) % 2 == 1:
        print("SE REALIZA CAMBIO DE CANCHA")


# Función que muestra el marcador del partido antes de hacer un game.
def marcador_puntos():
    global puntos_uno
    global puntos_dos

    # Como utilizo contadores para contar puntos, aquí se calcula lo que representarían en realidad.
    if puntos_uno == 0:
        marcador_uno = "0"
    elif puntos_uno == 1:
        marcador_uno = "15"
    elif puntos_uno == 2:
        marcador_uno = "30"
    elif (puntos_uno >= 3 and puntos_uno == puntos_dos) or (3 <= puntos_uno < puntos_dos) or (puntos_uno == 3):
        marcador_uno = "40"
    else:
        marcador_uno = "Adv"

    if puntos_dos == 0:
        marcador_dos = "0"
    elif puntos_dos == 1:
        marcador_dos = "15"
    elif puntos_dos == 2:
        marcador_dos = "30"
    elif (puntos_dos >= 3 and puntos_dos == puntos_uno) or (3 <= puntos_dos < puntos_uno) or (puntos_dos == 3):
        marcador_dos = "40"
    else:
        marcador_dos = "Adv"

    return marcador_uno + " - " + marcador_dos


# Función que realiza el conteo de puntos hasta que se haga un game.
def conteo_puntos(param):
    global puntos_uno
    global puntos_dos
    global juegos_uno
    global juegos_dos

    # Utilizo contadores para saber los puntos que marcan game (ver linea 55).
    if param == 1:
        puntos_uno += 1
    else:
        puntos_dos += 1

    # Si un jugador marca un punto después de tener Adv obtiene un juego.
    if puntos_uno > 3 and puntos_uno - puntos_dos >= 2 :
        print("\nGame para "+nombres_jugadores[0])
        juegos_uno += 1
        return False

    if puntos_dos > 3 and puntos_dos - puntos_uno >= 2:
        print("\nGame para "+nombres_jugadores[1])
        juegos_dos += 1
        return False

    print("\nMARCADOR\n" + marcador_puntos())
    return True


# Función que muestra el marcador en los juegos.
def marcador_juegos():
    global nombres_jugadores
    print("\nJuegos: "+nombres_jugadores[0]+" "+str(juegos_uno)+" - "+str(juegos_dos)+" "+nombres_jugadores[1]+" \n")


# Función que realiza el conteo de juegos para un set.
def conteo_juegos():
    global set_uno
    global set_dos
    global game
    if juegos_uno >= 6 and juegos_uno - juegos_dos >= 2:
        print("\nSet para " + nombres_jugadores[0])
        set_uno += 1
        game = False
        return False

    if juegos_dos >= 6 and juegos_dos - juegos_uno >= 2:
        print("\nSet para " + nombres_jugadores[1])
        set_dos += 1
        game = False
        return False

    return True


# Función que muestra el marcador en los sets.
def marcador_sets():
    global nombres_jugadores
    print("\nSets: "+nombres_jugadores[0]+" "+str(set_uno)+" - "+str(set_dos)+" "+nombres_jugadores[1])


# Función que representa la simulación del juego.
def comienza_juego():
    global juegos_uno
    global juegos_dos
    global puntos_uno
    global puntos_dos
    global aleatorio
    global punto
    global game

    # Representa los sets.
    while set_uno != 2 and set_dos != 2:
        juego = True
        marcador_sets()
        juegos_uno, juegos_dos = 0, 0

        # Representa los juegos.
        while juego:
            game = True
            marcador_juegos()
            juego = conteo_juegos()
            cambio_cancha()
            puntos_uno, puntos_dos = 0, 0

            # Representa los puntos para juegos.
            while game:
                try:
                    saque()
                    punto = int(input("¿Para quién será el punto? \nPara jugador uno - 1\nPara jugador dos - 2 \n"))
                    if punto != 1 and punto != 2:
                        raise Exception()
                    game = conteo_puntos(punto)
                    aleatorio += 1
                except ValueError:
                    print("\nERROR: Por favor introducir un número\n")
                except Exception:
                    print("\nError: el número debe ser 1 ó 2\n")

    if set_uno == 2:
        print("\n¡¡¡ "+nombres_jugadores[0]+" es el ganador del juego !!!\n")

    if set_dos == 2:
        print("\n¡¡¡ "+nombres_jugadores[1]+" es el ganador del juego !!!\n")

    print("Marcador final: " + nombres_jugadores[0] + " " + str(set_uno) + " - " + str(set_dos) + " " + nombres_jugadores[1])


# Función principal
if __name__ == "__main__":
    nombres_jugadores = pide_nombres()
    comienza_juego()
