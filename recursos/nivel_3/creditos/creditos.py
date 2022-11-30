import pygame


def creditos():
    """la funcion creditos() crea una ventana en la cual se van a posicionar textos que se van 
    moviendo verticalmente """
    
    movimiento_creditos=0
    pygame.init()
    pygame.font.init()
    FuenteLetra = pygame.font.SysFont('comicsans',35)
    Ventana=pygame
    Ventana=pygame.display.set_mode((1000,563))
    ImgCreditos=pygame.image.load("./creditos/fondo_negro.jpg")
    GameOver=False
    
    while not GameOver:
        for Eventos in pygame.event.get():
            if Eventos.type == pygame.QUIT:
                GameOver=True

        movimiento_creditos+=0.1    
        if movimiento_creditos> 600:
            movimiento_creditos=-80

        Ventana.blit(ImgCreditos,(0,0))
        Texto_Credito=FuenteLetra.render("Creado por Yeferson Gomez M.  ",1,(255,255,255))
        Texto_Credito_2=FuenteLetra.render("En Colaboracion con Sebastian agudelo  ",1,(255,255,255))
        Texto_Credito_3=FuenteLetra.render("Desarrollado en Pygame  ",1,(255,255,255))
        Ventana.blit(Texto_Credito,(260,movimiento_creditos))
        Ventana.blit(Texto_Credito_2,(220,movimiento_creditos+70))
        Ventana.blit(Texto_Credito_3,(300,movimiento_creditos+140))
        pygame.display.flip()
       
        
        
        
                
