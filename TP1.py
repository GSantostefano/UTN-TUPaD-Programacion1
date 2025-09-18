# Trabajo Práctico 1 - Programación
# Universidad Tecnológica Nacional - TUPaD

print("=== TRABAJO PRÁCTICO 1 - PROGRAMACION ===\n")

# Actividad 1: Imprimir "Hola Mundo!"
print("1) Hola Mundo!")
print("Hola Mundo!\n")

# Actividad 2: Saludo personalizado
print("2) Saludo personalizado")
nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola {nombre}!\n")

# Actividad 3: Información personal
print("3) Información personal")
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar_residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.\n")

# Actividad 4: Área y perímetro de un círculo
print("4) Cálculo de área y perímetro de un círculo")
import math
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Para un círculo de radio {radio}:")
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}\n")

# Actividad 5: Conversión de segundos a horas
print("5) Conversión de segundos a horas")
segundos = float(input("Ingresa la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.4f} horas\n")

# Actividad 6: Tabla de multiplicar
print("6) Tabla de multiplicar")
numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
print("-----------------------------")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} × {i} = {resultado}")
print()

# Actividad 7: Operaciones con dos números
print("7) Operaciones con dos números enteros")
print("Ingresa dos números enteros distintos de cero:")
num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
if num1 == 0 or num2 == 0:
    print("Error: Ambos números deben ser distintos de cero")
else:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    
    print(f"\nResultados de las operaciones con {num1} y {num2}:")
    print("=" * 40)
    print(f"Suma: {num1} + {num2} = {suma}")
    print(f"Resta: {num1} - {num2} = {resta}")
    print(f"Multiplicación: {num1} × {num2} = {multiplicacion}")
    print(f"División: {num1} ÷ {num2} = {division:.2f}")
print()

# Actividad 8: Índice de masa corporal
print("8) Cálculo del Índice de Masa Corporal")
altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Tu Índice de Masa Corporal es: {imc:.2f}\n")

# Actividad 9: Conversión de temperatura
print("9) Conversor de temperatura: Celsius a Fahrenheit")
print("==============================================")
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F\n")

# Actividad 10: Promedio de tres números
print("10) Cálculo del promedio de tres números")
print("Cálculo detallado del promedio")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
num3 = float(input("Tercer número: "))
suma = num1 + num2 + num3
print(f"\nPaso 1: Suma = {num1} + {num2} + {num3} = {suma}")
print(f"Paso 2: Cantidad de números = 3")
print(f"Paso 3: Promedio = {suma} ÷ 3 = {suma/3:.2f}")
print(f"\nEl promedio es: {(num1 + num2 + num3)/3:.2f}")

print("\n=== FIN DEL PROGRAMA ===")