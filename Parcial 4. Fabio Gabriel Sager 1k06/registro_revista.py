import random


class Revista:
    def __init__(self, num_identificacion, nombre, precio_venta, editorial, tipo, cantidad_en_stock):
        self.num_identificacion = num_identificacion
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.editorial = editorial
        self.tipo = tipo
        self.cantidad_en_stock = cantidad_en_stock


def to_string(revista):
    r = ''
    r += 'Numero de identificacion: ' + str(revista.num_identificacion)
    r += ' - Nombre de revista: ' + revista.nombre
    r += ' - Precio: ' + str(revista.precio_venta)
    r += ' - Editorial de procedencia: ' + str(revista.editorial)
    r += ' - Tipo de revista: ' + str(revista.tipo)
    r += ' - Cantidad en stock: ' + str(revista.cantidad_en_stock)

    return r


def generar_nom_revista():
    nom_revistas = 'Acerca De Ti', 'Hobby', 'Revistas Imperium', 'Magnate', 'Nova', 'La Brecha Dorada', 'La Paradoja', \
                   'Nexus', 'La Popular', 'Juventud activa', 'La Trivi', 'Magazine Lux'

    return random.choice(nom_revistas)


def crear_registro_revista():
    num_identificacion = random.randint(0, 10000)
    nombre = generar_nom_revista()
    precio_venta = round(random.uniform(50, 500), 2)
    editorial = random.randint(0, 19)
    tipo = random.randint(0, 19)
    cantidad_en_stock = random.randint(0, 1000)

    revista = Revista(num_identificacion, nombre, precio_venta, editorial, tipo, cantidad_en_stock)
    return revista
