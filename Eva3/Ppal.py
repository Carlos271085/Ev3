import funciones as f

jugadores = []
jugador = {}

opc = 0

while opc != 4:

    opc = f.menu()

    if opc == 1:
        f.registrarPuntaje()
    
    elif opc == 2:
        f.listarPuntaje()

    elif opc == 3:
        f.imprimirTipo()

    else:
        print('Salir del Programa!!!')
