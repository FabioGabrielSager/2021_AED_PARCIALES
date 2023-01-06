"""Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

1.)    Ingrese tres cantidades que corresponden a las ventas de tres sucursales de una empresa informática,
       y cargue también el nombre de cada sucursal. Muestre el nombre de la sucursal con menor cantidad de ventas.
       Informe si el promedio de las tres cantidades fue mayor a 100. En caso contrario informar "No cumplió
       la condición".

2.)    Ingresar una secuencia de números, a razón de un número por vuelta de ciclo. La carga de dicha secuencia
       finaliza cuando se ingresa un cero. Determine el porcentaje de números que sean pares y
       mayores a 50 respecto al total de números ingresados. Informe si el porcentaje calculado se encuentra
       incluido está entre los valores x e y (que también deben ser cargados por teclado). En caso contrario
       informar que el porcentaje no se encuentra dentro del rango especificado.

3.)    Terminar el programa."""

# Titulo
print("■ " * 27)
print("\t" * 5, "Parcial 1")
print("■ " * 27)

# Menu de opciones
opcion = 0

while opcion != 3:
    # opciones
    print("\t" * 4, "■" * 16)
    print("\t" * 5, "Opciones")
    print("\t" * 4, "■" * 16)

    # Impresion de opciones a elejir
    print("■" * 54)
    print("1: Analizar datos de ventas de secursales\n"
          "2: Leer secuencia de numeros ingresados de uno por vez\n"
          "3: Salir del programa")
    print("■" * 54)

    print()
    # Habilitacion de teclado para ingreso de opcion seleccionada
    opcion = int(input("Ingrese, segun lo que desee, "
                       "el numero de opcion seleccionada: "))

    print()

    # Conformacion de opcion 1 (cantidad de ventas de sucursales)
    if opcion == 1:
        # Carga de datos, nombres de sucursales y cantidad de ventas.
        nom_sucursal_1 = input("Ingrese el nombre de la sucursal 1: ")
        cant_ventas_sucur_1 = int(input("Ingrese su cantidad de ventas: "))

        print()

        nom_sucursal_2 = input("Ingrese el nombre de la sucursal 2: ")
        cant_ventas_sucur_2 = int(input("Ingrese su cantidad de ventas: "))

        print()

        nom_sucursal_3 = input("Ingrese el nombre de la sucursal 3: ")
        cant_ventas_sucur_3 = int(input("Ingrese su cantidad de ventas: "))

        # Busqueda de la menor cantidad de ventas realizadas.
        if cant_ventas_sucur_1 < cant_ventas_sucur_2 \
           and cant_ventas_sucur_1 < cant_ventas_sucur_3:
            menor_en_ventas = nom_sucursal_1

        elif cant_ventas_sucur_2 < cant_ventas_sucur_3:
            menor_en_ventas = nom_sucursal_2

        else:
            menor_en_ventas = nom_sucursal_3

        # Calculo del promedio de ventas entre las tres sucursales.
        promedio_ventas = round((cant_ventas_sucur_1 + cant_ventas_sucur_2 + cant_ventas_sucur_3) / 3, 2)

        # Impresion en pantalla de resultados 1 (sucursal con menor cantidad de ventas).
        print("■" * 70)
        print("La sucursal con menor cantidad de ventas fue:", menor_en_ventas)

        # Segunda impresion de resultados (fue el promedio de ventas menor a cien?)
        if promedio_ventas > 100:
            print("El promedio de ventas fue mayor a 100")
        else:
            print("No cumplió la condición, el promedio de ventas fue menor a 100")
        print("■" * 70)

        print()
        input("Presione enter para continuar")
        print()

    # Conformacion de opcion 2. Secuencias de numeros.
    elif opcion == 2:
        # Contadores
        cont_nums = cont_pares = 0

        # Carga de datos (da arranque al ciclo).
        num = int(input("Ingrese un numero (con 0 termina): "))

        # Ciclo while, para carga de secuencia de numeros por vuelta de ciclo
        while num != 0:
            # Contador total de numeros
            cont_nums += 1

            # Se trata de un numero mayor a 50?
            if num > 50:
                # Se trata de un numero par?
                if (num % 2) == 0:
                    cont_pares += 1

            # Carga de datos correspondiente al ciclo, para evitar infinitud.
            num = int(input("Ingrese un numero (con 0 termina): "))

        print()

        # Condicional para evitar error de primer carga = 0.
        if cont_nums > 0:
            # Determinacion de porcentaje de numero pares > 50, con respecto al total.
            porcentaje_pares = (cont_pares * 100) / cont_nums

            # Habilitacion de teclado para el ingreso del
            # rango en el que se debe encontrar el porcentaje de los numeros pares mayores a 50.
            lim_inf = int(input("Ingrese el limite inferior del porcentaje de pares: "))
            lim_sup = int(input("Ingres el limite superior del porcentaje de pares: "))

            # Impresion en pantalla de resultados
            print()
            print("■" * 65)
            print("El porcentaje de numeros pares mayores a 50 es de:", porcentaje_pares)

            # Esta el procentaje de numero pares comprendido en los limites cargados previamente?
            if lim_inf < porcentaje_pares < lim_sup:
                print("El porcentaje esta comprendido entre", lim_inf, "y", lim_sup)
            else:
                print("El porcentaje no esta comprendido entre", lim_inf, "y", lim_sup)
            print("■" * 65)

        # Si no se cargo ningun numero, es decir, la primer carga es = 0.
        else:
            print("=" * 27)
            print("No se ingreso ningun numero")
            print("=" * 27)

        print()
        input("Presione enter para continuar")
        print()

    # Conformacion de opcion 3 (salir del programa).
    elif opcion == 3:
        print("■" * 42)
        print("Gracias por utilizar este programa, adios!")
        print("■" * 42)
        print()
        input("Presione enter para finalizar")
        print()

    # Si no se carga una opcion valida.
    elif opcion != 3:
        print("=" * 29)
        print("¡ERROR, ESA OPCION NO EXISTE!")
        print("=" * 29)
        print()
        input("Presione enter para continuar")
        print()
