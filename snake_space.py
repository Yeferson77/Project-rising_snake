import pygame,random
import os

#.....colores en RGB.......
Negro = (0, 0, 0)
Rojo = (255,0,0)
Azul = (0,0,255)


class Snake_Space():
    """ La clase Snake_Space()  crea objetos de tipo 'Snake_Space' cuyos atributos son:
        Imagen_Serpiente_3------------->imagen de formato png que tendra el objeto
        CoorX-------------------------->Variable entera que guarda la posicion en x del objeto
        CoorY-------------------------->Variable entera que guarda la posicion en y del objeto
        VelX-------------------------->Variable entera que guarda cuanto debe avanzar el objeto en x
        VelY-------------------------->Variable entera que guarda cuanto debe avanzar el objeto en Y
        Puntaje-------------------------->Variable entera que guarda el puntaje que le corresponde al objeto
        VelBala_arriba-------------------------->Variable entera que guarda cuanto debe aumentar en posicion las balas que dispara el objeto en el eje y
        MaxBalas-------------------------->Variable entera que guarda la maxima cantidad de disparos que puede realizar el objeto
        """
                
    def __init__(self,Imagen_Serpiente_3,CoorX,CoorY,VelX,
    VelY,Puntaje,VelBala_arriba,MaxBalas):
    
        self.Imagen_Serpiente_3= Imagen_Serpiente_3
        self.CoorX= CoorX
        self.CoorY= CoorY
        self.VelX= VelX
        self.VelY= VelY
        self.Puntaje= Puntaje
        self.VelBala_arriba=VelBala_arriba
        self.MaxBalas=MaxBalas

    def disparo(self):
        """La funcion disparo() crea rectangulos que representan los disparos,los rectangulos tienen posicion x,
        posicion y ,ancho y alto """
        return(pygame.Rect(self.CoorX+35,self.CoorY-15,10,5))



    def colision_serpiente_pared(self):
            """La funcion colision_serpiente_pared() recibe las cordenadas (x,y) del objeto
            y mediante restricciones usando if se cambiar el trayecto del objeto invirtiendo el valor de (x,y),
            El cambio de trayecto se realiza siempre y cuando las posiciones del objeto(x,y) se salgan de las restricciones
            que representan las paredes de la ventana donde interactua el objeto."""

            if self.CoorX<=10 or self.CoorX>=1030 or self.CoorY<=300 or self.CoorY>=520:
                if self.VelX==-6 and self.VelY==-6:
                    self.CoorX-=self.VelX
                    self.CoorY-=self.VelY
                if self.VelX==6 and self.VelY==-6:
                    self.CoorX-=self.VelX
                    self.CoorY-=self.VelY
                if self.VelX==6 and self.VelY==6:
                    self.CoorX-=self.VelX
                    self.CoorY-=self.VelY
                if self.VelX==-6 and self.VelY==6:
                    self.CoorX-=self.VelX
                    self.CoorY-=self.VelY


                if self.VelY== 0:
                    self.CoorX-=self.VelX
                if self.VelX == 0:
                    self.CoorY-=self.VelY

    def movimiento(self):
        """ La funcion movimiento() recibe las coordenadas (x,y) del objeto y le aumenta el valor de 
        VelX (lo que debe avanzar en x) y VelY (lo que debe avanzar en y)
        para que asi cambia el valor de CoorX y CoorY y el objeto pueda mostrarse en una posicion diferente
        simulando asi el movimiento del objeto"""
        self.CoorX +=self.VelX
        self.CoorY +=self.VelY

