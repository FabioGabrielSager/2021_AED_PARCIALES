import pickle
import registro_revista
import os.path


def add_in_order_x_num_iden(vec, revista):
    n = len(vec)
    pos = n
    lim_izq, lim_der = 0, n - 1

    while lim_izq <= lim_der:
        c = (lim_izq + lim_der) // 2

        if vec[c].num_identificacion == revista.num_identificacion:
            pos = c
            break

        if revista.num_identificacion < vec[c].num_identificacion:
            lim_der = c - 1

        else:
            lim_izq = c + 1

    if lim_izq > lim_der:
        pos = lim_izq

    vec[pos:pos] = [revista]


def crear_arreglo_revistas(cantidad):
    vec = []
    for i in range(cantidad):
        revista = registro_revista.crear_registro_revista()
        add_in_order_x_num_iden(vec, revista)

    return vec


def buscar_en_arreglo_x_num_iden(vec_revistas, num_identificacion_a_buscar):
    n = len(vec_revistas)
    lim_izq, lim_der = 0, n - 1
    pos = -1

    while lim_izq <= lim_der:
        c = (lim_izq + lim_der) // 2

        if vec_revistas[c].num_identificacion == num_identificacion_a_buscar:
            pos = c
            break

        if num_identificacion_a_buscar < vec_revistas[c].num_identificacion:
            lim_der = c - 1

        else:
            lim_izq = c + 1

    return pos


def cargar_revistas_en_arch_entre(fd, lim_inf, lim_sup, vec_revistas):
    m = open(fd, 'wb')

    for revista in vec_revistas:
        if lim_inf < revista.tipo < lim_sup:
            pickle.dump(revista, m)

    m.close()


def mostrar_revistas_de_arch_con_stock_may_0(fd):
    if os.path.exists(fd):
        m = open(fd, 'rb')
        tam = os.path.getsize(fd)
        cont = 0

        print('Mostrando revistas...')
        while m.tell() < tam:
            revista = pickle.load(m)
            if revista.cantidad_en_stock > 0:
                print(registro_revista.to_string(revista))
                cont += 1

        print(f'La cantidad de revistas mostrada con stock mayor a 0 es de: {cont}')
        m.close()

    else:
        print(f'El archivo de nombre {fd} no existe')
