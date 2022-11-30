import pygame


def creditos():
    """la funcion creditos() crea una ventana en la cual se van a posicionar textos que se van 
    moviendo verticalmente usando  el contador  'movimiento_creditos' el cual inicia en 0 y aumenta positivamente
    para simular el efecto de que el texto esta bajando y cuando baja hasta cierto punto el valor de
    movimiento_creditos baja a -80 para que el texto aparezca arriba """
    
    movimiento_creditos=0
    pygame.init()
    pygame.font.init()
    FuenteLetra = pygame.font.SysFont('comicsans',35)
    Ventana=pygame
    Ventana=pygame.display.set_mode((1120,600))
    GameOver=False
    Negro=(0,0,0)
    while not GameOver:
        for Eventos in pygame.event.get():
            if Eventos.type == pygame.QUIT:
                GameOver=True

        movimiento_creditos+=0.1    
        if movimiento_creditos> 600:
            movimiento_creditos=-80
        Ventana.fill(Negro)
        
        Texto_Credito=FuenteLetra.render("Creado por Yeferson Gomez M.  ",1,(255,255,255))
        Texto_Credito_2=FuenteLetra.render("En Colaboracion con Sebastian agudelo  ",1,(255,255,255))
        Texto_Credito_3=FuenteLetra.render("Desarrollado en Pygame  ",1,(255,255,255))
        Ventana.blit(Texto_Credito,(310,movimiento_creditos))
        Ventana.blit(Texto_Credito_2,(270,movimiento_creditos+70))
        Ventana.blit(Texto_Credito_3,(350,movimiento_creditos+140))
        pygame.display.flip()
       
        
        
        
                
