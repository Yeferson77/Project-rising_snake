import pygame,random
from pygame.math import Vector2



class Snake:
	""" La clase Snake()  crea objetos de tipo 'Snake' cuyos atributos son:
        ventana-------------> Es una ventana en la pantalla  donde interactuaran los objetos
        img_cabeza,-------------------------->Variable que guarda la imagen de la cabeza de una serpiente
        img_vuelta-------------------------->Variable que guarda la imagen de la curva del cuerpo de una serpiente
        img_cuerpo-------------------------->Variable que guarda la imagen  del cuerpo sin curva  de una serpiente
        img_cola-------------------------->Variable que guarda la imagen  de la cola   de una serpiente

        snake_p---------------------------->lista de Vectores que representan la cabeza, cuerpo y cola de una
		serpiente en ejes (x,y) (La cabeza es el primer dato del vector,el cuerpo los datos intermedios,y la cola el dato final)
        
		direccion--------------------------->vector de tamaño dos que representa la direccion en la que va la
		serpiente

		bloque_nuevo------------------------>variable booleana que permite o deniega adicionar un bloque nuevo 
		a la serpiente
        
		tamaño------------------------------>constante entera que reprenta el tamaño en el cual se divide la 
		pantalla en (x,y)para trabajar con los vectores
        """
	def __init__(self,ventana,img_cabeza,img_vuelta,img_cuerpo,img_cola):
		self.snake_p = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direccion = Vector2(0,0)
		self.bloque_nuevo = False
		self.img_cabeza = img_cabeza
		self.img_cola = img_cola
		self.img_cuerpo = img_cuerpo
		self.img_vuelta = img_vuelta
		self.ventana=ventana
		self.cabeza = self.img_cabeza
		self.tamaño = 40 #Tamaño de celda

	def draw_snake(self):
		"""La funcion draw_snake se enarga de dibujar la serpiente,
		el dibujo se realiza utilizando los vectores,como la ventaja donde se va a dibujar la serpiente
		esta dividida en cuadriculas de tamaño 40, los vectores se ubican en esas cuadricula mediante la 
		posicion(x,y) de cada vector,en el primer vector de la lista se ubica  la cabeza en los vectores 
		intermedios se ubica el cuerpo y en el vextor final se ubica la cola,en cada cuadro asignado al vector
		se pone la imagen respectiva.Como la serpiente se curva se debe guardar el vector anterior y el vector 
		siguiente de los vectores del cuerpo en cada iteracion para asi asignarle al vector intermedio la imagen
		del cuerpo curvo en caso de ser necesario.A causa de que la serpiente se mueve en 4 direccion tiene que
		cambiar las orientaciones de las imagenes de (cabeza,cuerpo,cola) y esto se realiza con las funciones
		update_head_graphics() y update_tail_graphics()               """
		self.update_head_graphics()
		self.update_tail_graphics()

		for ind,block in enumerate(self.snake_p):
			x_pos = int(block.x * self.tamaño)
			y_pos = int(block.y * self.tamaño)
			bloque = pygame.Rect(x_pos,y_pos,self.tamaño,self.tamaño)

			if ind == 0:
				self.ventana.blit(self.cabeza,bloque)
			elif ind == len(self.snake_p) - 1:
				self.ventana.blit(self.cola,bloque)
			else:
				anterior_bloque = self.snake_p[ind + 1] - block
				siguiente_bloque = self.snake_p[ind - 1] - block
				if anterior_bloque.x == siguiente_bloque.x:
					self.ventana.blit(self.img_cuerpo,bloque)
				elif anterior_bloque.y == siguiente_bloque.y:
					self.ventana.blit(pygame.transform.rotate(self.img_cuerpo, 90),bloque)
				else:
					if anterior_bloque.x == -1 and siguiente_bloque.y == -1 or anterior_bloque.y == -1 and siguiente_bloque.x == -1:
						self.ventana.blit(pygame.transform.rotate(self.img_vuelta, 270),bloque)
					elif anterior_bloque.x == -1 and siguiente_bloque.y == 1 or anterior_bloque.y == 1 and siguiente_bloque.x == -1:
						self.ventana.blit(self.img_vuelta,bloque)
					elif anterior_bloque.x == 1 and siguiente_bloque.y == -1 or anterior_bloque.y == -1 and siguiente_bloque.x == 1:
						self.ventana.blit(pygame.transform.rotate(self.img_vuelta, 180),bloque)
					elif anterior_bloque.x == 1 and siguiente_bloque.y == 1 or anterior_bloque.y == 1 and siguiente_bloque.x == 1:
						self.ventana.blit(pygame.transform.rotate(self.img_vuelta, 90),bloque)

	def update_head_graphics(self):
		"""La funcion update_head_graphics() se encarga de girar la cabeza de la serpiente segun hacia donde
		se este moviendo,esto lo hace guardando en la variable 'head_relation' la resta de dos vectores, el
		primer vector es el que representa al  pedazo de cuerpo mas cercano a la cabeza(segundo vector de la 
		lista de vectores),el segundo es el vector que representa a la cabeza(primer vector de la lista de vectores).
		Al primero se le resta el segundo y asi se obtiene el valor de la variable head_relation con esa variable
		se puede saber la orientacion de la cabeza y asi girar la imagen a la orientacion requerida """
		head_relation = self.snake_p[1] - self.snake_p[0]
		if head_relation == Vector2(1,0): self.cabeza =  pygame.transform.rotate(self.img_cabeza, 180)
		elif head_relation == Vector2(-1,0): self.cabeza = self.img_cabeza
		elif head_relation == Vector2(0,1): self.cabeza = pygame.transform.rotate(self.img_cabeza, 90)
		elif head_relation == Vector2(0,-1): self.cabeza = pygame.transform.rotate(self.img_cabeza, 270)

	def update_tail_graphics(self):
		"""La funcion update_tail_graphics() se encarga de girar la cola de la serpiente segun hacia donde se 
		este moviendo,esto lo hace guardando en la variable 'cola_rel' la resta de dos vectores(como las 2 
		posiciones finales de la lista de vectores son variables entonces se usan posiciones negativas para
		acceder facilmente a la ultima y penultima posicion),el primer vector es el que representa al  pedazo
		de cuerpo mas cercano a la cola(penultimo vector de la lista de vectores),el segundo es el vector que
		representa a la cola(ultimo vector de la lista de vectores).Al primero se le resta el segundo y asi se
		obtiene el valor de la variable cola_rel con esa variable se puede saber la orientacion de la cola y
		asi girar la imagen a la orientacion requerida """
		cola_rel = self.snake_p[-2] - self.snake_p[-1]
		if cola_rel == Vector2(1,0): self.cola = pygame.transform.rotate(self.img_cola, 180)
		elif cola_rel == Vector2(-1,0): self.cola = self.img_cola
		elif cola_rel == Vector2(0,1): self.cola = pygame.transform.rotate(self.img_cola, 90)
		elif cola_rel == Vector2(0,-1): self.cola = pygame.transform.rotate(self.img_cola, 270)

	def move_snake(self):
		"""La funcion move_snake se encarca de hacer los movimientos de la serpiente en las distintas direcciones,
		esto lo hace segun sea la condicion,la primera condicion es que si la serpiente come alimento entonces se
		debe agregar un nuevo vector a la lista (bloque_nuevo==True),se crea una copia del cuerpo y a la primera
		posicion de la lista de vectores se le inserta un nuevo vector que tendra los valores de la primera posicion
		de la lista + el vector de hacia donde esta realizando el movimiento la serpiente,  despues el cuerpo
		original toma el valor de la copia y asi se hace el moviento de vectores en este caso.Para el segundo 
		caso donde no se agrega un vector nuevo entonces solo se realiza la copia del cuerpo hasta la penultima 
		posicion de la lista de vectores del cuerpo y a la primera posicion de la lista de vectores se le inserta
		un nuevo vector que tendra los valores de la primera posicion de la lista + el vector de hacia donde esta 
		realizando el movimiento la serpiente, de esta forma se agrega un vector adelante y se elimina uno atras
		para que la lista de vectores siga teniendo el mismo tamaño, despues el cuerpo original toma el valor de
		la copia y asi se hace el moviento de vectores en este caso   """
		if self.bloque_nuevo == True:
			copia_cuerpo = self.snake_p[:]
			copia_cuerpo.insert(0,copia_cuerpo[0] + self.direccion)
			self.snake_p = copia_cuerpo[:]
			self.bloque_nuevo = False
		else:
			copia_cuerpo = self.snake_p[:-1]
			copia_cuerpo.insert(0,copia_cuerpo[0] + self.direccion)
			self.snake_p = copia_cuerpo[:]

	def agruega_bloque(self):
		"""La funcion  agruega_bloque(self) le da el valor de 'True' al atributo  para asi dar la autorizacion
		de agregar un vector nuevo a la lista de vectores del cuerpo de la serpiente"""
		self.bloque_nuevo = True

	def reinicio(self):
		"""la funcion reinicio() es utilizada para reiniciar la lista de vectores que representa 
		a la serpiente a su tamaño original cada que la serpiente pierde y tambien reinicia el vector
		direccion hacia donde se mueve la serpiente"""
		self.snake_p = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direccion = Vector2(0,0)


