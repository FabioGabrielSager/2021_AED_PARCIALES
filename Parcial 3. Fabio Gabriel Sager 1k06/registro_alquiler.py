# Creacion del tipo de dato alquiler
class Alquiler:
    # Funcion constructora
    def __init__(self, num_identificacion, descripcion, tipo_de_vehiculo, importe, dias_de_alquiler):
        self.num_identificacion = num_identificacion
        self.descripcion = descripcion
        self.tipo_de_vehiculo = tipo_de_vehiculo
        self.importe = importe
        self.dias_de_alquiler = dias_de_alquiler


# write para la muestra de los atributos de un alquiler
def write(alquiler):
    print(f'Numero de identificacion de operaciones: {alquiler.num_identificacion}', end='  |')
    print(f'Descripcion de automovil: {alquiler.descripcion}', end='  |')
    print(f'tipo de vehiculo: {alquiler.tipo_de_vehiculo}', end='  |')
    print(f'Importe a cobrar: {alquiler.importe}', end='  |')
    print(f'Dias de alquiler: {alquiler.dias_de_alquiler}')
