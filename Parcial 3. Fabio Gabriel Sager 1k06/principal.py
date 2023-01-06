"""Una empresa de alquiler de vehículos necesita un programa para procesar los datos de los alquileres que
tiene ofrecidos. Por cada alquiler se tienen los siguientes datos: número de identificación de esa operación,
descripción del automóvil alquilado, el tipo de vehículo (un número entero entre 1 y 10, para indicar por ejemplo: 1:
sedán cuatro puertas, 2: familiar siete asientos, etc.), el importe a cobrar por el alquiler y la cantidad de días por
los que se hace el alquiler. Se desea almacenar la información referida a los n alquileres en un arreglo de
registros de tipo Alquiler (definir el tipo Alquiler y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo
dos módulos, que permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de los n alquileres. Valide que el número identificador de la operación
de alquiler sea positivo y que el tipo del vehículo esté entre 1 y 10. Puede hacer la carga en forma manual,
o puede generar los datos en forma automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea.
Pero al menos una debe programar.

2- Mostrar todos los datos de todos los alquileres, en un listado ordenado de menor a mayor según los importes
a cobrar de esos alquileres. En el listado no incluya la visualización de la cantidad de días de alquiler.
Al final del listado, mostrar una línea adicional en la que se indique el importe promedio pagado entre todos
los vehículos que se mostraron.

3- Determinar y mostrar la cantidad de alquileres que se hicieron de cada tipo posible de vehículo
(un contador para los alquileres tipo 1, otro para el tipo 2, etc.) En total, 10 contadores.
Muestre solo los resultados mayores a cero.

4- Determinar y mostrar el alquiler con mayor importe. Mostrar además la diferencia entre este importe mayor,
y el importe promedio entre todos los alquileres del arreglo.

5- Determinar si fue alquilado un vehículo cuya descripción sea igual a c y que tenga un importe de x o más,
siendo c y x dos valores que se cargan por teclado. Si existe, mostrar sus datos. Si no existe, informar con un mensaje.
Si existe más de un registro que coincida con esos parámetros de búsqueda,
debe mostrar sólo el primero que encuentre."""

import funciones
import validaciones
from registro_alquiler import *


def principal():
    vec_alquileres = []

    opcion = -1

    while opcion != 6:
        opcion = funciones.menu_principal()

        # Si no existe un vector cargado con alquileres, no se puede ejecutar ningna opcion que requiere
        # de este para operar
        if opcion != 1 and opcion != 6 and len(vec_alquileres) == 0:
            print()
            print('Debe haber cargado alquileres antes de hacer esto')
            print()
            input('Presione enter para continuar')
            print()
            continue

        # Conformacion de la opcion uno, carga de vector_alquiler
        elif opcion == 1:
            cantidad = validaciones.cargar_y_validar_mayor_que(1, 'Ingrese la cantidad de alquileres: ',
                                                               'ERROR LA CANTIDAD DEBE SER MAYOR A 0')

            vec_alquileres = funciones.cargar_vec_alquileres(cantidad)

            # Muestra de alquileres generados
            print('Generando alquileres...')
            print()
            for alquiler in vec_alquileres:
                write(alquiler)

            print()
            print('Alquileres generados...')
            print()
            input('Presione enter para continuar')
            print()

        elif opcion == 2:
            # Se ordena el vector alquileres segun los importes de los alquileres
            funciones.shell_sort_importes(vec_alquileres)

            # Se muestra el vector alquileres ordenado
            print('Mostrando y ordenando alquileres por importe...')
            print()

            for alquiler in vec_alquileres:
                write(alquiler)

            print()
            input('Presione enter para continuar')
            print()

        elif opcion == 3:
            # Se genera un vector de conteo por tipo de auto
            vec_conteo = funciones.contar_alquileres_por_tipo_auto(vec_alquileres)

            # Se recorre el vector de conteo por tipo de auto y se muestran solo aquellos tipos que tengan mas de
            # 0 alquileres
            for i in range(len(vec_conteo)):
                if vec_conteo[i] > 0:
                    print(f'Se contaron {vec_conteo[i]} del tipo {i+1}')

            print()
            input('Presione enter para continuar')
            print()

        elif opcion == 4:
            # Se busca y guarda el indice del mayor importe de los alquileres
            indice_mayor_importe = funciones.buscar_mayor_importe(vec_alquileres)
            # Se calcula y guarda el promedio de los importes de los alquileres
            promedio_importes = funciones.calcular_promedio_importes(vec_alquileres)

            # Se muestran los datos del alquiler con mayor importe
            print('El alquiler con mayor importe es: ')
            write(vec_alquileres[indice_mayor_importe])

            # Se muestra la diferencia entre el mayor importe y el promedio de importes
            print()
            print(f'La diferencia de este con el promedio de importes es: '
                  f'{vec_alquileres[indice_mayor_importe].importe - promedio_importes}')

            print()
            input('Presione enter para continuar')
            print()

        elif opcion == 5:
            # Se habilita teclado para la carga de la descripcion de el auto buscado
            descripcion = input('Ingrese la descripcion del vehiculo buscado: ')
            # Se habilita telcado para la carga del importe a buscar
            importe = validaciones.cargar_y_validar_mayor_que(1, 'Ingrese el importe buscado: ',
                                                              'ERROR DEBE SER MAYOR A 0')

            # Se busca y se guarda el indice del alquiler con la descipcion ingresada anteriormente y
            # con mayor o igual importe ingresado anterior mente
            indice_de_alquiler_buscado = funciones.buscar_vehiculo_x_desc_y_importe(vec_alquileres, descripcion,
                                                                                    importe)

            # Si el alquiler fue encontrado se muestran sus datos
            if indice_de_alquiler_buscado != -1:
                print('El alquiler buscado es: ')
                write(vec_alquileres[indice_de_alquiler_buscado])

            # Si no se menciona que no fue encontrado
            else:
                print('Ese alquiler no se encuentra registrado')

            print()
            input('Presione enter para continuar')
            print()

        # Opcion de salir del programa
        elif opcion == 6:
            print('Gracias por utilizar este programa, adios!')

            print()
            input('Presione enter para finalizar')
            print()


if __name__ == '__main__':
    principal()
