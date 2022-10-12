artistas = {
    # nombre: codigo, origen, duracion en minutos de la presentacion)
    'Marco Antonio Solis': (1, 'Estados Unidos', 74),
    'Daddy Yankee': (2, 'Puerto Rico', 70),
    'Myriam Hernandez': (3, 'Chile', 40),
    'Los Charros de Lumaco': (4, 'Chile', 25),
    'Metallica': (5, 'Estados Unidos', 45),
    'U2': (6, 'Irlanda', 80),
    'Justin Bieber': (7, 'Canada', 5),
}

artistas_por_dia = {
    # dia, orden de las presentaciones
    "Lunes": (1, 4, 3, 6, 2, 5),
    "Martes": (2, 5, 1),
    "Miercoles": (3, 6, 2, 4),
    "Jueves": (2, 5),
}

#Ejercicio en clases 1:
def cantidad_de_artistas(dia):
    return len(artistas_por_dia[dia])

def nombre_primer_artista(dia):
    for artists, info in artistas.items():
        if info[0] == artistas_por_dia[dia][0]:
            return artists

def pais_origen_ultimo(dia):
    for artists, info in artistas.items():
        if info[0] == artistas_por_dia[dia][-1]:
            return info[1]

def tiempo_total(dia):
    sum = 0
    for artist in artistas_por_dia[dia]:
        for artists, info in artistas.items():
            if artist == info[0]:
                sum = sum + info[2]
    return sum


dia = input('Ingrese dia: ')
print('Ese dia se presentaran', cantidad_de_artistas(dia), 'artistas')
print('El primer artista del dia sera', nombre_primer_artista(dia))
print('El ultimo artista del dia viene de', pais_origen_ultimo(dia))
print('Ese dia el concierto completo durara', tiempo_total(dia),'minutos')
