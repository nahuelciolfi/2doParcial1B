from Config import *

class Enemigo:
    def __init__(self, animaciones) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, 50,50)
        self.rectangulo_principal = self.animaciones["izquierda"][0].get_rect()
        self.rectangulo_principal.x = 1200
        self.rectangulo_principal.y = 600

        self.esta_muerto = False
        self.pasos = 0
        self.animacion_actual = self.animaciones["izquierda"]
        self.muriendo = False                                       

    def avanzar(self):
        self.rectangulo_principal.x -= 5

    def animar(self, pantalla):
        largo = len(self.animacion_actual)

        if self.pasos >= largo:
            self.pasos = 0

        pantalla.blit(self.animacion_actual[self.pasos], self.rectangulo_principal)
        self.pasos += 1

        if self.muriendo and self.pasos == largo:
            self.esta_muerto = True

    def actualizar(self, pantalla):
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.avanzar()

    def aplicar_gravedad(self, pantalla, plataformas):
        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
            
        for piso in plataformas:
            if self.rectangulo_principal.colliderect(piso["rectangulo"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.rectangulo_principal.bottom = piso["rectangulo"].top
                break
            else:
                self.esta_saltando = True

    def checkeo_sprite_choca_borde_pantalla(self, pantalla):
        x = self.rectangulo_principal.x
        y = self.rectangulo_principal.y
        width = self.rectangulo_principal.width
        height = self.rectangulo_principal.height

        return (x <= 0 or x + width >= screen_width or
            y <= 0 or y + height >= screen_height)

    def rebote_sprite(self):
        self.desplazamiento_x, self.desplazamiento_y = self.velocidad

        rebote_velocidad = -1 * self.desplazamiento_x 

        if self.rectangulo_principal.x <= 0 or self.rectangulo_principal.x + sprite.rectangulo_width >= screen_width: 
            self.velocidad = (rebote_velocidad, self.desplazamiento_y)


