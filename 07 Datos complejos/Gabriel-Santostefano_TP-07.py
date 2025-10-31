""" 1) Dado el diccionario precios_frutas 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
Añadir las siguientes frutas con sus respectivos precios: 
● Naranja = 1200 
● Manzana = 1500 
● Pera = 2300 """

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario después de añadir frutas:")
print(precios_frutas)

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
● Banana = 1330 
● Manzana = 1700 
● Melón = 2800  """

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\nDiccionario después de actualizar precios:")
print(precios_frutas)


""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
precios. """

frutas_sin_precios = list(precios_frutas.keys())

print("\nLista de frutas sin precios:")
print(frutas_sin_precios)

""" 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
• Luego, pedí un nombre y mostrale el número asociado, si existe. """

contactos = {}

print(" CARGA DE CONTACTOS ")

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero

print("\n CONSULTA DE CONTACTOS ")

while True:
    nombre_consulta = input("\nIngrese un nombre para consultar (o 'salir' para terminar): ")
    
    if nombre_consulta.lower() == 'salir':
        break
    
    if nombre_consulta in contactos:
        print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
    else:
        print(f"El contacto '{nombre_consulta}' no existe en la agenda.")

print("Fin")

""" 
5) Solicita al usuario una frase e imprime: 
• Las palabras únicas (usando un set). 
• Un diccionario con la cantidad de veces que aparece cada palabra. """


frase = input("Ingrese una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)
print("\nPalabras_únicas:")
print(palabras_unicas)

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("\nRecuento:")
print(recuento)

""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
Luego, mostrá el promedio de cada alumno. """

alumnos = {}

print(" INGRESO DE ALUMNOS Y NOTAS ")
for i in range(3):
    nombre = input(f"\nIngrese el nombre del alumno {i+1}: ")
    
    print(f"Ingrese las 3 notas de {nombre}:")
    notas = []
    for j in range(3):
        nota = float(input(f"Nota {j+1}: "))
        notas.append(nota)
    
    alumnos[nombre] = tuple(notas)

print("\n PROMEDIOS ")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: Notas {notas} - Promedio: {promedio:.2f}")


""" 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
y Parcial 2: 
• Mostrá los que aprobaron ambos parciales. 
• Mostrá los que aprobaron solo uno de los dos. 
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). """

aprobados_parcial1 = {"Juan", "María", "Carlos", "Ana", "Luis"}
aprobados_parcial2 = {"María", "Pedro", "Ana", "Sofía", "Carlos"}

print("Estudiantes que aprobaron Parcial 1:", aprobados_parcial1)
print("Estudiantes que aprobaron Parcial 2:", aprobados_parcial2)

ambos_parciales = aprobados_parcial1 & aprobados_parcial2
print("\na) Aprobaron ambos parciales:", ambos_parciales)

solo_parcial1 = aprobados_parcial1 - aprobados_parcial2
solo_parcial2 = aprobados_parcial2 - aprobados_parcial1
solo_un_parcial = solo_parcial1 | solo_parcial2
print("b) Aprobaron solo un parcial:", solo_un_parcial)

al_menos_uno = aprobados_parcial1 | aprobados_parcial2
print("c) Aprobaron al menos un parcial:", al_menos_uno)

""" 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
Permití al usuario: 
• Consultar el stock de un producto ingresado. 
• Agregar unidades al stock si el producto ya existe. 
• Agregar un nuevo producto si no existe.  """

inventario = {
    "Manzanas": 50,
    "Bananas": 30,
    "Naranjas": 25,
    "Leche": 15
}

print(" SISTEMA DE GESTIÓN DE STOCK ")

while True:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a producto existente")
    print("3. Agregar nuevo producto")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        if producto in inventario:
            print(f"Stock de {producto}: {inventario[producto]} unidades")
        else:
            print(f"El producto '{producto}' no existe en el inventario")
    
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        if producto in inventario:
            try:
                unidades = int(input("Ingrese las unidades a agregar: "))
                inventario[producto] += unidades
                print(f"Stock actualizado: {producto} = {inventario[producto]} unidades")
            except ValueError:
                print("Error: Debe ingresar un número válido")
        else:
            print(f"El producto '{producto}' no existe. Use la opción 3 para agregarlo.")
    
    elif opcion == "3":
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in inventario:
            try:
                stock_inicial = int(input("Ingrese el stock inicial: "))
                inventario[producto] = stock_inicial
                print(f"Producto '{producto}' agregado con {stock_inicial} unidades")
            except ValueError:
                print("Error: Debe ingresar un número válido")
        else:
            print(f"El producto '{producto}' ya existe. Use la opción 2 para modificar su stock.")
    
    elif opcion == "4":
        print("Inventario final:")
        for producto, stock in inventario.items():
            print(f"- {producto}: {stock} unidades")
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione 1-4.")


""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. """

agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "15:00"): "Clase de inglés",
}

print(" CONSULTA ESPECÍFICA ")
dia_consulta = input("Ingrese el día: ")
hora_consulta = input("Ingrese la hora (HH:MM): ")

clave_consulta = (dia_consulta.capitalize(), hora_consulta)

if clave_consulta in agenda:
    print(f"Actividad: {agenda[clave_consulta]}")
else:
    print("No hay actividades programadas para ese día y hora")

print("\n--- AGENDA COMPLETA ---")
for (dia, hora), evento in agenda.items():
    print(f"{dia} {hora}: {evento}")


""" 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
diccionario donde: 
• Las capitales sean las claves. 
• Los países sean los valores. """

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago"
}

print("Diccionario original:")
print(paises_capitales)

capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("\nDiccionario invertido:")
print(capitales_paises)
