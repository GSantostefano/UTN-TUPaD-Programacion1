# Actividades: 
# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas. 
# 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja.
print("\n=================================================")
print("=== EJERCICIO 1: LISTA DE NOTAS DE ESTUDIANTES ===")

notas_estudiantes = [8.5, 7.2, 9.1, 6.8, 8.9, 7.5, 9.3, 8.0, 7.8, 8.7]

print("\nLista completa de notas:")
for i in range(len(notas_estudiantes)):
    print(f"Estudiante {i+1}: {notas_estudiantes[i]}")

suma_notas = 0
for nota in notas_estudiantes:
    suma_notas += nota

promedio = suma_notas / len(notas_estudiantes)
print(f"\nPromedio de las notas: {promedio:.2f}")

nota_maxima = notas_estudiantes[0]
nota_minima = notas_estudiantes[0]

for nota in notas_estudiantes:
    if nota > nota_maxima:
        nota_maxima = nota
    if nota < nota_minima:
        nota_minima = nota

print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")

print("\n" + "="*50) 


# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.
print("\n=================================================")
print("=== EJERCICIO 2: LISTA DE PRODUCTOS ===")

productos = []

for i in range(5):
    productos.append(input(f"Producto {i+1}: ").strip())
print("\nLista original:")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]}")

print("\nLista ordenada:")
productos_ordenados = sorted(productos)
for i in range(len(productos_ordenados)):
    print(f"{i+1}. {productos_ordenados[i]}")

print("\nProductos para eliminar:")
productos_para_eliminar = sorted(productos)
for i in range(len(productos_para_eliminar)):
    print(f"{i+1}. {productos_para_eliminar[i]}")       

while True:
    indice_eliminar = int(input(f"\nIngrese el número del producto que desea eliminar (1-5): ")) - 1
    
    if indice_eliminar >= 0 and indice_eliminar < 5:
        producto_eliminado = productos_para_eliminar.pop(indice_eliminar)
        print(f"\nProducto '{producto_eliminado}' eliminado exitosamente.")
        break
    else:
        print("Debe elegir un número del 1 al 5.")

print("\nLista final actualizada (ordenada):")
for i in range(len(productos_para_eliminar)):
    print(f"{i+1}. {productos_para_eliminar[i]}")


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista.
print("\n=================================================")
print("\n=== EJERCICIO 3: NÚMEROS ALEATORIOS PARES E IMPARES ===")

import random

numeros_aleatorios = []
for i in range(15):
    numero = random.randint(1, 100)
    numeros_aleatorios.append(numero)

print("\nLista de números aleatorios:")
for i in range(len(numeros_aleatorios)):
    print(f"{i+1}. {numeros_aleatorios[i]}")

numeros_pares = []
numeros_impares = []

for numero in numeros_aleatorios:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("\nNúmeros pares:")
for i in range(len(numeros_pares)):
    print(f"{i+1}. {numeros_pares[i]}")

print("\nNúmeros impares:")
for i in range(len(numeros_impares)):
    print(f"{i+1}. {numeros_impares[i]}")

print(f"\nCantidad de números pares: {len(numeros_pares)}")
print(f"Cantidad de números impares: {len(numeros_impares)}")



# 4) Dada una lista con valores repetidos: 
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado.
print("\n=================================================")
print("\n=== EJERCICIO 4: ELIMINAR ELEMENTOS REPETIDOS ===")


lista_con_repetidos = [1, 2, 3, 6, 4, 1, 6, 3, 6, 2, 7, 1, 8, 4, 9]


print("\nLista original con repetidos:")
for i in range(len(lista_con_repetidos)):
    print(f"{i+1}. {lista_con_repetidos[i]}")

lista_sin_repetidos = []

for elemento in lista_con_repetidos:
    if elemento not in lista_sin_repetidos:
        lista_sin_repetidos.append(elemento)

print("\nLista sin elementos repetidos:")
for i in range(len(lista_sin_repetidos)):
    print(f"{i+1}. {lista_sin_repetidos[i]}")

print(f"\nCantidad original: {len(lista_con_repetidos)} elementos")
print(f"Cantidad sin repetidos: {len(lista_sin_repetidos)} elementos")

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada.
print("\n=================================================")
print("\n=== EJERCICIO 5: GESTIÓN DE ESTUDIANTES ===")