class Naves_Enemigas():
    """ La clase Naves_Enemigas()  crea objetos de tipo 'Naves_Enemigas' cuyos atributos son:
        Imagen_Nave------------->imagen de formato png que tendra el objeto
        CoorX-------------------------->Variable entera que guarda la posicion en x del objeto
        CoorY-------------------------->Variable entera que guarda la posicion en y del objeto
        VelX-------------------------->Variable entera que guarda cuanto debe avanzar el objeto en x
        VelY-------------------------->Variable entera que guarda cuanto debe avanzar el objeto en Y
        Puntaje-------------------------->Variable entera que guarda el puntaje que le corresponde al objeto
        VelBala_abajo-------------------------->Variable entera que guarda cuanto debe aumentar en posicion las balas que dispara el objeto en el eje y
        MaxBalas-------------------------->Variable entera que guarda la maxima cantidad de disparos que puede realizar el objeto
        """
   
                
    def __init__(self,Imagen_Nave,CoorX,CoorY,VelX,
    VelY,VelBala_abajo,MaxBalas,Puntaje):

        self.Imagen_Nave= Imagen_Nave
        self.CoorX= CoorX
        self.CoorY= CoorY
        self.VelX= VelX
        self.VelY= VelY
        self.VelBala_abajo=VelBala_abajo
        self.MaxBalas=MaxBalas
        self.Puntaje=Puntaje

    def disparo(self):
        """La funcion disparo() crea rectangulos que representan los disparos,los rectangulos tienen posicion x,
        posicion y ,ancho y alto """
        return(pygame.Rect(self.CoorX+33,self.CoorY+20,10,5))

    def colision_nave_pared(self):
            """La funcion colision_nave_pared() recibe las cordenadas (x,y) del objeto
            y mediante restricciones usando if se cambiar el trayecto del objeto invirtiendo el valor de (x,y),
            El cambio de trayecto se realiza siempre y cuando las posiciones del objeto(x,y) se salgan de las restricciones
            que representan las paredes de la ventana donde interactua el objeto."""
            if self.CoorX<=10 or self.CoorX>=1030  :
                self.CoorX-=self.VelX

            if self.CoorY<=30 or self.CoorY>=250:
                self.CoorY-=self.VelY

    def movimiento(self):
        """ La funcion movimiento() recibe las coordenadas (x,y) del objeto y le aumenta el valor de 
        VelX (lo que debe avanzar en x) y VelY (lo que debe avanzar en y)
        para que asi cambia el valor de CoorX y CoorY y el objeto pueda mostrarse en una posicion diferente
        simulando asi el movimiento del objeto,en este caso el valor  de Velx y Vely se define con un random que 
        elige entre los numero enteros (-6,6,0)"""
        i=random.randint(0,15)
        lista_opciones=[-6,6,0]
        rand_x=random.randint(0,2)
        rand_y=random.randint(0,2)
        if i==5:
            self.VelX=lista_opciones[rand_x]
            self.VelY=lista_opciones[rand_y]
        self.CoorX +=self.VelX
        self.CoorY +=self.VelY

    



