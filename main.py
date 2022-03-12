import logica

def main():
    juego = logica.inicializar_juego()
    while True:
        logica.mostrar_juego(juego)
        if logica.juego_ganado(juego):
            print("Congratulation! you win")
            return
        if logica.juego_perdido(juego):
            print("oops, try again!")
            return
        dir = logica.pedir_direccion(juego)
        nuevo_juego = logica.actualizar_juego(juego, dir)
        if nuevo_juego != juego:
            juego = logica.insertar_nuevo_random(nuevo_juego) 
            print(juego)

main()


