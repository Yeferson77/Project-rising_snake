import pygame,sys
from pygame.math import Vector2
from snake import *
from PIL import Image
from snake_space import *
from creditos import *


def main():
	"""La funcion main() se encarga de crear la ventana donde se va a interactuar,posiciona la imagen png
	de interfaz como fondo de la  ventana y recibe eventos de clic en partes de la venana para poder ver los 
	creditos,iniciar el juego o salir de la ventana """
	I = Image.open("recursos/pantalla_inicio.png")
	pygame.init()

	ventana = pygame.display.set_mode(I.size)
	principal_img = pygame.image.load("recursos/pantalla_inicio.png")
	icono_creditos= pygame.image.load("recursos/icono_creditos.png")
	icono_play= pygame.image.load("recursos/icono_play.png")
	icono_salir= pygame.image.load("recursos/icono_salir.png")
	ventana.blit(principal_img,(0,0))

	pygame.display.update()
	x=True
	while x:
		for eventos in pygame.event.get():
			if eventos.type == pygame.QUIT:
				pygame.quit()
			if eventos.type==pygame.MOUSEBUTTONDOWN:
				(x,y) = pygame.mouse.get_pos()
				if x>=503 and y>=328 and x<=615 and y<=435:
					x=False
					play_game()
					main()
				if x>=767 and y>=327 and x<=877 and y<=430:
					x=False
					exit()
				
				if x>=244 and y>=327 and x<=354 and y<=430:
					x=False
					creditos()
					main()

			if eventos.type==pygame.MOUSEMOTION:
				x,y=pygame.mouse.get_pos()
                
				if (x>=503 and y>=328 and x<=615 and y<=435):
					ventana.blit(icono_play,(503-15,328-15))


				elif (x>=767 and y>=327 and x<=877 and y<=430):
					ventana.blit(icono_salir,(767-15,327-15))
                

				elif (x>=244 and y>=327 and x<=354 and y<=430):
					ventana.blit(icono_creditos,(244-15,327-15))
                

                
                

				elif not(x>=503 and y>=328 and x<=615 and y<=435):
					ventana.blit(principal_img,(0,0))
                    

				elif not(x>=767 and y>=327 and x<=877 and y<=430):
					ventana.blit(principal_img,(0,0))
                

				elif not(x>=244 and y>=327 and x<=354 and y<=430):
					ventana.blit(principal_img,(0,0))
                
				pygame.display.update()
				