class Food:
	""" La clase Food()  crea objetos de tipo 'Food' cuyos atributos son:
        
        imagen-------------------------->Variable que guarda la imagen de la comida de la serpiente del nivel 1 
		(un huevo en este caso)

        lista_imagenes-------------------------->lista que guarda las imagenes de la comida de la serpiente del
		nivel 2 (un pajaro rojo en este caso)

        ventana-------------------------->Ventana donde interactua la seerpiente con el alimento
		tamaño------------------------------>constante entera que reprenta el tamaño en el cual se divide la
		pantalla en (x,y)para trabajar con los vectores

        var_x------------------------------->Variable entera que guarda cuanto debe avanzar el objeto comida
		en el eje x (se usa en en nivel 2 porque el pajaro se mueve)

		var_y------------------------------->Variable entera que guarda cuanto debe avanzar el objeto comida
		en el eje y (se usa en en nivel 2 porque el pajaro se mueve)

		cont-------------------------------->Variable entera utilizada para saber en que intervalo numerico
		usar determinada imagen del pajaro(comida 2) para asi simular el aleteo
		"""
	def __init__(self,ventana,imagen,lista_imagenes):
		self.imagen=imagen
		self.lista_imagenes = lista_imagenes
		self.ventana=ventana
		self.poner_comidad()
		self.tamaño = 40
		
		self.var_x=3
		self.var_y=3
		self.cont=0

		

	def dibujar_comida(self):
		"""La funcion dibujar comida() se encarga de dibujar la comida de la serpiente del primer nivel en la 
		ventana,la funcion crea un rectangulo con la coordnadas (x,y) respectivas y de tamaño (40,40),
		despues se dibuja la comida en la posicion del rectangulo"""
		food_rect = pygame.Rect(int(self.pos.x),int(self.pos.y),self.tamaño,self.tamaño)
		self.ventana.blit(self.imagen,food_rect)

	def dibujar_comida_2(self):
		"""La funcion dibujar comida() se encarga de dibujar la comida de la serpiente del primer nivel en la 
		ventana,  La funcion utiliza condiciones if ayudadas por la variable cont para saber en que intervalo 
		numerico usar determinada imagen del pajaro(comida 2),ademas utiliza otras condiciones if ayudadas por la
		varable var_x para determivar hacia que lado en el eje x se esta moviendo y asi usar la imagen que tenga esa 
		orientacion.Posteriormente se utiliza un random que elige entre (-3 y 3) y ese valor se le asigna a var_x
		y var_y para luego sumarle ese valor a las coordenada (x,y) del objeto comida ,de esta forma se simula un
		movimiento aleatorio.Cuando las coordenada (x,y) del objeto superan cierto limite el valor de var_x
		y var_y se invierte para que el objeto se mueva hacia el lado contrario para asi simular un choque con
		las paredes de la ventana.Finalmente se  crea un rectangulo con la coordnadas (x,y) respectivas
		y de tamaño (40,40), despues se dibuja la comida en la posicion del rectangulo"""
		#animacion..............................
		if self.cont==0 :
			if self.var_x==-3 or self.var_x==0 :
				self.imagen=self.lista_imagenes[0]
			elif self.var_x==3:
				self.imagen = self.lista_imagenes[1]
		elif self.cont==1:
			if self.var_x==-3 or self.var_x==0 :
				self.imagen=self.lista_imagenes[2]
			elif self.var_x==3:
				self.imagen = self.lista_imagenes[3]
		elif self.cont==2:
			if self.var_x==-3 or self.var_x==0 :
				self.imagen=self.lista_imagenes[4]
			elif self.var_x==3:
				self.imagen = self.lista_imagenes[5]
		elif self.cont==3:
			if self.var_x==-3 or self.var_x==0 :
				self.imagen=self.lista_imagenes[6]
			elif self.var_x==3:
				self.imagen = self.lista_imagenes[7]

		self.cont=self.cont+1
		if self.cont>=4:
			self.cont=0
        #.......................................................     
		
		#generacion de movimiento en (x,y) del alimento 2
		i=random.randint(0,15)
		lista_opciones=[-3,3]
		rand_x=random.randint(0,1)
		rand_y=random.randint(0,1)
		if i==5:
			self.var_x=lista_opciones[rand_x]
			self.var_y=lista_opciones[rand_y]

		self.pos.x=self.pos.x + self.var_x
		self.pos.y=self.pos.y + self.var_y

        #choque con las paredes de la ventana
		if self.pos.y>=560:
			self.var_y=-3
        
		elif self.pos.x>=1080:
			self.var_x=-3

		elif self.pos.y<=20:
			self.var_y=3
        
		elif self.pos.x<=20:
			self.var_x=3	
         
		#dibuja el pajaro
		self.food_rect = pygame.Rect(int(self.pos.x) ,int(self.pos.y) ,self.tamaño,self.tamaño)
		self.ventana.blit(self.imagen,self.food_rect)
		
        
	def poner_comidad(self):
		""" La funcion poner_comida() se encarga de darle un numero aleatorio de determinado rango a las
		posicion(x,y) de el alimento para asi dibujar el alimento en esas posiciones,esto se utiliza cada
		que la serpiente consume el alimento """
		self.x = random.randint(0,1080)
		self.y = random.randint(0,560)
		self.pos = Vector2(self.x,self.y)