def Jugar_T():
    """ Jugar_T() es la funcion que crea la ventana donde de interactuan los dos objetos de tipo Snake_Space y tipo
    Naves_Enemigas, En dicha ventana se  posiciona la imagen de fondo,se crean y posicionan los objetos con sus respectivas caracteriasticas
    y mediante eventos de presion de teclas que representan arriba,abajo, izquiera y derecha se aumenta o se disminuye la
    posicion (x y)  de los objetos.Con el evento de presional la tecla derecha de Ctrl se crean balas(rectangulos) que salen del objeto
    hacia el objeto contrario en el eje y.Posteriormente mediante las funciones de colisiones se limita el movimiento de los objeto
    en el escenario.Cuando las balas de un objeto colisionan con el otro objeto,dicho objeto recibe un punto por cada bala
    que logro acertar, los puntos se ven reflejados en la parte superior del escenario y uno de los objetos   llega a un limite definido de puntos
    este objeto de declara como ganador y se imprime en pantalla que objeto gano"""
    
    pygame.init()
    pygame.font.init()
    FuenteLetra = pygame.font.SysFont('comicsans',20)
    FuenteLetra_2 = pygame.font.SysFont('comicsans',30)
    tam = (1120,600)
    Ventana = pygame.display.set_mode(tam)
    Clock=pygame.time.Clock()
    Tablero=pygame.image.load(os.path.join('recursos/nivel_3/espacio.jpg'))
    GameOver=False
    imagen_Snake_3=pygame.image.load(os.path.join('recursos/nivel_3/Snake_nivel_3_op.png'))
    Imagen_Nave_enemiga=pygame.image.load(os.path.join('recursos/nivel_3/imagen_nave_enemiga.png'))
    Snake_S=Snake_Space(imagen_Snake_3,600,400,0,0,0,-7,1000)
    Lista_arriba_Balas_Snake=[]
    Naves_E=Naves_Enemigas(Imagen_Nave_enemiga,600,40,6,6,7,1000,0)
    Lista_abajo_Balas_Nave=[]
    
  
   

    
    #ciclo de la interacion de los objetos en pantalla
    while not GameOver:
        for Evento in pygame.event.get():
            if Evento.type == pygame.QUIT:
                GameOver=True
            if Evento.type == pygame.KEYDOWN:
                #controles jugador 1

                if Evento.key == pygame.K_LEFT:
                        Snake_S.VelX=-6
                              
                               
                if Evento.key == pygame.K_RIGHT:
                        Snake_S.VelX=6
                                  
                if Evento.key == pygame.K_UP:
                        Snake_S.VelY=-6
                          
                if Evento.key == pygame.K_DOWN:
                        Snake_S.VelY = 6

                if Evento.key == pygame.K_SPACE and len(Lista_arriba_Balas_Snake)<Snake_S.MaxBalas:
                    #creacion de las balas
                    Bala=Snake_S.disparo()
                    Lista_arriba_Balas_Snake.append(Bala)


                                   
            

            if Evento.type == pygame.KEYUP:
                #controles jugador 1

                if Evento.key == pygame.K_LEFT:
                        Snake_S.VelX=0
                        
                if Evento.key == pygame.K_RIGHT:
                        Snake_S.VelX=0

                if Evento.key == pygame.K_UP:
                        Snake_S.VelY=0
                            
                    
                if Evento.key == pygame.K_DOWN:
                        Snake_S.VelY = 0

       

        # creacion de disparos nave enemiga
        VarRand=random.randint(0,15)
        if  VarRand==3 and len(Lista_abajo_Balas_Nave)<Naves_E.MaxBalas:
                    Bala_nave=Naves_E.disparo()
                    Lista_abajo_Balas_Nave.append(Bala_nave)

       
       
        #Aumento coorx coory serpiente
        Snake_S.movimiento()

        #Aumento coorx coory nave enemiga
        Naves_E.movimiento()
        
        

        #colisiones con las paredes de la nave y serpiente........................................
        
        Snake_S.colision_serpiente_pared()

        Naves_E.colision_nave_pared()

        

       #rectangulo asociado a ambas tanquetas  para que las balas colisionen....
        cuadrado_nave = pygame.draw.rect(Ventana, (255,255,255), (Naves_E.CoorX, Naves_E.CoorY, 66, 44))
        cuadrado_serpiente = pygame.draw.rect(Ventana, (255,255,255), (Snake_S.CoorX, Snake_S.CoorY, 80, 74))
        
        #..............................imprimir en pantalla.................................#

        Ventana.fill(Negro)
        Ventana.blit(Tablero,(0,0))

        #colision de balas serpiente.............................
        
        for Bala in Lista_arriba_Balas_Snake:   
            Bala.y += Snake_S.VelBala_arriba
            pygame.draw.rect(Ventana,Rojo,Bala)
            """Ventana.blit(Snake_S.Imagen_Serpiente_3,(Bala.x,Bala.y))"""
            
            if cuadrado_nave.colliderect(Bala):
                Snake_S.Puntaje+=1
                Bala.y=-1000  
        
        #colision de balas nave enemiga.............................
        
        
        for Bala_nave in Lista_abajo_Balas_Nave:   
            Bala_nave.y += Naves_E.VelBala_abajo
            pygame.draw.rect(Ventana,Azul,Bala_nave)
            
            
            if cuadrado_serpiente.colliderect(Bala_nave):
                Naves_E.Puntaje+=1
                Bala_nave.y=1000 
        
        
        
        #.----imprimir en pantalla la serpiente---

        Ventana.blit(Snake_S.Imagen_Serpiente_3,(Snake_S.CoorX,Snake_S.CoorY))

        #____imprimir en pantalla nave enemiga_______________
        Ventana.blit(Naves_E.Imagen_Nave,(Naves_E.CoorX,Naves_E.CoorY))

        #____imprimir en pantalla puntaje de la serpiente_______________
        
        Texto_Puntaje_serpiente=FuenteLetra.render("Puntaje serpiente: "+str(Snake_S.Puntaje),1,(255,255,255))
        Ventana.blit(Texto_Puntaje_serpiente,(620,2))

         #____imprimir en pantalla puntaje de la nave_______________
        
        Texto_Puntaje_nave=FuenteLetra.render("Puntaje nave: "+str(Naves_E.Puntaje),1,(255,255,255))
        Ventana.blit(Texto_Puntaje_nave,(300,2))
        
        
         #_____declara al ganador y imprime en pantalla el que gano____
        if Snake_S.Puntaje==30:
            n=0
            while n<=4000:
                Texto=FuenteLetra_2.render("La Ganadora es la serpiente ",1,(255,255,255))
                Ventana.blit(Texto,(350,300))
                n+=1
                pygame.display.update()
            return True

        if Naves_E.Puntaje==30:
            n=0
            while n<=4000:
                Texto2=FuenteLetra_2.render("La Ganadora es la nave espacial ",1,(255,255,255))
                Ventana.blit(Texto2,(350,300))
                n+=1
                pygame.display.update()
            return True
        #_____________________________________________

        pygame.display.update()
        pygame.display.flip()
        Clock.tick(20)

        
        
    pygame.quit()

