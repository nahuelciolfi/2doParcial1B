import pygame as py

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = py.transform.scale(img, (ancho,alto))

def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes
################################## SPRITE PJ ###############################################################################################
personaje_quieto = [py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Idle (1).png"), 
                    py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Idle (2).png"),
                    py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Idle (3).png"),
                    py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Idle (4).png"),
                    py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Idle (5).png"),
                    py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Idle (6).png"),
                    py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Idle (7).png"),
                    py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Idle (8).png"),
                    py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Idle (9).png"),
                    py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Idle (10).png")]

personaje_camina_derecha = [py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Run (1).png"),
                            py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Run (2).png"),
                            py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Run (3).png"),
                            py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Run (4).png"),
                            py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Run (5).png"),
                            py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Run (6).png"),
                            py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Run (7).png"),
                            py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Run (8).png")]

personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha)

personaje_salta = [py.image.load(r"2C 1°\Segundo Parcial\Sprites Robot\png\Jump (7).png")]

############################################## SPRITE ENEMIGO ##################################################

enemigo_camina = [py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Walk (1).png"),
                  py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Walk (2).png"),
                  py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Walk (3).png"),
                  py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Walk (4).png"),
                  py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Walk (5).png"),
                  py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Walk (6).png"),
                  py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Walk (7).png"),
                  py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Walk (8).png"),
                  py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Walk (9).png"),
                  py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Walk (10).png")]

enemigo_muere = [py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (1).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (2).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (3).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (4).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (5).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (6).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (7).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (8).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (9).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (10).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (11).png"),
                 py.image.load(r"2C 1°\Segundo Parcial\Sprites Zombie\png\male\Dead (12).png")]