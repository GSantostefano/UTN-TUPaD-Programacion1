#Alumno: Gabriel Santostefano

titulos = []
ejemplares = []
opcion = 0


while True:
    print ("\n=====================| UTN-TUP |=======================")
    print ("===========|  Primer Parcial Programación 1  |=========")
    print ("=============| Menú Biblioteca Escolar  |==============")
    print ("=======================================================")
    print ("\n>>  1-Ingresar Títulos")
    print (">>  2-Ingresar Ejemplares")
    print (">>  3-Mostrar Catálogo")
    print (">>  4-Consultar Disponibilidad")
    print (">>  5-Listar Agotados")
    print (">>  6-Agregar Título Con Ejemplares")
    print (">>  7-Actualizar Ejemplares (Préstamo/Devolución)")
    print (">>  8-Salir")
    print ("\n=======================================================")
    print ("==============| Por Gabriel Santostefano |=============")


    while True:
            opcionStr = input("\n>>  Seleccione una opción del 1 al 8 para continuar --> ").strip()
            if opcionStr == "":
                print("\n❌ Debe ingresar una opción!")
                continue
            if opcionStr.isdigit():
                opcion = int(opcionStr)
                if opcion >= 1 and opcion <= 8:
                    break
                else:
                    print("\n=====================¡¡Error!!=========================")
                    print("\n❌ Error! La opción debe ser un número del 1 al 8!")
            else:
                print("\n=====================¡¡Error!!=========================")
                print("\n❌ Error! La opción debe ser un número del 1 al 8!")

    match opcion:
        case 1:
            print("\n=====================Opción 1=========================")
            print("\nUsted eligió la Opción 1: Ingresar Títulos")
            titulo_confirmado = False
            while not titulo_confirmado:
                tituloStr = input("\nIngrese nuevo título >> ").strip()
                if tituloStr == "":
                    print("\n❌ Texto vacío!")
                    continue
                print('Usted ingresó el título:', '"',tituloStr, '"')
                while True:
                    modificar = input("\n¿Desea modificar? (S/N) >> ").upper().strip()
                    if modificar == "S":
                        break
                    elif modificar == "N":
                        titulo_existe = False
                        for i in range(len(titulos)):
                            if titulos[i].upper() == tituloStr.upper():
                                titulo_existe = True
                                break
                        if titulo_existe:
                            print("\n❌ Título ya existe!")
                            break
                        else:
                            titulos.append(tituloStr)
                            ejemplares.append(0)
                            print("\n✅ Título ingresado correctamente!")
                            
                            while True:
                                confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                                if confirmacion == "":
                                    break
                                else:
                                    print("\n❌ Presione solo Enter para continuar!")
                            titulo_confirmado = True
                            break
                    else:
                        print("\n❌ Opción inválida! Ingrese S o N")
                if modificar == "N" and not titulo_existe:
                    continue
        case 2:
            print("\n=====================Opción 2=========================")
            print("\nUsted eligió la Opción 2: Ingresar Ejemplares")
            
            if len(titulos) == 0:
                print("\n❌ No hay títulos registrados!")
                print("Primero debe ingresar títulos (Opción 1)")
                
                while True:
                    confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                    if confirmacion == "":
                        break
                    else:
                        print("\n❌ Presione solo Enter para continuar!")
                continue
            
            print("\nTítulos Disponibles:")
            print("=" * 50)
            print(f"{'N°':<4} {'Título':<35} {'Ejemplares':<10}")
            print("=" * 50)
            for i in range(len(titulos)):
                numero = i + 1
                titulo = titulos[i]
                ejemplares_count = ejemplares[i]
                
                if len(titulo) > 33:
                    titulo_mostrar = titulo[:30] + "..."
                else:
                    titulo_mostrar = titulo
                
                print(f"{numero:<4} {titulo_mostrar:<35} {ejemplares_count:<10}")
            print("=" * 50)
            
            while True:
                print(f"\n>> Seleccione un título del 1 al {len(titulos)}")
                seleccionStr = input("Ingrese número del título >> ").strip()
                
                if seleccionStr.isdigit():
                    seleccion = int(seleccionStr)
                    if seleccion >= 1 and seleccion <= len(titulos):
                        titulo_seleccionado = titulos[seleccion-1]
                        ejemplares_actuales = ejemplares[seleccion-1]
                        print(f"\nTítulo seleccionado: '{titulo_seleccionado}'")
                        print(f"Ejemplares actuales: {ejemplares_actuales}")
                        break
                    else:
                        print(f"\n❌ Número debe estar entre 1 y {len(titulos)}")
                else:
                    print("\n❌ Debe ingresar un número válido!")
            
            while True:
                cantidadStr = input(f"\n>> ¿Cuántos ejemplares desea agregar a '{titulo_seleccionado}'? >> ").strip()
                
                if cantidadStr.isdigit():
                    cantidad = int(cantidadStr)
                    if cantidad >= 0 and cantidad <= 9999:
                        ejemplares_nuevos = ejemplares[seleccion-1] + cantidad
                        if ejemplares_nuevos <= 9999:
                            ejemplares[seleccion-1] = ejemplares_nuevos
                            
                            print("\n✅ Ejemplares actualizados correctamente!")
                            print(f"Título: '{titulo_seleccionado}'")
                            print(f"Ejemplares anteriores: {ejemplares_actuales}")
                            print(f"Ejemplares agregados: {cantidad}")
                            print(f"Ejemplares totales: {ejemplares_nuevos}")
                            
                            while True:
                                confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                                if confirmacion == "":
                                    break
                                else:
                                    print("\n❌ Presione solo Enter para continuar!")
                            break
                        else:
                            print(f"\n❌ El total no puede superar 9999 ejemplares!")
                            print(f"Ejemplares actuales: {ejemplares_actuales}")
                            print(f"Cantidad a agregar: {cantidad}")
                            print(f"Total sería: {ejemplares_nuevos}")
                    elif cantidad > 9999:
                        print("\n❌ La cantidad no puede ser mayor a 9999!")
                    else:
                        print("\n❌ La cantidad debe ser 0 o positiva!")
                else:
                    print("\n❌ Debe ingresar un número válido!")
            continue
        case 3:
            print("\n=====================Opción 3=========================")
            print("\nUsted eligió la Opción 3: Mostrar Catálogo")
            
            if len(titulos) == 0:
                print("\n❌ No hay títulos registrados en el catálogo!")
                print("El catálogo está vacío")
                
                while True:
                    confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                    if confirmacion == "":
                        break
                    else:
                        print("\n❌ Presione solo Enter para continuar!")
            else:
                print("\n📚 ========== Catálogo de la Biblioteca ==========")
                print("=" * 55)
                print(f"{'N°':<4} {'Título':<35} {'Ejemplares':<10}")
                print("=" * 55)
                
                for i in range(len(titulos)):
                    numero = i + 1
                    titulo = titulos[i]
                    ejemplares_count = ejemplares[i]
                    
                    if len(titulo) > 33:
                        titulo_mostrar = titulo[:30] + "..."
                    else:
                        titulo_mostrar = titulo
                    
                    print(f"{numero:<4} {titulo_mostrar:<35} {ejemplares_count:<10}")
                
                print("=" * 55)
                
                total_libros = len(titulos)
                total_ejemplares = sum(ejemplares)
                libros_agotados = sum(1 for e in ejemplares if e == 0)
                
                print(f"\nEstadísticas del Catálogo:")
                print(f"   Total de títulos: {total_libros}")
                print(f"   Total de ejemplares: {total_ejemplares}")
                print(f"   Libros agotados: {libros_agotados}")
                print(f"   Libros disponibles: {total_libros - libros_agotados}")
                
                while True:
                    confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                    if confirmacion == "":
                        break
                    else:
                        print("\n❌ Presione solo Enter para continuar!")
            continue    
        case 4:
            print("\n=====================Opción 4=========================")
            print("\nUsted eligió la Opción 4: Consultar Disponibilidad")
            
            if len(titulos) == 0:
                print("\n❌ No hay títulos registrados!")
                
                while True:
                    confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                    if confirmacion == "":
                        break
                    else:
                        print("\n❌ Presione solo Enter para continuar!")
            else:
                titulo_buscar = input("\n>> Ingrese el título a buscar >> ").strip()
                
                if titulo_buscar == "":
                    print("\n❌ No puede ingresar texto vacío!")
                else:
                    titulo_encontrado = False
                    indice_encontrado = -1
                    
                    for i in range(len(titulos)):
                        if titulos[i].upper() == titulo_buscar.upper():
                            titulo_encontrado = True
                            indice_encontrado = i
                            break
                    
                    if titulo_encontrado:
                        titulo_real = titulos[indice_encontrado]
                        ejemplares_disponibles = ejemplares[indice_encontrado]
                        
                        print(f"\nTítulo: {titulo_real}")
                        print(f"Ejemplares disponibles: {ejemplares_disponibles}")
                    else:
                        print(f"\n❌ Título no encontrado: '{titulo_buscar}'")
                
                while True:
                    confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                    if confirmacion == "":
                        break
                    else:
                        print("\n❌ Presione solo Enter para continuar!")
            continue
        case 5:
            print("\n=====================Opción 5=========================")
            print("\nUsted eligió la Opción 5: Listar Agotados")
            
            if len(titulos) == 0:
                print("\n❌ No hay títulos registrados!")
            else:
                libros_agotados = []
                for i in range(len(titulos)):
                    if ejemplares[i] == 0:
                        libros_agotados.append(titulos[i])
                
                if len(libros_agotados) == 0:
                    print("\n✅ No hay libros agotados")
                    print("Todos los títulos tienen ejemplares disponibles")
                else:
                    print(f"\n❌ Libros agotados ({len(libros_agotados)}):")
                    for i in range(len(libros_agotados)):
                        print(f"   {i+1}. {libros_agotados[i]}")
            
            while True:
                confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                if confirmacion == "":
                    break
                else:
                    print("\n❌ Presione solo Enter para continuar!")
            continue
        case 6:
            print("\n=====================Opción 6=========================")
            print("\nUsted eligió la Opción 6: Agregar Título Con Ejemplares")
            
            while True:
                titulo_nuevo = input("\n>> Ingrese el nuevo título >> ").strip()
                
                if titulo_nuevo == "":
                    print("\n❌ No puede ingresar texto vacío!")
                    continue
                
                titulo_existe = False
                for i in range(len(titulos)):
                    if titulos[i].upper() == titulo_nuevo.upper():
                        titulo_existe = True
                        break
                
                if titulo_existe:
                    print("\n❌ Título ya existe!")
                    continue
                else:
                    break
            
            while True:
                cantidadStr = input(f"\n>> ¿Cuántos ejemplares desea agregar a '{titulo_nuevo}'? >> ").strip()
                
                if cantidadStr.isdigit():
                    cantidad = int(cantidadStr)
                    if cantidad >= 0 and cantidad <= 9999:
                        break
                    elif cantidad > 9999:
                        print("\n❌ La cantidad no puede ser mayor a 9999!")
                    else:
                        print("\n❌ La cantidad debe ser 0 o positiva!")
                else:
                    print("\n❌ Debe ingresar un número válido!")
            
            titulos.append(titulo_nuevo)
            ejemplares.append(cantidad)
            
            print(f"\n✅ Título agregado correctamente!")
            print(f"Título: {titulo_nuevo}")
            print(f"Ejemplares: {cantidad}")
            
            while True:
                confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                if confirmacion == "":
                    break
                else:
                    print("\n❌ Presione solo Enter para continuar!")
            continue
        case 7:
            print("\n=====================Opción 7=========================")
            print("\nUsted eligió la Opción 7: Actualizar Ejemplares (Préstamo/Devolución)")
            
            if len(titulos) == 0:
                print("\n❌ No hay títulos registrados!")
                
                while True:
                    confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                    if confirmacion == "":
                        break
                    else:
                        print("\n❌ Presione solo Enter para continuar!")
            else:
                
                print("\nTítulos Disponibles:")
                print("=" * 50)
                print(f"{'N°':<4} {'Título':<35} {'Ejemplares':<10}")
                print("=" * 50)
                for i in range(len(titulos)):
                    numero = i + 1
                    titulo = titulos[i]
                    ejemplares_count = ejemplares[i]
                    
                    if len(titulo) > 33:
                        titulo_mostrar = titulo[:30] + "..."
                    else:
                        titulo_mostrar = titulo
                    
                    print(f"{numero:<4} {titulo_mostrar:<35} {ejemplares_count:<10}")
                print("=" * 50)
                
                while True:
                    print(f"\n>> Seleccione un título del 1 al {len(titulos)}")
                    seleccionStr = input("Ingrese número del título >> ").strip()
                    
                    if seleccionStr.isdigit():
                        seleccion = int(seleccionStr)
                        if seleccion >= 1 and seleccion <= len(titulos):
                            titulo_seleccionado = titulos[seleccion-1]
                            ejemplares_actuales = ejemplares[seleccion-1]
                            print(f"\nTítulo seleccionado: '{titulo_seleccionado}'")
                            print(f"Ejemplares actuales: {ejemplares_actuales}")
                            break
                        else:
                            print(f"\n❌ Número debe estar entre 1 y {len(titulos)}")
                    else:
                        print("\n❌ Debe ingresar un número válido!")
                
                while True:
                    print(f"\n>> ¿Qué operación desea realizar?")
                    print("   1. Préstamo (Disminuir 1 ejemplar)")
                    print("   2. Devolución (Aumentar 1 ejemplar)")
                    
                    operacionStr = input("Ingrese opción (1 o 2) >> ").strip()
                    
                    if operacionStr == "1":
                        if ejemplares_actuales > 0:
                            ejemplares[seleccion-1] = ejemplares[seleccion-1] - 1
                            print("\n✅ Préstamo realizado correctamente!")
                            print(f"Título: '{titulo_seleccionado}'")
                            print(f"Ejemplares anteriores: {ejemplares_actuales}")
                            print(f"Ejemplares actuales: {ejemplares[seleccion-1]}")
                        else:
                            print(f"\n❌ No se puede realizar préstamo!")
                            print(f"No hay ejemplares disponibles")
                            print(f"Título: '{titulo_seleccionado}'")
                            print(f"Ejemplares: {ejemplares_actuales}")
                        break
                    elif operacionStr == "2":
                        
                        ejemplares[seleccion-1] = ejemplares[seleccion-1] + 1
                        print("\n✅ Devolución realizada correctamente!")
                        print(f"Título: '{titulo_seleccionado}'")
                        print(f"Ejemplares anteriores: {ejemplares_actuales}")
                        print(f"Ejemplares actuales: {ejemplares[seleccion-1]}")
                        break
                    else:
                        print("\n❌ Opción inválida! Ingrese 1 o 2")
                
                while True:
                    confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                    if confirmacion == "":
                        break
                    else:
                        print("\n❌ Presione solo Enter para continuar!")
            continue
        case 8:
            print("\n=====================Opción 8=========================")
            print("\nUsted eligió la Opción 8! - Salir")
            
            while True:
                confirmacion = input("\n>> ¿Está seguro de que desea salir? (S/N) >> ").upper().strip()
                if confirmacion == "S":
                    print("\n===================Fin del Programa===================")
                    exit()
                elif confirmacion == "N":
                    print("\nRegresando al menú principal...")
                    break
                else:
                    print("\n❌ Opción inválida! Ingrese S o N")
        case _:
            print("\n=====================¡¡Error!!=========================")
            print("\n❌ Error! La opción debe ser un número del 1 al 8!")
            
            while True:
                confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
                if confirmacion == "":
                    break
                else:
                    print("\n❌ Presione solo Enter para continuar!")