def play_game():
	"""La funcion play_game se encarga de iniciar el juego,Primero crea la ventana donde van a interactuar los objetos
	despues se carga la musica del juego,el tipo de letra,las imagenes del primer nivel,las imagenes del segundo
	nivel.Despues se crean 2 objetos de tipo Snake() y Food() que representan a la serpiente y a la comida
	, se crea otro objeto de tipo Game() que recibe los 2 anteriores objetos.Posteriormente se crea un while para
	ejecutar los ciclos de instrucciones que van a dibujar los objetos y sus interacciones.Luego
	se usan las funciones correspondientes a los objetos  como move_snake()-->utilizada para mover el objeto
	serpiente(Snake),choque()---> usada para detectar las colisiones de la serpiente,comer()------->usada para
	detectar los choches del objeto serpiente con el objeto comida y hacer aparecer la comida en otro lugar,
	dibujar_comida() y dibujar_comida_2-------->utilizadas para dibujarla el objeto comida en las posiciones (x,y)
	respectivas,draw_snake()---->usada para dibujar el objeto serpiente,para mover el objeto serpiente se usan
	los evento de presion de teclas arriba,abajo,izquierda y derecha.Para definir el puntaje se toma el tamaño de la lista de vectores correspondiente al objeto serpiente
	y se le resta 3 porque 3 es el tamaño inicial con el que inicia el objeto serpiente.Para acceder al segundo nivel
	se debe llegar a una cantidad determinada de puntaje,despues mediante un condicional if se cambia la imagen del fondo
	y las imagenes correspondientes al objeto serpiente(Snake).Para acceder al nivel 3 se debe llegar a una cantidad
	determinada de puntaje,despues mediante un condicional if se ejecuta la funcion Jugar_T() la cual reinicial el
	puntaje y abre el nuevo escenario donde se realiza el nivel 3.Cunado el while para el juego termina. """
     
	ventana = pygame.display.set_mode((1120,600))
	pygame.init()
	pygame.mixer.init()
	sonido_nivel_1_2 =pygame.mixer.Sound("recursos/sonido/sonido_nivel_1.wav")
	sonido_nivel_3 =pygame.mixer.Sound("recursos/sonido/sonido_nivel_3.wav")
	clock = pygame.time.Clock()
	fuente_letra = pygame.font.SysFont('Eras Bold ITC',25)
	
	game_over=False
	
	#Carga de elementos para el nivel 1

	cabeza_1 = pygame.image.load('recursos/nivel_1/cabeza.png').convert_alpha()
	cola_1 = pygame.image.load('recursos/nivel_1/cola.png').convert_alpha()
	vuelt_1 = pygame.image.load('recursos/nivel_1/vuelta.png').convert_alpha()
	cuerpo_1 = pygame.image.load('recursos/nivel_1/cuerpo.png').convert_alpha()
	fondo_1=pygame.image.load('recursos/nivel_1/cesped.jpg')
	huevo = pygame.image.load('recursos/nivel_1/huevo_normal.png').convert_alpha()
	huevo_contaminado = pygame.image.load('recursos/nivel_1/huevo_contaminado.png').convert_alpha()
	
	
	#Carga de elementos para el nivel 2
	cabeza_2 = pygame.image.load('recursos/nivel_2/cabeza.png').convert_alpha()
	cola_2 = pygame.image.load('recursos/nivel_2/cola.png').convert_alpha()
	vuelt_2 = pygame.image.load('recursos/nivel_2/vuelta.png').convert_alpha()
	cuerpo_2 = pygame.image.load('recursos/nivel_2/cuerpo.png').convert_alpha()
	fondo_2=pygame.image.load('recursos/nivel_2/cielo.jpg')
	
	pajaro_rojo_1_izquierda = pygame.image.load('recursos/nivel_2/pajaro_rojo.png').convert_alpha()
	pajaro_rojo_2_izquierda = pygame.image.load('recursos/nivel_2/pajaro_rojo_2.png').convert_alpha()
	pajaro_rojo_3_izquierda = pygame.image.load('recursos/nivel_2/pajaro_rojo_3.png').convert_alpha()
	pajaro_rojo_4_izquierda = pygame.image.load('recursos/nivel_2/pajaro_rojo_4.png').convert_alpha()

	pajaro_rojo_1_derecha = pygame.image.load('recursos/nivel_2/pajaro_rojo_derecha.png').convert_alpha()
	pajaro_rojo_2_derecha = pygame.image.load('recursos/nivel_2/pajaro_rojo_2_derecha.png').convert_alpha()
	pajaro_rojo_3_derecha = pygame.image.load('recursos/nivel_2/pajaro_rojo_3_derecha.png').convert_alpha()
	pajaro_rojo_4_derecha = pygame.image.load('recursos/nivel_2/pajaro_rojo_4_derecha.png').convert_alpha()
    
	#Creacion de los objetos
	fondo=fondo_1
	snake=Snake(ventana,cabeza_1,vuelt_1,cuerpo_1,cola_1)
	lista_imagenes=[pajaro_rojo_1_izquierda,pajaro_rojo_1_derecha,pajaro_rojo_2_izquierda,pajaro_rojo_2_derecha,
	pajaro_rojo_3_izquierda,pajaro_rojo_3_derecha,pajaro_rojo_4_izquierda,pajaro_rojo_4_derecha]
	food=Food(ventana,huevo,lista_imagenes)
	game = Game(ventana,fuente_letra,huevo,snake,food)
	x=0
    
	#ciclo del juego
	while not game_over:

		

		#movimientos y choques nivel 1 y 2
		game.snake.move_snake()
		if x>1:
			game_over=game.choque()
		else:
			game.choque()

		game.comer()

		#crea el alimento contaminado antes de pasar al 2do nivel
		if game.puntaje == "9":
			game.food.imagen=huevo_contaminado

        #cambia atributos para el segundo nivel
		if game.puntaje == "10":
			game.snake.img_vuelta=vuelt_2
			game.snake.img_cabeza=cabeza_2
			game.snake.img_cola=cola_2
			game.snake.img_cuerpo=cuerpo_2
			fondo=fondo_2

		
		#eventos con el teclado
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					if game.snake.direccion.y != 1:
						game.snake.direccion = Vector2(0,-1)
						x+=1
				if event.key == pygame.K_RIGHT:
					if game.snake.direccion.x != -1:
						game.snake.direccion = Vector2(1,0)
						x+=1
				if event.key == pygame.K_DOWN:
					if game.snake.direccion.y != -1:
						game.snake.direccion = Vector2(0,1)
						x+=1
				if event.key == pygame.K_LEFT:
					if game.snake.direccion.x != 1:
						game.snake.direccion = Vector2(-1,0)
						x+=1
					
        #dibujar en la ventana
		ventana.fill((175,215,70))
		ventana.blit(fondo,(0,0))
		if int(game.puntaje) < 10:
			food.dibujar_comida()
		if  int(game.puntaje) >= 10:
			food.dibujar_comida_2()
			game.imagen=pajaro_rojo_1_derecha
			
		snake.draw_snake()

		#dibuja puntaje del nivel 1 y 2..................................................
		game.puntaje = str(len(game.snake.snake_p) - 3)
		fondo_puntaje = game.game_font.render(game.puntaje,True,(56,74,12))
		puntaje_x = int(1120 - 60)
		puntaje_y = int(600 - 40)
		puntaje_rect = fondo_puntaje.get_rect(center = (puntaje_x,puntaje_y))
		comida_rect = game.imagen.get_rect(midright = (puntaje_rect.left,puntaje_rect.centery))
		bg_rect = pygame.Rect(comida_rect.left,comida_rect.top,comida_rect.width + puntaje_rect.width + 6,comida_rect.height)

		pygame.draw.rect(game.ventana,(167,209,61),bg_rect)
		game.ventana.blit(fondo_puntaje,puntaje_rect)
		game.ventana.blit(game.imagen,comida_rect)
		pygame.draw.rect(game.ventana,(56,74,12),bg_rect,2)
		"""bg_rect = pygame.Rect(1120-50,600-50,50,50)
		pygame.draw.rect(game.ventana,(0,0,0),bg_rect,0)

		Tex=fuente_letra.render(str(game.puntaje),1,(255,255,255))
		game.ventana.blit(Tex,(1120-35,600-40))"""

		

        #inicia el tercer nivel.................................................
		if game.puntaje== "20":
			sonido_nivel_1_2.stop()
			sonido_nivel_3.play()
			game_over=False
			game_over= Jugar_T()

        #inicia_musica
		if game_over!=True:
				sonido_nivel_1_2.play()
		#detiene la musica cuando finaliza el juego
		if game_over==True:
				sonido_nivel_1_2.stop()
				sonido_nivel_3.stop()	
		

		#..........................................................................
		pygame.display.update()
		clock.tick(8)	
		
			

main()