estudiantes = ["Gabriel", "Carlos", "Ana", "Pedro", "Claudio", "Juan", "Julieta", "Diego"]

print("\nLista inicial de estudiantes:")
for i in range(len(estudiantes)):
    print(f"{i+1}. {estudiantes[i]}")

print("\n¿Qué desea hacer?")
print("1. Agregar un nuevo estudiante")
print("2. Eliminar un estudiante existente")

opcion = int(input("Ingrese su opción (1 o 2): "))

if opcion == 1:
    
    nuevo_estudiante = input("\nIngrese el nombre del nuevo estudiante: ").strip()
    estudiantes.append(nuevo_estudiante)
    print(f"Estudiante '{nuevo_estudiante}' agregado exitosamente.")
    
elif opcion == 2:
    
    print("\nEstudiantes disponibles para eliminar:")
    for i in range(len(estudiantes)):
        print(f"{i+1}. {estudiantes[i]}")
    
    indice_eliminar = int(input(f"\nIngrese el número del estudiante a eliminar (1-{len(estudiantes)}): ")) - 1
    
    if indice_eliminar >= 0 and indice_eliminar < len(estudiantes):
        estudiante_eliminado = estudiantes.pop(indice_eliminar)
        print(f"Estudiante '{estudiante_eliminado}' eliminado exitosamente.")
    else:
        print("Número inválido. No se eliminó ningún estudiante.")

print("\nLista final actualizada:")
for i in range(len(estudiantes)):
    print(f"{i+1}. {estudiantes[i]}")

print(f"\nTotal de estudiantes: {len(estudiantes)}")



# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero).

print("\n=================================================")
print("=== EJERCICIO 6: ROTACIÓN DE ELEMENTOS ===")

numeros = [1, 2, 3, 4, 5, 6, 7]

print("\nLista original:")
for i in range(len(numeros)):
    print(f"{i+1}. {numeros[i]}")

ultimo_elemento = numeros[-1] 

for i in range(len(numeros) - 1, 0, -1):
    numeros[i] = numeros[i-1]

numeros[0] = ultimo_elemento

print("\nLista rotada hacia la derecha:")
for i in range(len(numeros)):
    print(f"{i+1}. {numeros[i]}")

print("\n=================================================") 


# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica.

print("\n=================================================")
print("=== EJERCICIO 7: TEMPERATURAS DE LA SEMANA ===")

temperaturas = [
    [15, 25],  #Día [min, max]
    [12, 22], 
    [18, 28],  
    [14, 24], 
    [16, 26],  
    [20, 30], 
    [17, 27]  
]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("\nTemperaturas de la semana:")
print("Día\t\tMínima\tMáxima\tAmplitud")
for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    print(f"{dias_semana[i]}\t\t{temperaturas[i][0]}°C\t{temperaturas[i][1]}°C\t{amplitud}°C")

suma_minimas = 0
for i in range(len(temperaturas)):
    suma_minimas += temperaturas[i][0]
promedio_minimas = suma_minimas / len(temperaturas)

suma_maximas = 0
for i in range(len(temperaturas)):
    suma_maximas += temperaturas[i][1]
promedio_maximas = suma_maximas / len(temperaturas)

print(f"\nPromedio de temperaturas mínimas: {promedio_minimas:.1f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maximas:.1f}°C")

mayor_amplitud = 0
dia_mayor_amplitud = 0

for i in range(len(temperaturas)):
    amplitud = temperaturas[i][1] - temperaturas[i][0]
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i

print(f"\nMayor amplitud térmica: {mayor_amplitud}°C")
print(f"Día con mayor amplitud: {dias_semana[dia_mayor_amplitud]}")

print("\n=================================================") 


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia.

print("\n=================================================")
print("=== EJERCICIO 8: MATRIZ DE NOTAS DE ESTUDIANTES ===")

notas_estudiantes = [
    [8, 7, 9], #Estudiante [Matemática, Física, Química]
    [6, 8, 7], 
    [9, 9, 8],
    [7, 6, 9],
    [8, 8, 7]
]

