import random
from types import NoneType
LARGO_MATRIZ = 4
NUMERO_GANADOR = 2048
NUMERO_RANDOM = 2
CASILLERO_VACIO = " "
POSICION_IZQUIERDA = "a"
POSICION_DERECHA = "d"
POSICION_ARRIBA = "w"
POSICION_ABAJO = "s"



def inicializar_juego():
	#Crea una matriz, que en este caso es 4x4
	matriz=[]
	for i in range(LARGO_MATRIZ):
		matriz.append([CASILLERO_VACIO] * LARGO_MATRIZ)
	
	# Busco una fila random y una columna random para agregar un 2
	matriz = insertar_nuevo_random(matriz)
	return matriz



def insertar_nuevo_random(matriz):
    #agrega un 2 en alguna posición random que este vacia
    nueva_matriz = matriz[:]
    fila_random = random.randint(0,LARGO_MATRIZ - 1)
    col_random = random.randint(0,LARGO_MATRIZ - 1)
    while nueva_matriz[fila_random][col_random] != " ":
        fila_random = random.randint(0,LARGO_MATRIZ - 1)
        col_random = random.randint(0,LARGO_MATRIZ - 1)

    nueva_matriz[fila_random][col_random] = NUMERO_RANDOM
    return nueva_matriz
    


def mostrar_juego(matriz):
	#imprime el juego
	for i in range(LARGO_MATRIZ):
		for j in range(LARGO_MATRIZ):
			print(matriz[i][j], end = "  |   ")
			
		print("\n----------------------------")
	return matriz



def juego_ganado(matriz):
	#Si algun casillero tiene un numero que es 2048, se gana el juego
    for  i in range(LARGO_MATRIZ):
        for j in range(LARGO_MATRIZ):
            if matriz[i][j] == NUMERO_GANADOR:
                return True
            else:
                continue
    return False



def juego_perdido(matriz):
    #Si todos los casilleros tienen un numero entonces el juego se pierde
	for i in range(LARGO_MATRIZ):
		for j in range(LARGO_MATRIZ):
			if matriz[i][j] == CASILLERO_VACIO:
				return False

	return True
		


def ingreso_posicion():
	return input("""ingrese una dirección para moverse 
w: Mover hacia arriba
s: Mover hacia abajo
a: Mover hacia la izquierda
d: Mover hacia la derecha:  """)

def pedir_direccion(dir):
    #Pide una dirección hasta que se ingrese una dirección valida.
	dir = ingreso_posicion()
	while dir not in "aAwWsSdD" or dir == "" :
		print(dir, "No es un valor valido")
		dir = ingreso_posicion()

	return dir




def juntar_numeros(matriz):
    #Junta los numeros y agrega casilleros vacios cuando se mueve un numero
    matriz_nueva = []

    for i in range(LARGO_MATRIZ):
        matriz_nueva.append([CASILLERO_VACIO] * LARGO_MATRIZ)
        n = 0

        for j in range(LARGO_MATRIZ):
            if matriz[i][j] != CASILLERO_VACIO:                
                matriz_nueva[i][n] = matriz[i][j]
                n += 1

    return matriz_nueva

    
def sumar(matriz):
    #Multiplica por 2 el valor que haya en el casillero, si es que hay dos numeros iguales consecutivos. Dependiendo el movimiento que se haga
    for i in range(LARGO_MATRIZ):
        for j in range(LARGO_MATRIZ - 1):
            if matriz[i][j] == matriz[i][j + 1] and matriz[i][j] != CASILLERO_VACIO :
                matriz[i][j] = matriz[i][j] * 2
                matriz[i][j + 1] = CASILLERO_VACIO

    return matriz

def espejar(matriz):
    #Espeja la matriz, todo lo que esta a la izquierda lo pone en la derecha
    matriz_nueva =[]
    for i in range(LARGO_MATRIZ):
        matriz_nueva.append([])

        for j in range(LARGO_MATRIZ):
            matriz_nueva[i].append(matriz[i][3 - j])

    return matriz_nueva



def transpuesta(matriz):
    #Hace la matriz traspuesta
    matriz_nueva = []
    for i in range(LARGO_MATRIZ):
        matriz_nueva.append([])

        for j in range(LARGO_MATRIZ):
            matriz_nueva[i].append(matriz[j][i])

    return matriz_nueva



def mover_izquierda(matriz):
    #Movimiento hacia la izquierda cuando se presiona "a"

    matriz_nueva = juntar_numeros(matriz)
    matriz_nueva = sumar(matriz_nueva)
    matriz_nueva = juntar_numeros(matriz_nueva)
    return matriz_nueva


def mover_derecha(matriz):
    #Movimiento hacia la derecha cuando se presiona "d"

    matriz_nueva = espejar(matriz)
    matriz_nueva = mover_izquierda(matriz_nueva)
    matriz_nueva = espejar(matriz_nueva)
    return matriz_nueva


def mover_arriba(matriz):
    #Movimiento hacia arriba cuando se presiona "w"

    matriz_nueva = transpuesta(matriz)
    matriz_nueva = mover_izquierda(matriz_nueva)
    matriz_nueva = transpuesta(matriz_nueva)
    return matriz_nueva


def mover_abajo(matriz):
    #Movimiento hacia abajo cuando se presiona "s"
    matriz_nueva = transpuesta(matriz)
    matriz_nueva = mover_derecha(matriz_nueva)
    matriz_nueva = transpuesta(matriz_nueva)
    return matriz_nueva 
 

def actualizar_juego(matriz, dir):
    if dir == POSICION_ARRIBA:
        nueva_matriz = mover_arriba(matriz)
        return nueva_matriz

    elif dir == POSICION_ABAJO:
        nueva_matriz = mover_abajo(matriz)
        return nueva_matriz

    elif dir == POSICION_IZQUIERDA:
        nueva_matriz = mover_izquierda(matriz)
        return nueva_matriz

    elif dir == POSICION_DERECHA:
         nueva_matriz = mover_derecha(matriz)
         return nueva_matriz

