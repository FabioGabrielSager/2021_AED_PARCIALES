def cargar_y_validar_entre(lim_inf, lim_sup, msj_ingreso='Ingrese un valor: ', msj_error='ERROR ESE DATO NO EXISTE'):
    opcion = int(input(msj_ingreso))

    while opcion < lim_inf or opcion > lim_sup:
        print()
        print(msj_error)
        print()
        input('Presione enter para continuar')

        opcion = int(input(msj_ingreso))

    return opcion


def cargar_y_validar_mayor_que(limite, msj_ingreso='Ingrese un valor: ', msj_error='ERROR LA CANTIDAD ES ERRONEA'):
    cantidad = int(input(msj_ingreso))

    while cantidad < limite:
        print()
        print(msj_error)
        print()
        input('Presione enter para continuar')

        cantidad = int(input(msj_ingreso))

    return cantidad