class Game:
	""" La clase game()  crea objetos de tipo 'game' cuyos atributos son:
        ventana-------------> Es una ventana en la pantalla  donde interactuaran los objetos
        imagen-------------------------->Variable que guarda la imagen de la comida de la serpiente
        game_font-------------------------->Variable que guarda un tipo de letre
        snake------------------------------>Variable que guarda un objeto de tipo Snake()
		food------------------------------>Variable que guarda un objeto de tipo Food()
		puntaje--------------------------->variable entera que guarda el valor del puntaje correspondiente
		a la serpiente
		"""
	def __init__(self,ventana,font,imagen,snake,food):
		self.imagen=imagen
		self.ventana=ventana
		self.game_font=font
		self.snake = snake
		self.food = food
		self.puntaje=0

		
    # funcion que revisa la colision con la comida
	def comer(self):
		"""La funcion comer() detecta la colision de la cabeza de la cabeza de la serpiente con la comida para
		luego hacer que aparezca comida en otro lugar y la serpiente aumente un bloque de tamaño.La colision de
		la comida se hace usando un rectangulo posicionado en la cabeza de la serpiente y  otro rectangulo
		posicionado en la misma posicion de la comida de la serpiente.La aparicion de la comida en otro lugar
		se realiza con la funcion poner_comida() de la clase Food y la adicion de un nuevo bloque(vector) a
		la serpiente se realiza con la funcion agruega_bloque() de la clase Snake() """
		rectangulo_comida = pygame.draw.rect(self.ventana, (255,255,255), (int(self.food.pos.x),int(self.food.pos.y),40,40))
		rectangulo_cabeza_serpiente = pygame.draw.rect(self.ventana, (255,255,255), (int(self.snake.snake_p[0].x*40),int(self.snake.snake_p[0].y*40),40,40))
		if rectangulo_comida.colliderect(rectangulo_cabeza_serpiente):
			
			self.food.poner_comidad()
			self.snake.agruega_bloque()

		
        #relocaliza la comida si aparece debajo del cuerpo
		for block in self.snake.snake_p[1:]:
			if (block.x*40>=self.food.pos.x-20 and block.x*40<=self.food.pos.x+20) and (block.y*40>=self.food.pos.y-20 and block.y*40<=self.food.pos.y+20):
				self.food.poner_comidad()

			
		

	def choque(self):
		"""La funcion choque() se encarga de detectar si la cabeza de la serpiente supero el rango de donde esta
		puede moverse ,si la cabeza supera este rango se llama a la funcion game_over de la clase Game(),Se llama
		a la funcion texto_game_over() de la clase Game,despues se retorna True para asi terminar la partida de
		juego.Esta funcion tambien detecta la colision de la comida del nivel 2 con la serpiente,Esto lo hace
		comparando la posicion de la comida y un rango que representa la posicion de los bloque de la serpiente, 
		en caso de los dos ser iguales se evita hacer el movimiento que tenia pensado hacer el alimento .Finalmente
		la funcion detecta colisiones de la serpiente consigo misma,esto lo hace comparando la posicion de cada uno
		de sus bloques(vectores) y en caso de que la posicion de su cabeza sea la misma que la de una parte de
		su cuerpo se llama a la funcion game_over de la clase Game() y se retorna True para finalizar la partida
		de juego"""
		#colision con las paredes
		if self.snake.snake_p[0].x < 0 or self.snake.snake_p[0].x > 27 or self.snake.snake_p[0].y < 0 or self.snake.snake_p[0].y > 14 :
			self.game_over()
			self.texto_game_over()
			return True

		#colision de la comida con el cuerpo
		for block in self.snake.snake_p[1:]:
			if (block.x*40>=self.food.pos.x-50 and block.x*40<=self.food.pos.x+50) and (block.y*40>=self.food.pos.y-50 and block.y*40<=self.food.pos.y+50):
					self.food.var_x=self.food.var_x*-1
					self.food.var_y=self.food.var_y*-1

					
		
        #colision con ella misma
		for block in self.snake.snake_p[1:]:
			if block == self.snake.snake_p[0]:	
				self.game_over()
				return True
		return False
		
	def game_over(self):
		"""La funcion game_over se encarga de llamar la funcion reinicio() de la clase Snake()"""
		self.snake.reinicio()

	def texto_game_over(self):
		"""La funcion texto_game_over() se encarga de mostrar durante un determinado tiempo la frase game over
		cuando la serpiente choca con alguna de las paredes de la ventana .Esto lo hace mediante un while que
		imprime en la ventana el texto  'game over' siempre y cuando la restriccion del while se lo permita """
		n=0
		while n<=1000:
				FuenteLetra = pygame.font.SysFont('comicsans',40)
				Texto2=FuenteLetra.render("game over ",1,(255,255,255))
				self.ventana.blit(Texto2,(470,300))
				pygame.display.update()
				n+=1

		
    
