"""Una empresa de venta de revistas mantiene información sobre los distintos artículos que tiene a la venta. Por cada
revista se registran los datos siguientes: número de identificación (un entero), nombre de la revista (una cadena),
precio de venta, editorial de procedencia (un valor entre 0 y 19 incluidos, por ejemplo: 0: Marvel, 1: DC Comics, 2:
National Geographics, etc.), tipo de revista (un número entero entre 0 y 19 incluidos, para indicar (por ejemplo): 0:
comic, 1: científica, 2: moda, etc.) y su cantidad en stock. Se pide definir un tipo registro Registro con los campos
que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Revista en un arreglo de registros (cargue n por teclado). Puede cargar
los datos manualmente, o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual, y
si la hace automática entonces TODA debe ser automática). Validar los campos que sea necesario. El arreglo debe crearse
de forma que siempre quede ordenado de menor a mayor, según el número de identificación de las revistas, y para hacer
esto debe aplicar el algoritmo de inserción ordenada con búsqueda binaria. Se considerará directamente incorrecta la
solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero
con búsqueda secuencial.

2- Mostrar el arreglo creado en el punto 1, a razón de un registro por línea, pero muestre solo los registros cuya
cantidad en stock sea mayor al valor st que se carga por teclado.

3- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación de
la revista sea igual a un valor p ingresado por el usuario. Si existe, mostrar por pantalla todos sus datos.
Si no existe, informar con un mensaje.

4- Guarde en un archivo los registros del arreglo cuyo tipo de revista esté entre dos valores x e y que se cargan por
teclado.

5- Mostrar el archivo creado en el punto anterior, pero solamente aquellos cuyo stock sea mayor a cero. Muestre al final
del listado una línea adicional indicando la cantidad de registros que se mostraron."""
import time
import interface
import funciones
import registro_revista
import validaciones


def principal():
    fd = 'Revistas.dat'
    vec_revistas = []
    op = -1

    while op != 6:
        op = interface.menu_principal()

        if op != 1 and op != 5 and op != 6 and len(vec_revistas) == 0:
            print('ERROR, PRIMERO DEBER CARGAR EN ARREGLO ANTES DE EJECUTAR ESTA OPCION')
            interface.presione_enter_para()

        if op == 1:
            cantidad = validaciones.cargar_y_validar_mayor_que(0, 'Ingrese la cantidad de revistas a generar: ',
                                                               'ERROR LA CANTIDAD ES ERRONEA, DEBE SER MAYOR A 0')

            print('Creando arreglo...')
            vec_revistas = funciones.crear_arreglo_revistas(cantidad)
            print()
            time.sleep(0.5)
            print('Arreglo creado...')
            interface.presione_enter_para()

        elif op == 2:
            st = validaciones.cargar_y_validar_mayor_que(0, 'Ingrese la cantidad minima de stock a mostrar: ',
                                                         'ERROR LA CANTIDAD ES ERRONEA, DEBE SER MAYOR A 0')

            print('Mostrando registos...')
            interface.mostrar_arreglo_revistas_con_filtro_op2(vec_revistas, st)

            print('Registros mostrados...')
            interface.presione_enter_para()

        elif op == 3:
            num_identificacion_a_buscar = int(input('Ingrese el numero de identificacion a buscar: '))

            pos_revista_buscada = funciones.buscar_en_arreglo_x_num_iden(vec_revistas, num_identificacion_a_buscar)

            if pos_revista_buscada != -1:
                print()
                print(f'Revista con numero {num_identificacion_a_buscar} encontrada, mostrando datos')
                print(registro_revista.to_string(vec_revistas[pos_revista_buscada]))
                interface.presione_enter_para()
                print()

            else:
                print()
                print(f'Revista con numero {num_identificacion_a_buscar} no encontrada')
                interface.presione_enter_para()
                print()

        elif op == 4:
            lim_inf = validaciones.cargar_y_validar_entre(0, 19, 'Ingrese el limite inferior del rango (entre 0 y 19):',
                                                          'ERROR, DEBE SER ENTRE 0 y 19 INCLUIDOS')
            lim_sup = validaciones.cargar_y_validar_entre(0, 19, 'Ingrese el limite superior del rango (entre 0 y 19): ',
                                                          'ERROR, DEBE SER ENTRE 0 y 19 INCLUIDOS')

            while lim_sup <= lim_inf:
                print('ERROR, EL LIMITE SUPERIOS NO PUEDE SER MENOR O IGUAL AL LIMITE INFERIOR DEL RANGO')
                lim_sup = validaciones.cargar_y_validar_entre(0, 19,
                                                              'Ingrese el limite superior del rango (entre 0 y 19): ',
                                                              'ERROR, DEBE SER ENTRE 0 y 19 INCLUIDOS')

            print(f'Escrbiendo arreglos en {fd}')
            funciones.cargar_revistas_en_arch_entre(fd, lim_inf, lim_sup, vec_revistas)
            time.sleep(0.5)
            print('Arreglos cargados...')
            interface.presione_enter_para()

        elif op == 5:
            funciones.mostrar_revistas_de_arch_con_stock_may_0(fd)
            interface.presione_enter_para()

        elif op == 6:
            print('Gracias por utilizar este programa, adios')
            interface.presione_enter_para('finalizar')


if __name__ == '__main__':
    principal()
