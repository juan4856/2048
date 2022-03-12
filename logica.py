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
	""""Initialize the game, in this case a matrix 4x4"""
	matriz=[]
	for i in range(LARGO_MATRIZ):
		matriz.append([CASILLERO_VACIO] * LARGO_MATRIZ)
	
	# insert a 2 in an empty space
	matriz = insertar_nuevo_random(matriz)
	return matriz



def insertar_nuevo_random(matriz):
    """Search and empty place and insert a 2"""
    nueva_matriz = matriz[:]
    fila_random = random.randint(0,LARGO_MATRIZ - 1)
    col_random = random.randint(0,LARGO_MATRIZ - 1)
    while nueva_matriz[fila_random][col_random] != " ":
        fila_random = random.randint(0,LARGO_MATRIZ - 1)
        col_random = random.randint(0,LARGO_MATRIZ - 1)

    nueva_matriz[fila_random][col_random] = NUMERO_RANDOM
    return nueva_matriz
    


def mostrar_juego(matriz):
	"""Print the game in the"""
	for i in range(LARGO_MATRIZ):
		for j in range(LARGO_MATRIZ):
			print(matriz[i][j], end = "  |   ")
			
		print("\n----------------------------")
	return matriz



def juego_ganado(matriz):
    """If any place has a 2048, the game finish"""
    for  i in range(LARGO_MATRIZ):
        for j in range(LARGO_MATRIZ):
            if matriz[i][j] == NUMERO_GANADOR:
                return True
            else:
                continue
    return False



def juego_perdido(matriz):
    """If there is no empty place, the game is lost"""
    for i in range(LARGO_MATRIZ):
        for j in range(LARGO_MATRIZ):
            if matriz[i][j] == CASILLERO_VACIO:
                return False
    return True
		


def ingreso_posicion():
    """User insert a direction"""

    return input("""ingrese una dirección para moverse 
w: Mover hacia arriba
s: Mover hacia abajo
a: Mover hacia la izquierda
d: Mover hacia la derecha:  """)

def pedir_direccion(dir):
	dir = ingreso_posicion()
	while dir not in "aAwWsSdD" or dir == "" :
		print(dir, "No es un valor valido")
		dir = ingreso_posicion()

	return dir




def juntar_numeros(matriz):
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
    """Does the sum of the numbers when necessary"""
    for i in range(LARGO_MATRIZ):
        for j in range(LARGO_MATRIZ - 1):
            if matriz[i][j] == matriz[i][j + 1] and matriz[i][j] != CASILLERO_VACIO :
                matriz[i][j] = matriz[i][j] * 2
                matriz[i][j + 1] = CASILLERO_VACIO

    return matriz

def espejar(matriz):
    """Mirror the matrix, everything is at left goes to the right"""
    matriz_nueva =[]
    for i in range(LARGO_MATRIZ):
        matriz_nueva.append([])

        for j in range(LARGO_MATRIZ):
            matriz_nueva[i].append(matriz[i][3 - j])

    return matriz_nueva



def transpuesta(matriz):
    """Transposes the matrix"""
    matriz_nueva = []
    for i in range(LARGO_MATRIZ):
        matriz_nueva.append([])

        for j in range(LARGO_MATRIZ):
            matriz_nueva[i].append(matriz[j][i])

    return matriz_nueva



def mover_izquierda(matriz):
    """Movement when the users press 'a'"""

    matriz_nueva = juntar_numeros(matriz)
    matriz_nueva = sumar(matriz_nueva)
    matriz_nueva = juntar_numeros(matriz_nueva)
    return matriz_nueva


def mover_derecha(matriz):
    """Movement when the users press 'd'"""

    matriz_nueva = espejar(matriz)
    matriz_nueva = mover_izquierda(matriz_nueva)
    matriz_nueva = espejar(matriz_nueva)
    return matriz_nueva


def mover_arriba(matriz):
    """Movement when the users press 'w'"""

    matriz_nueva = transpuesta(matriz)
    matriz_nueva = mover_izquierda(matriz_nueva)
    matriz_nueva = transpuesta(matriz_nueva)
    return matriz_nueva


def mover_abajo(matriz):
    """Movement when the users press 's'"""
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

