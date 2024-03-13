import random


# ---- 1 Area de funciones -----
def imprimirTablero(tablero):
    print('Juego TA-TE-TI')
    for fila in tablero:
        print(fila[0], fila[1], fila[2])


def tableroLleno(tablero):
    casillasOcupadas = 0
    for i in range(3):
        for j in range(3):
            if (tablero[i][j] == 'X' or tablero[i][j] == 'O'):
                casillasOcupadas += 1
    if casillasOcupadas == 9:
        return True
    else:
        return False

def verificaGanador(tablero):
    empate = True
    terminar = False
    ganador = ""
    # Paso 6 Verificar si gano el usuario
    if ((tablero[0][0] == simbolo_usuario and tablero[0][1] == simbolo_usuario and tablero[0][
        2] == simbolo_usuario) or  # Horizontal top
            (tablero[1][0] == simbolo_usuario and tablero[1][1] == simbolo_usuario and tablero[1][
                2] == simbolo_usuario) or  # Horizontal mid
            (tablero[2][0] == simbolo_usuario and tablero[2][1] == simbolo_usuario and tablero[2][
                2] == simbolo_usuario) or  # Horizontal bot
            (tablero[0][0] == simbolo_usuario and tablero[1][0] == simbolo_usuario and tablero[2][
                0] == simbolo_usuario) or  # Vertical top
            (tablero[0][1] == simbolo_usuario and tablero[1][1] == simbolo_usuario and tablero[2][
                1] == simbolo_usuario) or  # Vertical mid
            (tablero[0][2] == simbolo_usuario and tablero[1][2] == simbolo_usuario and tablero[2][
                2] == simbolo_usuario) or  # Vertical bot
            (tablero[0][0] == simbolo_usuario and tablero[1][1] == simbolo_usuario and tablero[2][
                2] == simbolo_usuario) or  # Diagonal invertida
            (tablero[0][2] == simbolo_usuario and tablero[1][1] == simbolo_usuario and tablero[2][
                0] == simbolo_usuario)):  # Diagonal normal
        ganador = "¡Tu ganaste!"
        empate = False
        terminar = True

    # Paso 7 Verificar si gano la PC
    if ((tablero[0][0] == simbolo_PC and tablero[0][1] == simbolo_PC and tablero[0][
        2] == simbolo_PC) or  # Horizontal top
            (tablero[1][0] == simbolo_PC and tablero[1][1] == simbolo_PC and tablero[1][
                2] == simbolo_PC) or  # Horizontal mid
            (tablero[2][0] == simbolo_PC and tablero[2][1] == simbolo_PC and tablero[2][
                2] == simbolo_PC) or  # Horizontal bot
            (tablero[0][0] == simbolo_PC and tablero[1][0] == simbolo_PC and tablero[2][
                0] == simbolo_PC) or  # Vertical top
            (tablero[0][1] == simbolo_PC and tablero[1][1] == simbolo_PC and tablero[2][
                1] == simbolo_PC) or  # Vertical mid
            (tablero[0][2] == simbolo_PC and tablero[1][2] == simbolo_PC and tablero[2][
                2] == simbolo_PC) or  # Vertical bot
            (tablero[0][0] == simbolo_PC and tablero[1][1] == simbolo_PC and tablero[2][
                2] == simbolo_PC) or  # Diagonal inversa
            (tablero[0][2] == simbolo_PC and tablero[1][1] == simbolo_PC and tablero[2][
                0] == simbolo_PC)):  # Diagonal normal
        ganador = "¡La computadora gana!"
        empate = False
        terminar = True

    # Paso 8 Verificar si fue empate
    if empate == True and tableroLleno(tablero) == True:
        ganador = "No hubo ganador. Fue empate"
        terminar = True

    return ganador, empate, terminar


