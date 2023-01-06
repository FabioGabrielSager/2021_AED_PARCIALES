"""
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una variable de
tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para indicar el final
del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco.
El programa debe incluir al menos una función simple con parámetros y retorno de resultado, debe procesar el texto
caracter a caracter (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

b.)      Ítems a desarrollar.

Turno 03 – Enunciado 03 [T3E3]

Determinar la cantidad promedio de vocales (minúsculas o mayúsculas) entre todas las palabras del texto. Por ejemplo,
en el texto “No hay gloria sin esfuerzo.”, hay un total de 5 palabras, y un total de 10 vocales. Por lo tanto,
el promedio pedido es 2 vocales por palabra.

Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que finalizan con el primer caracter
de todo el texto (minúscula o mayúscula si es letra). Por ejemplo, en el texto: "Antes de ahora no sabia nada.",
hay 3 palabras que cumplen con la condición ("antes", "ahora" y "nada") sobre un total de 6 palabras. Por lo tanto,
el porcentaje pedido es del 50%.

Determinar la cantidad de palabras que incluyeron una "r" (minúscula o mayúscula) entre las primeras dos posiciones,
pero no contuvieron una "n" entre las posiciones tres y cuatro. Por ejemplo, en el texto:
"Rara vez renueva el armario.”, hay 2 palabras que cumplen: "Rara" y "armario". La palabra "renueva" no cuenta,
porque si bien tiene una "r" entre las primeras dos, tiene también una "n" en la posición tres.

Determinar la cantidad de palabras que contienen la expresión "br"(con cualquiera de sus letras en minúscula o
en mayúscula) pero de forma que la palabra no comience con la letra "a"
(mayúscula o minúscula). Por ejemplo, en el texto: "Nos abrazamos porque en abril volvemos a Brasil.", hay 1 palabra
que cumple con la condición ("Brasil"). Las palabras "abrazamos" y "abril" tienen "br", pero no cuentan
porque comienzan con "a".
"""

__author__ = 'Fabio Sager (92419) 1k06'


def promedio(acumulado, cantidad):
    prom = 0
    if cantidad > 0:
        prom = round((acumulado / cantidad), 2)
    return prom


def porcentaje(cantidad_1, cantidad_total):

    porcen = 0
    if cantidad_total > 0:
        porcen = round((cantidad_1 * 100) / cantidad_total, 2)

    return porcen


def es_vocal(caracter):

    # Retorna un True si el caracter es una vocal (esta comprendido en el conjunto),
    # de lo contrario retorna un False
    return caracter in 'aeiouáéíóú'


def principal():

    # contadores
    cont_palabras = cont_letras_x_palabra = 0
    cont_vocales = 0
    cont_palabras_punto_2 = 0
    cont_palabras_punto_3 = 0
    cont_palabras_punto_4 = 0

    # Banderas
    bandera_tiene_r = bandera_tiene_n = False
    bandera_comienza_con_a = bandera_tiene_b = bandera_tiene_br = False

    # Otros
    primer_letra_texto = None
    ultimo_caracter = None

    # Carga de datos, cadena de caracteres                                                conversion de cadena a
    #                                                                                     minusculas
    cadena_de_caracteres = input('Ingrese una cadena de caracteres que finalice con ".": ').lower()

    # Ciclo for. para el recorrido de secuencia de a elemento por vez (cadena de caracteres).
    for caracter in cadena_de_caracteres:

        # Analisis de letras
        # Se determina si se trata de un espacio, punto o letra.
        if caracter != ' ' and caracter != '.':
            cont_letras_x_palabra += 1

            # PUNTO 1
            if es_vocal(caracter):
                cont_vocales += 1

            # PUNTO 2
            # Se trata de la primer letra de la primer palabra del texto?
            if cont_palabras == 0 and cont_letras_x_palabra == 1:
                primer_letra_texto = caracter

            # PUNTO 3
            # si se trata de la primera o segunda letra de la palabra
            if cont_letras_x_palabra == 1 or cont_letras_x_palabra == 2:
                if caracter == 'r':
                    bandera_tiene_r = True

            else:
                # si se trata de la cuarta o tercera letra de la palabra
                if cont_letras_x_palabra == 3 or cont_letras_x_palabra == 4:
                    if caracter == 'n':
                        bandera_tiene_n = True

            # PUNTO 4
            # si la palabra comienza con "a"
            if cont_letras_x_palabra == 1 and caracter == 'a':
                bandera_comienza_con_a = True

            # La palabra tiene b?
            if caracter == 'b':
                bandera_tiene_b = True

            else:
                # La palabra tiene una r pegada a un b?
                if bandera_tiene_b and caracter == 'r':
                    bandera_tiene_br = True
                bandera_tiene_b = False

            # Guardado de ultimo caracter de cada palabra
            ultimo_caracter = caracter

        # Si se determino que se trata de un espacio o punto, entoces se trata de un palabra
        else:
            # Por si se ingresan mas de dos espacios o puntos seguidos
            if cont_letras_x_palabra > 0:
                cont_palabras += 1

                # PUNTO 2
                # Es el ultimo caracter de la palabra igual al primer caracter del texto?
                if ultimo_caracter == primer_letra_texto:
                    cont_palabras_punto_2 += 1

                # PUNTO 3
                # si la palabra tiene r en la pocision 1 o 2 y no tiene n en la pocision 3 o 4
                if bandera_tiene_r and not bandera_tiene_n:
                    cont_palabras_punto_3 += 1

                # PUNTO 4
                # Si la palabra no comienza con "a" y tiene la expresion "br"
                if not bandera_comienza_con_a and bandera_tiene_br:
                    cont_palabras_punto_4 += 1

                # Reinicializacion de variables que contienen datos por palabra.
                cont_letras_x_palabra = 0
                bandera_tiene_r = bandera_tiene_n = False
                bandera_comienza_con_a = bandera_tiene_br = False

    # Calculos con los datos obtenidos del analisis del texto
    # PUNTO 1
    promedio_vocales = promedio(cont_vocales, cont_palabras)

    # PUNTO 2
    porcentaje_palabras_punto_2 = porcentaje(cont_palabras_punto_2, cont_palabras)

    # Impresion en pantalla de resultados
    print()
    print('■' * 155)
    print(f'La cantidad promedio de vocales entre todas las palabras del texto fue de: {promedio_vocales}')
    print(f'El porcentaje de palabras (con respecto al total de palabras de texto) que finalizan con '
          f'el primer caracter de todo el texto fue de: {porcentaje_palabras_punto_2}%')
    print(f'La cantidad de palabras que incluyeron una "r" entre las primeras dos posiciones, pero no contuvieron '
          f'una "n" entre las posiciones tres y cuatro fue de: {cont_palabras_punto_3}')
    print(f'La cantidad de palabras que contienen la expresión "br", pero de forma que la palabra no comience '
          f'con la letra "a" fue de: {cont_palabras_punto_4}')
    print('■' * 155)


if __name__ == '__main__':
    principal()
