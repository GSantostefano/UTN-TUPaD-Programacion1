# Trabajo Practico 9 - Aplicacion de la Recursividad
# Universidad Tecnologica Nacional - TUPaD
# Estudiante: Gabriel Santostefano

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)

def es_palindrome(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0].lower() != palabra[-1].lower():
        return False
    else:
        return es_palindrome(palabra[1:-1])

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo_digito = numero % 10
        resto = numero // 10
        if ultimo_digito == digito:
            return 1 + contar_digito(resto, digito)
        else:
            return contar_digito(resto, digito)

def ejercicio_1():
    print("=== EJERCICIO 1: FACTORIAL RECURSIVO ===\n")
    numero = int(input("Ingrese un numero entero positivo: "))
    if numero < 1:
        print("Error: Debe ingresar un numero positivo mayor a 0.\n")
        return
    
    print(f"\nFactoriales del 1 al {numero}:\n")
    for i in range(1, numero + 1):
        resultado = factorial(i)
        print(f"{i}! = {resultado}")
    print()

def ejercicio_2():
    print("=== EJERCICIO 2: SERIE DE FIBONACCI RECURSIVA ===\n")
    posicion = int(input("Ingrese la posicion hasta la cual desea ver la serie: "))
    if posicion < 0:
        print("Error: Debe ingresar un numero positivo o cero.\n")
        return
    
    print(f"\nSerie de Fibonacci hasta la posicion {posicion}:\n")
    for i in range(posicion + 1):
        valor = fibonacci(i)
        print(f"F({i}) = {valor}")
    print()

def ejercicio_3():
    print("=== EJERCICIO 3: POTENCIA RECURSIVA ===\n")
    base = float(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente (entero positivo): "))
    if exponente < 0:
        print("Error: El exponente debe ser un numero entero positivo.\n")
        return
    
    resultado = potencia(base, exponente)
    print(f"\n{base}^{exponente} = {resultado}\n")

def ejercicio_4():
    print("=== EJERCICIO 4: CONVERSION DECIMAL A BINARIO RECURSIVA ===\n")
    numero = int(input("Ingrese un numero entero positivo: "))
    if numero < 0:
        print("Error: Debe ingresar un numero positivo.\n")
        return
    
    resultado = decimal_a_binario(numero)
    print(f"\n{numero} en binario es: {resultado}\n")

def ejercicio_5():
    print("=== EJERCICIO 5: PALINDROMO RECURSIVO ===\n")
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ").strip()
    
    if not palabra:
        print("Error: Debe ingresar una palabra.\n")
        return
    
    resultado = es_palindrome(palabra)
    if resultado:
        print(f"\n'{palabra}' ES un palindromo.\n")
    else:
        print(f"\n'{palabra}' NO es un palindromo.\n")

def ejercicio_6():
    print("=== EJERCICIO 6: SUMA DE DIGITOS RECURSIVA ===\n")
    numero = int(input("Ingrese un numero entero positivo: "))
    if numero < 0:
        print("Error: Debe ingresar un numero positivo.\n")
        return
    
    resultado = suma_digitos(numero)
    print(f"\nLa suma de los digitos de {numero} es: {resultado}\n")

def ejercicio_7():
    print("=== EJERCICIO 7: PIRAMIDE DE BLOQUES RECURSIVA ===\n")
    n = int(input("Ingrese el numero de bloques en el nivel mas bajo: "))
    if n < 1:
        print("Error: Debe ingresar un numero positivo mayor a 0.\n")
        return
    
    resultado = contar_bloques(n)
    print(f"\nPara construir una piramide con {n} bloques en el nivel mas bajo,")
    print(f"se necesitan {resultado} bloques en total.\n")

def ejercicio_8():
    print("=== EJERCICIO 8: CONTAR DIGITO RECURSIVO ===\n")
    numero = int(input("Ingrese un numero entero positivo: "))
    digito = int(input("Ingrese un digito (0-9) a buscar: "))
    
    if numero < 0:
        print("Error: El numero debe ser positivo.\n")
        return
    
    if digito < 0 or digito > 9:
        print("Error: El digito debe estar entre 0 y 9.\n")
        return
    
    resultado = contar_digito(numero, digito)
    print(f"\nEl digito {digito} aparece {resultado} vez/veces en el numero {numero}.\n")

def mostrar_menu():
    print("=" * 60)
    print("TRABAJO PRACTICO 9 - APLICACION DE LA RECURSIVIDAD")
    print("Universidad Tecnologica Nacional - TUPaD")
    print("=" * 60)
    print("\nEjercicios disponibles:")
    print("1. Factorial recursivo")
    print("2. Serie de Fibonacci recursiva")
    print("3. Potencia recursiva")
    print("4. Conversion decimal a binario recursiva")
    print("5. Palindromo recursivo")
    print("6. Suma de digitos recursiva")
    print("7. Piramide de bloques recursiva")
    print("8. Contar digito recursivo")
    print("9. Salir")
    print("=" * 60)

def main():
       
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion (1-9): ").strip()
        
        if opcion == '1':
            ejercicio_1()
            input("Presione Enter para continuar...")
        elif opcion == '2':
            ejercicio_2()
            input("Presione Enter para continuar...")
        elif opcion == '3':
            ejercicio_3()
            input("Presione Enter para continuar...")
        elif opcion == '4':
            ejercicio_4()
            input("Presione Enter para continuar...")
        elif opcion == '5':
            ejercicio_5()
            input("Presione Enter para continuar...")
        elif opcion == '6':
            ejercicio_6()
            input("Presione Enter para continuar...")
        elif opcion == '7':
            ejercicio_7()
            input("Presione Enter para continuar...")
        elif opcion == '8':
            ejercicio_8()
            input("Presione Enter para continuar...")
        elif opcion == '9':
            print("\n¡Gracias por usar el sistema!")
            break
        else:
            print("\nOpcion no valida. Por favor seleccione una opcion del 1 al 9.")

if __name__ == "__main__":
    main()

