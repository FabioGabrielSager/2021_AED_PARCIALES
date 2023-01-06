import random
import validaciones
from registro_alquiler import Alquiler

# Funcion para la muestra del menu principal del programa.
# Y para retornar una opcion valida dentro del mismo menu
def menu_principal():
    menu = '\n              ■■■■■MENU PRINCIPAL■■■■■' \
           '\n1. Cargar datos de n alquileres de coches' \
           '\n2. Mostrar todos lo datos de todos los alquileres ordenados por importes' \
           '\n3. Determinar y mostrar la cantidad de alquileres por tipo de vehiculo' \
           '\n4. Determinar y mostrar el alquiler con mayor importe y la diferencia de este con el ' \
           'promedio de importes' \
           '\n5. Determinar si fue alquilado un vehículo cuya descripción sea igual a c y que tenga un importe de ' \
           'x o más' \
           '\n6. Salir del programa' \
           '\n' \
           '\nIngrese la opcion deseada: '

    # Se invoca a la funcion del modulo validaciones para la carga de una opcion valida dentro de un limite establecido
    opcion = validaciones.cargar_y_validar_entre(1, 6, menu, 'ERROR, ESA OPCION NO EXISTE')

    return opcion

# Funcion para la generacion aleatoria de la descripcion de un auto, retorna un str con la descripcion
def generar_descripcion_auto():
    descripcion = 'Puertas:'

    descripcion += random.choice(('3', '4')) + ' '
    descripcion += random.choice(('con aire', 'sin aire')) + ', '
    descripcion += random.choice(('4x4', '4x2')) + ', '
    descripcion += random.choice(('con turbo', 'Sin turbo')) + ', '
    descripcion += random.choice(('Manual', 'Automatico')) + ', '
    descripcion += random.choice(('gasolero', 'naftero')) + '.'

    return descripcion


# Funcion para la carga de un vector contenedor de n(cantidad) tipos de datos alquileres
def cargar_vec_alquileres(cantidad):
    vec_alquileres = []

    for i in range(cantidad):
        num_identificacion = random.randint(10, 10000)
        descripcion = generar_descripcion_auto()
        tipo_de_vehiculo = random.randint(1, 10)
        importe = random.randint(1000, 10000)
        dias_de_alquiler = random.randint(1, 60)

                   # Se invoca a la clase Alquiler para hacer uso de su funcionalidad __init__
        alquiler = Alquiler(num_identificacion, descripcion, tipo_de_vehiculo, importe, dias_de_alquiler)

        vec_alquileres.append(alquiler)

    return vec_alquileres


# Metodo de ordenamiento (shell sort) para el ordenamiento (de menor a mayor) de un vector contenedor de tipos
# de datos alquileres segun los importes de estos
def shell_sort_importes(vec_alquileres):
    n = len(vec_alquileres)
    h = 1
    while h <= n // 9:
        h = 3*h + 1
    while h > 0:
        for j in range(h, n):
            y = vec_alquileres[j]
            k = j - h
            while k >= 0 and y.importe < vec_alquileres[k].importe:
                vec_alquileres[k+h] = vec_alquileres[k]
                k -= h
            vec_alquileres[k+h] = y
        h //= 3


# Funcion para el conteo (haciendo uso de vector de conteo) de cantidad de alquileres por tipo de auto
def contar_alquileres_por_tipo_auto(vec_alquileres):
    vec_conteo = [0] * 10

    for alquiler in vec_alquileres:
        vec_conteo[alquiler.tipo_de_vehiculo - 1] += 1

    return vec_conteo


# Funcion para la busqueda dentro de un vector contenedor de tipos de datos alquileres el indice del alquiler
# con mayor importe
def buscar_mayor_importe(vec_alquileres):
    mayor_importe = 0
    indice_mayor_importe = None

    for i in range(len(vec_alquileres)):
        if vec_alquileres[i].importe > mayor_importe:
            mayor_importe = vec_alquileres[i].importe
            indice_mayor_importe = i

    return indice_mayor_importe


# Funcion para el calculo de importes de alquileres contenidos en un vector
def calcular_promedio_importes(vec_aquileres):
    acumulador = 0

    for alquiler in vec_aquileres:
        acumulador += alquiler.importe

    return round(acumulador / len(vec_aquileres), 2)


# Funcion para la busqueda dentro de un vector contenedor de tipo de datos alquileres un alquiler segun descripcion y
# un importe menor o igual
def buscar_vehiculo_x_desc_y_importe(vec_alquileres, descripcion, importe):
    n = len(vec_alquileres)

    for i in range(n):
        if vec_alquileres[i].descripcion == descripcion and vec_alquileres[i].importe >= importe:
            return i

    return -1


if __name__ == '__main__':
    menu_principal()
