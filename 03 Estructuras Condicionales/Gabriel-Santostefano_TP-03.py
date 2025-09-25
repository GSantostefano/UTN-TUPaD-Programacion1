#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

edad = int(input("Ingrese edad: "))
if edad >=18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#mensaje “Desaprobado”. 

nota = float(input("Ingrese nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar.


numero = int(input("Ingrese numero par"))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese edad: "))
if edad <12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#  5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#  (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#  pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#  pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#  de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#  como una lista o un string. 

contraseña = input("Ingrese contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#  6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
#  y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
#  siguiente: ...............

import random
from statistics import mode,  median, mean


numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo o a la derecha"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo o a la izquierda"
else:
    sesgo = "Sin sesgo"

print("Lista de numeros aleatorios:", numeros_aleatorios)
print("Moda: ",moda)
print("Mediana: ", mediana)
print("Media: ", media)
print("Resultado: ", sesgo)


#  7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#  termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#  pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#  pantalla. 
frase = input("Ingrese frase o palabra: ")

if frase and frase[-1].lower() in 'aeiouáéíóú':
    frase = frase + '!'
    print(frase)
else:
    print(frase)


#  8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#  dependiendo de la opción que desee: 
#  1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#  2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#  3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#  El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#  usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#  lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")

print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. ")

opcion = input("el número 1, 2 o 3 dependiendo de la opción que desee: ")

if opcion == "1":
    print("El resultado: ",nombre.upper())
elif opcion == "2":
    print("El resultado: ",nombre.lower())
elif opcion == "3":
    print("El resultado: ",nombre.title())
else: 
    print("\nError!! Ingrese número 1, 2 o 3")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud_terremoto =float(input("Ingrese la magnitud de un terremoto según la escala de Richter: "))

if magnitud_terremoto <3:
    print("Muy leve (imperceptible)")
elif magnitud_terremoto >=3 and magnitud_terremoto <4:
    print("Leve (ligeramente perceptible).")
elif magnitud_terremoto >=4 and magnitud_terremoto <5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud_terremoto >=5 and magnitud_terremoto <6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud_terremoto >=6 and magnitud_terremoto <7:
    print("Muy Fuerte (puede causar daños significativos). ")
elif magnitud_terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala). ")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año...
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En cuál hemisferio te encuentras (N)orte o (S)ur? (N/S) --> ").upper()


if not (hemisferio == 'N' or hemisferio == 'S'):
    print("Error: Hemisferio debe ser N (Norte) o S (Sur)")
else:

    mes = int(input("¿Qué mes del año es? (1-12) --> "))
    dia = int(input("¿Qué día del año es? (1-31) --> "))

    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        if hemisferio == 'N':
            estacion = "Invierno"
        else:
            estacion = "Verano"

    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        if hemisferio == 'N':
            estacion = "Primavera"
        else:
            estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        if hemisferio == 'N':
            estacion = "Verano"
        else:
            estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        if hemisferio == 'N':
            estacion = "Otoño"
        else:
            estacion = "Primavera"
    else:
        estacion = "Error Fecha invalida"
    if estacion != "Error Fecha invalida":
        print("La estacion actual es: ",estacion)