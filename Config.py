import pygame as py

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = py.transform.scale(img, (ancho,alto))

def rotar_imagen(lista_original,flip_x,flip_y):
    lista_girada = []
    for img in lista_original:
        lista_girada.append(py.transform.flip(img, flip_x, flip_y))
        
    return lista_girada
    
    
################################## SPRITE PJ ###############################################################################################
personaje_quieto_derecha = [py.image.load(r"2C 1º\Segundo Parcial\Sprites Robot\Idle (1).png")]

personaje_quieto_izquierda = rotar_imagen(personaje_quieto_derecha, True, False)

personaje_camina_derecha = [py.image.load(r"2C 1º\Segundo Parcial\Sprites Robot\Run (1).png"),
                            py.image.load(r"2C 1º\Segundo Parcial\Sprites Robot\Run (2).png"),
                            py.image.load(r"2C 1º\Segundo Parcial\Sprites Robot\Run (3).png"),
                            py.image.load(r"2C 1º\Segundo Parcial\Sprites Robot\Run (4).png"),
                            py.image.load(r"2C 1º\Segundo Parcial\Sprites Robot\Run (5).png"),
                            py.image.load(r"2C 1º\Segundo Parcial\Sprites Robot\Run (6).png"),
                            py.image.load(r"2C 1º\Segundo Parcial\Sprites Robot\Run (7).png"),
                            py.image.load(r"2C 1º\Segundo Parcial\Sprites Robot\Run (8).png")]

personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha, True, False)

personaje_salta = [py.image.load(r"2C 1º\Segundo Parcial\Sprites Robot\Jump (7).png")]

############################################## SPRITE ENEMIGO ##################################################

enemigo_camina = [py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Walk (1).png"),
                  py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Walk (2).png"),
                  py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Walk (3).png"),
                  py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Walk (4).png"),
                  py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Walk (5).png"),
                  py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Walk (6).png"),
                  py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Walk (7).png"),
                  py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Walk (8).png"),
                  py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Walk (9).png"),
                  py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Walk (10).png")]

enemigo_muere = [py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (1).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (2).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (3).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (4).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (5).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (6).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (7).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (8).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (9).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (10).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (11).png"),
                 py.image.load(r"2C 1º\Segundo Parcial\Sprites Zombie\male\Dead (12).png")]