import pygame as py
from pygame.locals import *
from Config import *
from os import system
system("cls")
from Class_Personaje import Personaje
from modo import *
from Class_Enemigo import Enemigo

##############################################        PANTALLA         (ANCHO W - ALTO H) #######################################################################
W,H = 1300, 700
FPS = 18 #Para desacelerar la pantalla

py.init()
RELOJ = py.time.Clock()
PANTALLA = py.display.set_mode((W,H)) # En pixeles
py.display.set_caption("Juego robot")

##############################################     FONDO LVL 1     ############################################################################################               
fondo = py.image.load(r"2C 1°\Segundo Parcial\fondo.jpg")#.convert()
fondo = py.transform.scale(fondo, (W,H))



############################################# FUNCIONES #######################################################################################################

def crear_plataforma(visible, tamaño,  x,  y, path=""):
    plataforma = {}
    if visible:
        plataforma["superficie"] = py.image.load(path)
        plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
    else:
        plataforma["superficie"] = py.Surface(tamaño)

    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y
    return plataforma

############################################## PERSONAJE ####################################################################################################
contador_pasos = 0
diccionario = {}
diccionario["Quieto"] = personaje_quieto
diccionario["Derecha"] = personaje_camina_derecha
diccionario["Izquierda"] = personaje_camina_izquierda
diccionario["Salta"] = personaje_salta

robot = Personaje(diccionario,(70,60),600,500,20)
reescalar_imagenes(diccionario, 80, 70)


############################################# PISO ##########################################################################################################
piso = crear_plataforma(True, (W,20), 0, H-60, r"2C 1°\Segundo Parcial\fondo.jpg")


############################################## PLATAFORMAS ####################################################################################################

plataformas= [piso]

########################################### ENEMIGOS #######################################################################################################
diccionario_animaciones = {"izquierda": enemigo_camina, "Muere": enemigo_muere}
un_enemigo = Enemigo(diccionario_animaciones)
d = {"Muere": diccionario_animaciones["Muere"]}

lista_enemigos = [un_enemigo]
#############################################################################################################################################################

x_inicial = W//2 - 400
y_inicial = 560
rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

que_hace = "Quieto"

############################################ CFG ##############################################################################################################

flag = True
while flag:
    RELOJ.tick(FPS)
    for event in py.event.get():
        if event.type == QUIT:
            flag = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
        elif event.type == KEYDOWN:
            if event.key == K_TAB:
                cambiar_modo()

    teclas = py.key.get_pressed()

    if teclas[py.K_RIGHT]:
        robot.que_hace = "Derecha"
    elif teclas[py.K_LEFT]:
        robot.que_hace = "Izquierda"
    elif(teclas[py.K_SPACE]):
        robot.que_hace = "Salta"


    else:
       robot.que_hace = "Quieto"

    PANTALLA.blit(fondo,(0,0))
    robot.verificar_colision_enemigo(lista_enemigos, PANTALLA)
    robot.actualizar(PANTALLA, plataformas)
    un_enemigo.actualizar(PANTALLA)
    py.display.flip()



# if obtener_modo():
        
#         #py.draw.rect(PANTALLA, "yellow", piso, 3)
#         py.draw.rect(PANTALLA, "blue", robot.rectangulo_principal,3)

#         for plataforma in plataformas:
#             py.draw.rect(PANTALLA, "red", plataforma["rectangulo"], 3)


py.quit()