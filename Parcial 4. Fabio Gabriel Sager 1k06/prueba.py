import random

def generar_descripcion():
    nombres_mujer = 'Ana', 'Rocio', 'Lucia', 'Paola', 'Valentina'
    nombres_hombre = 'Diego', 'Lionel', 'Emiliano', 'Sergio', 'Raul'
    generos = 'Mujer', 'Hombre'
    genero = random.choice(generos)
    descripcion = ''
    descripcion += 'Sexo: ' + genero + ' '
    descripcion += 'Edad: ' + str(random.randint(18, 100)) + ' '

    if genero == 'Mujer':
        descripcion += 'Nombre: ' + random.choice(nombres_mujer)
    else:
        descripcion += 'Nombre: ' + random.choice(nombres_hombre)

    return descripcion

print(generar_descripcion())
