jugadores = []
def menu():
    while True:
        print('************Bienvenido a eSport (eShirlitos)**********')
        print('==========Menù==========')
        print('1. Registrar puntajes torneo')
        print('2. Listar los todos puntajes')
        print('3. Imprimir por Tipo')
        print('4. Salir del programa')
        print('-'*30)

        while True:
            try:
                opc = int(input('Ingrese Opciòn: '))
                if 1 <= opc <= 4:
                    break
                else:
                    print('Opciòn ingresada NO es Vàlida!!!')
                    print('-'*30)
            except:
                print('Opciòn es un nùmero!!!')
                print('-'*30)
        return opc
    

def registrarPuntaje():
    idJugador = input('Ingrese ID del Jugador: ').lower()
    nombreApellido = input('Ingrese Nombre y Apellido del Jugador: ').lower()
    valorant = int(input('Ingrese Puntaje Valorant: '))
    fortnite = int(input('Ingrese Puntaje Fortnite: '))
    fifa = int(input('Ingrese Puntaje Fifa: '))
    tipo = input('Ingrese el tipo: ( Principiante - Avanzado - Experto ): ')

    jugador = {
        'idJugador': idJugador,
        'nombreApellido': nombreApellido,
        'valorant': valorant,
        'fortnite': fortnite,
        'fifa': fifa,
        'tipo': tipo
    }

    jugadores.append(jugador)
    print('Los Datos Ingresados quedaron guardados correctamente!!!')
    print('-'*30)

def listarPuntaje():
    print('ID \tNombreApellido \tValorant \tFortnite \tFifa \tTipo \n. ')
    for jugador in jugadores:
        print(f'{jugador['idJugador']} \t{jugador['nombreApellido']} \t{jugador['valorant']} \t{jugador['fortnite']} \t{jugador['fifa']} \t{jugador['tipo']} \n. ')
        print('-'*30)

def imprimirTipo():
    tipo = input('Ingrese el tipo: ( Principiante - Avanzado - Experto ): ')
    jugadorGuardado = [jugador for jugador in jugadores if jugador ['tipo'] == tipo]
    if not jugadorGuardado:
        print('La busqueda de tipo {tipo}, no fue encontrada!!!')
        print('-'*30)

    nombreArchivo = f'{tipo}.txt'
    with open(nombreArchivo, 'w')as archivo:
        archivo.write('ID \tNombreApellido \tValorant \tFortnite \tFifa \tTipo \n. ')
        for jugador in jugadores:
            archivo.write(f'{jugador['idJugador']} \t{jugador['nombreApellido']} \t{jugador['valorant']} \t{jugador['fortnite']} \t{jugador['fifa']} \t{jugador['tipo']} \n. ')
    print(f'Los puntajes de los jugadores guardados de tipo {tipo}, fueron almacenados en archivos{nombreArchivo}')
    print('-'*30)

 