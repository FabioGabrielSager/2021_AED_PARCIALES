import validaciones
import registro_revista


def menu_principal():
    menu = '\n              ■■■■■MENU PRINCIPAL■■■■■' \
           '\n1.Cargar n revistas en arreglo' \
           '\n2.Mostrar arreglo creado en punto 1' \
           '\n3.Buscar en el arreglo creado en el punto 1 una revista por numero de identificacion' \
           '\n4.Guardar en archivo los registros del arreglo cuyo tipo de revista esté entre dos valores x e y que\n' \
           '  se cargan porteclado' \
           '\n5.Mostrar desde el archivo revistas cuyo stock sea mayor a 0 y la cantidad de revistas mostradas' \
           '\n6.Salir del programa' \
           '\n' \
           '\nIngrese la opcion deseada: '

    opcion = validaciones.cargar_y_validar_entre(1, 6, menu, 'ERROR, ESA OPCION NO EXISTE')

    return opcion


def presione_enter_para(para='continuar'):
    input(f'Presione enter para {para}')


def mostrar_arreglo_revistas_con_filtro_op2(vec_revistas, st):
    for revista in vec_revistas:
        if revista.cantidad_en_stock > st:
            print(registro_revista.to_string(revista))