# --- 2 Programa Principal -----
# Definimos el tablero como una lista de listas (3 listas de 3 elementos cada una)
# Paso 1 Generar el tablero
respuesta = 'si'
while respuesta == 'si':
    tablero = [['-', '-', '-'],
               ['-', '-', '-'],
               ['-', '-', '-']]

    # Paso 2 Elegir el simbolo a utilizar X u O
    simbolo_usuario = input('¿Que simbolo quieres usar? Elige X u O: ')
    if simbolo_usuario == 'X':
        simbolo_PC = 'O'
    elif simbolo_usuario == 'O':
        simbolo_PC = 'X'
    else:
        simbolo_usuario = 'O'
        simbolo_PC = 'X'
        print('Simbolo inválido, tu simbolo sera O y el de la PC será X')
    print('Simbolo usuario : ', simbolo_usuario)
    print('Simbolo PC: ', simbolo_PC)
    imprimirTablero(tablero)

    if simbolo_usuario == "O":
        terminar = False
        while terminar == False:
            # Paso 3 jugada del usuario
            fil_usuario = int(input('Indica la fila que quieres ocupar(1-3) '))
            col_usuario = int(input('Indica la columna que quieres ocupar(1-3) '))
            if tablero[fil_usuario - 1][col_usuario - 1] == '-':
                tablero[fil_usuario - 1][col_usuario - 1] = simbolo_usuario
            else:
                while tablero[fil_usuario - 1][col_usuario - 1] != '-':
                    print('La posicion esta ocupada, vuelve a intentarlo')
                    fil_usuario = int(input('Indica la fila que quieres ocupar(1-3'))
                    col_usuario = int(input('Indica la fila que quieres ocupar(1-3'))
                tablero[fil_usuario - 1][col_usuario - 1] = simbolo_usuario

            imprimirTablero(tablero)
            ganador, empate, terminar = verificaGanador(tablero)

            if terminar == False:
                # Paso 4 jugada de la computadora
                fil_PC = random.randint(1, 3)
                col_PC = random.randint(1, 3)
                if tablero[fil_PC - 1][col_PC - 1] == '-':
                    tablero[fil_PC - 1][col_PC - 1] = simbolo_PC
                else:
                    while tablero[fil_PC - 1][col_PC - 1] != '-':
                        fil_PC = random.randint(1, 3)
                        col_PC = random.randint(1, 3)
                    tablero[fil_PC - 1][col_PC - 1] = simbolo_PC
                print('La jugada de la PC fue: ', fil_PC, '-', col_PC)

                # Paso 5 Reimprimir el tablero
                imprimirTablero(tablero)
                ganador, empate, terminar = verificaGanador(tablero)

    else:
        terminar = False
        while terminar == False:
            # Paso 4 jugada de la computadora
            fil_PC = random.randint(1, 3)
            col_PC = random.randint(1, 3)
            if tablero[fil_PC - 1][col_PC - 1] == '-':
                tablero[fil_PC - 1][col_PC - 1] = simbolo_PC
            else:
                while tablero[fil_PC - 1][col_PC - 1] != '-':
                    fil_PC = random.randint(1, 3)
                    col_PC = random.randint(1, 3)
                tablero[fil_PC - 1][col_PC - 1] = simbolo_PC
            print('La jugada de la PC fue: ', fil_PC, '-', col_PC)

            imprimirTablero(tablero)
            ganador, empate, terminar = verificaGanador(tablero)

            if terminar == False:
                # Paso 3 jugada del usuario
                fil_usuario = int(input('Indica la fila que quieres ocupar(1-3) '))
                col_usuario = int(input('Indica la columna que quieres ocupar(1-3) '))
                if tablero[fil_usuario - 1][col_usuario - 1] == '-':
                    tablero[fil_usuario - 1][col_usuario - 1] = simbolo_usuario
                else:
                    while tablero[fil_usuario - 1][col_usuario - 1] != '-':
                        print('La posicion esta ocupada, vuelve a intentarlo')
                        fil_usuario = int(input('Indica la fila que quieres ocupar(1-3'))
                        col_usuario = int(input('Indica la fila que quieres ocupar(1-3'))
                    tablero[fil_usuario - 1][col_usuario - 1] = simbolo_usuario

                # Paso 5 Reimprimir el tablero
                imprimirTablero(tablero)
                ganador, empate, terminar = verificaGanador(tablero)

    print(ganador)
    respuesta = input('¿Deseas jugar de nuevo? (si/no): ')
print('¡Gracias por jugar!')