nombres_estudiantes = ["Gabriel", "Carlos", "Ana", "Pedro", "Claudio"]
nombres_materias = ["Matemática", "Física", "Química"]

print("\nMatriz de notas:")
print("Estudiante\tMatemática\tFísica\t\tQuímica")
for i in range(len(notas_estudiantes)):
    print(f"{nombres_estudiantes[i]}\t\t{notas_estudiantes[i][0]}\t\t{notas_estudiantes[i][1]}\t\t{notas_estudiantes[i][2]}")

print("\nPromedio de cada estudiante:")
for i in range(len(notas_estudiantes)):
    suma_notas = 0
    for j in range(len(notas_estudiantes[i])):
        suma_notas += notas_estudiantes[i][j]
    promedio = suma_notas / len(notas_estudiantes[i])
    print(f"{nombres_estudiantes[i]}: {promedio:.2f}")

print("\nPromedio de cada materia:")
for j in range(len(notas_estudiantes[0])):
    suma_materia = 0
    for i in range(len(notas_estudiantes)):
        suma_materia += notas_estudiantes[i][j]
    promedio_materia = suma_materia / len(notas_estudiantes)
    print(f"{nombres_materias[j]}: {promedio_materia:.2f}")

print("\n=================================================") 


# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada.

print("\n=================================================")
print("=== EJERCICIO 9: JUEGO TA-TE-TI ===")

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def mostrar_tablero():
    print("\nTablero actual:")
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            print(tablero[i][j], end=" ")
        print()

mostrar_tablero()

jugador_actual = "X"

for jugada in range(9):  
    print(f"\nTurno del jugador {jugador_actual}")

    fila = int(input("Ingrese fila (0, 1, 2): "))
    columna = int(input("Ingrese columna (0, 1, 2): "))
    
    if tablero[fila][columna] == "-":

        tablero[fila][columna] = jugador_actual

        mostrar_tablero()
        
        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"
    else:
        print("Esa casilla ya está ocupada. Intente otra posición.")

print("\n¡Juego terminado!")

print("\n=================================================") 


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana.

print("\n=================================================")
print("=== EJERCICIO 10: VENTAS DE LA TIENDA ===")

ventas = [
    [10, 15, 12, 18, 20, 14, 16],  # Producto
    [8, 12, 10, 15, 18, 11, 13],   
    [5, 8, 6, 10, 12, 7, 9],      
    [12, 18, 15, 22, 25, 16, 20] 
]

nombres_productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("\nVentas de la semana:")
print("Producto\tLunes\tMartes\tMiérc.\tJueves\tViernes\tSábado\tDomingo")
for i in range(len(ventas)):
    print(f"{nombres_productos[i]}\t\t", end="")
    for j in range(len(ventas[i])):
        print(f"{ventas[i][j]}\t", end="")
    print()

print("\nTotal vendido por cada producto:")
for i in range(len(ventas)):
    total_producto = 0
    for j in range(len(ventas[i])):
        total_producto += ventas[i][j]
    print(f"{nombres_productos[i]}: {total_producto} unidades")

print("\nVentas totales por día:")
mayor_ventas_dia = 0
dia_mayor_ventas = 0

for j in range(len(ventas[0])):
    total_dia = 0
    for i in range(len(ventas)):
        total_dia += ventas[i][j]
    print(f"{dias_semana[j]}: {total_dia} unidades")
    
    if total_dia > mayor_ventas_dia:
        mayor_ventas_dia = total_dia
        dia_mayor_ventas = j

print(f"\nDía con mayores ventas totales: {dias_semana[dia_mayor_ventas]} ({mayor_ventas_dia} unidades)")

print("\nProducto más vendido en la semana:")
mayor_ventas_producto = 0
producto_mas_vendido = 0

for i in range(len(ventas)):
    total_producto = 0
    for j in range(len(ventas[i])):
        total_producto += ventas[i][j]
    
    if total_producto > mayor_ventas_producto:
        mayor_ventas_producto = total_producto
        producto_mas_vendido = i

print(f"{nombres_productos[producto_mas_vendido]}: {mayor_ventas_producto} unidades")

print("\n=================================================")