# Trabajo Practico 8 - Manejo de Archivos
# Universidad Tecnologica Nacional - TUPaD
# Estudiante: Gabriel Santostefano

import os

ARCHIVO_PRODUCTOS = "productos.txt"

def crear_archivo_inicial():
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        with open(ARCHIVO_PRODUCTOS, 'w', encoding='utf-8') as archivo:
            archivo.write("Lapiz,1200.5,30\n")
            archivo.write("Cuaderno,4500.0,15\n")
            archivo.write("Regla,850.75,25\n")
        print("Archivo productos.txt creado con productos iniciales.\n")
    else:
        print("El archivo productos.txt ya existe.\n")

def leer_y_mostrar_productos():
    productos = []
    
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        print(f"El archivo {ARCHIVO_PRODUCTOS} no existe.\n")
        return productos
    
    with open(ARCHIVO_PRODUCTOS, 'r', encoding='utf-8') as archivo:
        print("=== PRODUCTOS EXISTENTES ===\n")
        
        for linea in archivo:
            linea_limpia = linea.strip()
            
            if linea_limpia:
                datos = linea_limpia.split(",")
                
                if len(datos) == 3:
                    nombre = datos[0].strip()
                    precio = float(datos[1].strip())
                    cantidad = int(datos[2].strip())
                    
                    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
                    
                    productos.append({
                        'nombre': nombre,
                        'precio': precio,
                        'cantidad': cantidad
                    })
                else:
                    print(f"Advertencia: Linea con formato incorrecto ignorada: {linea_limpia}")
        print()
    
    return productos

def agregar_producto_desde_teclado(productos):
    print("=== AGREGAR NUEVO PRODUCTO ===\n")
    
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    if not nombre:
        print("Error: El nombre del producto no puede estar vacio.\n")
        return
    
    precio_str = input("Ingrese el precio del producto: ").strip()
    precio = float(precio_str)
    if precio < 0:
        print("Error: El precio no puede ser negativo.\n")
        return
    
    cantidad_str = input("Ingrese la cantidad del producto: ").strip()
    cantidad = int(cantidad_str)
    if cantidad < 0:
        print("Error: La cantidad no puede ser negativa.\n")
        return
    
    with open(ARCHIVO_PRODUCTOS, 'a', encoding='utf-8') as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    
    nuevo_producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    productos.append(nuevo_producto)
    
    print(f"\nProducto '{nombre}' agregado correctamente al archivo y a la lista.\n")

def buscar_producto_por_nombre(productos):
    print("=== BUSCAR PRODUCTO ===\n")
    
    if not productos:
        print("No hay productos en la lista. Primero debe leer o agregar productos.\n")
        return
    
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    
    if not nombre_buscar:
        print("Error: Debe ingresar un nombre para buscar.\n")
        return
    
    encontrado = False
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscar.lower():
            print(f"\nProducto encontrado:")
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}\n")
            encontrado = True
            break
    
    if not encontrado:
        print(f"\nError: El producto '{nombre_buscar}' no existe.\n")

def guardar_productos_actualizados(productos):
    if not productos:
        print("No hay productos para guardar.\n")
        return
    
    with open(ARCHIVO_PRODUCTOS, 'w', encoding='utf-8') as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Productos guardados correctamente en productos.txt\n")

def mostrar_menu():
    print("=" * 50)
    print("SISTEMA DE GESTION DE PRODUCTOS")
    print("=" * 50)
    print("\nOpciones disponibles:")
    print("1. Leer y mostrar productos")
    print("2. Agregar nuevo producto")
    print("3. Buscar producto por nombre")
    print("4. Guardar productos actualizados")
    print("5. Salir")
    print("=" * 50)

def main():
    print("\n=== TRABAJO PRACTICO 8 - MANEJO DE ARCHIVOS ===\n")
    
    crear_archivo_inicial()
    productos = leer_y_mostrar_productos()
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion (1-5): ").strip()
        
        if opcion == '1':
            productos = leer_y_mostrar_productos()
            input("\nPresione Enter para continuar...")
        elif opcion == '2':
            agregar_producto_desde_teclado(productos)
            input("\nPresione Enter para continuar...")
        elif opcion == '3':
            buscar_producto_por_nombre(productos)
            input("\nPresione Enter para continuar...")
        elif opcion == '4':
            guardar_productos_actualizados(productos)
            input("\nPresione Enter para continuar...")
        elif opcion == '5':
            guardar_productos_actualizados(productos)
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("\nOpcion no valida. Por favor seleccione una opcion del 1 al 5.")

main()
