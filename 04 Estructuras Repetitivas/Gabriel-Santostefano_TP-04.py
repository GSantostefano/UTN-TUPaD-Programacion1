#  1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#  (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

print("EJERCICIO 1 NUMEROS DEL 0 AL 100")
for i in range(101):
    print(i)

#  2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#  dígitos que contiene. 

print("\nEJERCICIO 2 CONTAR DIGITOS")
numero = int(input("INGRESE UN NUMERO ENTERO: "))

numero_str = str(abs(numero))
cantidad_digitos = len(numero_str)

print(f"El número {numero} tiene {cantidad_digitos} dígito(s)")


#  3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#  dados por el usuario, excluyendo esos dos valores. 

print("\nEJERCICIO 3 SUMA ENTRE DOS VALORES")
valor1 = int(input("INGRESE EL PRIMER VALOR: "))
valor2 = int(input("INGRESE EL SEGUNDO VALOR: "))

menor = min(valor1, valor2)
mayor = max(valor1, valor2)

suma = 0
for i in range(menor + 1, mayor):
    suma += i

print(f"LA SUMA DE LOS NUMEROS ENTRE {valor1} y {valor2} (EXCLUYENDO EXTREMOS) ES: {suma}")


#  4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#  secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#  un 0. 

print("\nEJERCICIO 4 SUMA SECUENCIAL")
suma_total = 0
numero = int(input("INGRESE UN NUMERO (0 PARA TERMINAR): "))

while numero != 0:
    suma_total += numero
    numero = int(input("INGRESE OTRO NUMERO (0 PARA TERMINAR): "))

print(f"EL TOTAL ACUMULADO ES: {suma_total}")


#  5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#  programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random

print("\nEJERCICIO 5 JUEGO DE ADIVINANZA")
numero_secreto = random.randint(0, 9)
intentos = 0

print("ADIVINA EL NUMERO ENTRE 0 Y 9")

while True:
    intento = int(input("INGRESA TU NUMERO: "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡CORRECTO! EL NUMERO ERA {numero_secreto}")
        print(f"LO ADIVINASTE EN {intentos} INTENTO(S)")
        break
    else:
        print("INCORRECTO, INTENTA DE NUEVO")


#  6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#  entre 0 y 100, en orden decreciente. 


print("\nEJERCICIO 6 NUMEROS PARES DECRECIENTES")
for i in range(100, -1, -2):
    print(i)


#  7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#  número entero positivo indicado por el usuario.

print("\nEJERCICIO 7 SUMA DESDE 0 HASTA UN NUMERO")
numero = int(input("INGRESE UN NUMERO ENTERO POSITIVO: "))

suma = 0
for i in range(numero + 1):
    suma += i

print(f"LA SUMA DE TODOS LOS NUMEROS DESDE 0 HASTA {numero} ES: {suma}")


#  8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#  programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#  negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#  menor, pero debe estar preparado para procesar 100 números con un solo cambio). 

print("\nEJERCICIO 8 ANALISIS DE NUMEROS")
cantidad_numeros = 100
pares = 0
impares = 0
negativos = 0
positivos = 0

print(f"INGRESE {cantidad_numeros} NUMEROS ENTEROS:")

for i in range(cantidad_numeros):
    numero = int(input(f"NUMERO {i+1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"\nRESULTADOS:")
print(f"NUMEROS PARES: {pares}")
print(f"NUMEROS IMPARES: {impares}")
print(f"NUMEROS POSITIVOS: {positivos}")
print(f"NUMEROS NEGATIVOS: {negativos}")


#  9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#  media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#  poder procesar 100 números cambiando solo un valor). 

print("\nEJERCICIO 9 MEDIA DE NUMEROS")
cantidad_numeros = 100

suma_total = 0

print(f"INGRESE {cantidad_numeros} NUMEROS ENTEROS:")

for i in range(cantidad_numeros):
    numero = int(input(f"NUMERO {i+1}: "))
    suma_total += numero

media = suma_total / cantidad_numeros

print(f"\nLA SUMA TOTAL ES: {suma_total}")
print(f"LA MEDIA DE LOS {cantidad_numeros} NUMEROS ES: {media}")


#  10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#  usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


print("\nEJERCICIO 10 INVERTIR DIGITOS")
numero = int(input("INGRESE UN NUMERO ENTERO: "))

numero_str = str(numero)
numero_invertido_str = numero_str[::-1]
numero_invertido = int(numero_invertido_str)

print(f"EL NUMERO ORIGINAL: {numero}")
print(f"EL NUMERO INVERTIDO: {numero_invertido}")