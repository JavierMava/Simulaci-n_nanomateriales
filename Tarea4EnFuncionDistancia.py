import pygame
import random
from math import sqrt
from pygame.locals import *
xmax = 1000    #tamano de la pantalla
ymax = 700     

class Particle():
    def __init__(self, iniciox, inicioy):









        self.x = iniciox
        self.y = inicioy
        self.sx = iniciox
        self.sy = inicioy

    def move(self,d,mx,my):

        if self.y < 0:

            self.x=self.sx
            self.y=self.sy

        else:
            self.y-=random.randint(-5,5) #Valores permitidos en el eje y
            
        self.x+=random.randint(-5,5) #Valores permitidos en el eje X        

def Particulas():  
    pygame.init()

    screen = pygame.display.set_mode((xmax,ymax))
    
    colorfondo = (236,234,229)#colores
    colorparticula = (193, 38, 78)
    colorcolision= (16,85,152)
    
    colorarea= (150,150,150)
    colorpina = (236, 234, 229)


    d = 10    #diametro y numero de particulas
    colision =(d+(d/2)) 
    n = random.randint(50,200)  #Cantidad de partículas
    

    
    particulas = []
    for part in range(n): 
        particulas.append( Particle(d*random.randint(0,xmax//d),d*random.randint(0,ymax//d)) ) #Posicion inicial de las particulas
    
    exitflag = False
    while not exitflag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exitflag = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exitflag = True

        screen.fill(colorfondo)  
        for p in particulas:
            p.move(d,xmax,ymax)
            pygame.draw.circle(screen, colorarea, (p.x, p.y), 50)

        for p in particulas:   #control de colisiones
            col = colorcolision
            for otro in particulas:
                if otro == p:
                    continue
                distancia = (sqrt((p.x - otro.x)**2 + (p.y - otro.y)**2))
                if distancia < colision:
                    col = colorparticula
                elif distancia < 100:
                    col = (0, 2 * (100 - distancia) + 55, 0)       
            pygame.draw.circle(screen, col, (p.x, p.y), 10)
            
        #pygame.time.delay(50)
        pygame.display.flip()



    pygame.quit()
    
def main():
    Particulas()

if __name__ == "__main__":
    main()
