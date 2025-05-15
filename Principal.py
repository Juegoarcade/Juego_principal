#Funciones importadas
from pygame import*
from random import randint


bala_enemigo = "bl.png"
bala_disparo = "bl2.png"
bowser = "bw.jpg"
llave = "ll.png"
mario_arma = "mrp.png"
mario ="mr.jpg"
princesa = "pp.jpg"
estrella = "str.png"
fondo_general = "fn.jpg"
fondo_victoria = "fv.jpeg"
fondo_derrota = "fd.jpeg"


win_width = 1000
win_height = 700

class Player():
    def __init__(self, player_image, player_x, player_y, player_speed, player_height, player_width):
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.speed = player_speed
        self.rect.y = player_y
        self.direction_x = randint(-2, 2)
        self.speed_x = 0.05
        self.width = player_width
        self.height = player_height
        self.stands_on = False
        
    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = min(self.rect.left, p.rect.right)
        self.gravitate()
        self.rect.y += self.y_speed
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
                    self.stands_on = p
        elif self.y_speed < 0: 
            self.stand_on = False
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)

    def gravitate(self):
        self.y_speed += 0.5

    def jump(self, y):
        if self.stands_on:
            self.y_speed = y
        
    def fire(self):
        if not len(bullets) >= 2:
            bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 5, 20, 40)
            bullets.add(bullet)

class Enemy():

    def __init__(self, player_image, player_x, player_y, player_speed, player_height, player_width):
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.speed = player_speed
        self.rect.y = player_y
        self.direction_x = randint(-2, 2)
        self.speed_x = 0.05
        self.width = player_width
        self.height = player_height
    
    def update(self):
        if self.rect.x < (win_width - self.width):
            if randint(0, 1) == 0:
                self.rect.x += self.speed
                if randint(0, 1) == 0:
                    self.rect.x -= self.speed
                else:
                    self.rect.y += self.speed
            else:
                self.rect.y -= self.speed
        else:
            self.rect.x -= self.speed

        
            
            
class Bullet():

    def __init__(self, player_image, player_x, player_y, player_speed, player_height, player_width):
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.speed = player_speed
        self.rect.y = player_y
        self.direction_x = randint(-2, 2)
        self.speed_x = 0.05
        self.width = player_width
        self.height = player_height

    def update(self):
        if self.rect.y < 0:
            self.kill()
        else:
            self.rect.y -= self.speed


run = True

 # Bucle principal del juego
 while run:
     # Manejo de eventos
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             run = False # Si el usuario cierra la ventana, termina el bucle
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 player.fire() # Si se presiona la barra espaciadora, el jugador dispara

     # Actualización de los objetos del juego
     player.update()
     enemy.update()
     bullets.update() # Actualiza la posición de todas las balas en el grupo

     # Detección de colisiones (ejemplo básico)
     for bullet in bullets:
         if sprite.collide_rect(bullet, enemy):
             bullets.remove(bullet) # Elimina la bala
             # Aquí podrías añadir lógica para la salud del enemigo, puntuación, etc.

     # Dibujo de los elementos en la pantalla
     screen.fill((0, 0, 0)) # Fondo negro (puedes cambiar el color)
     screen.blit(player.image, player.rect) # Dibuja al jugador
     screen.blit(enemy.image, enemy.rect) # Dibuja al enemigo
     bullets.draw(screen) # Dibuja todas las balas del grupo

     # Actualiza la pantalla para mostrar los cambios
     pygame.display.flip()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            mario.x_speed = -5
        elif event.key == pygame.K_RIGHT:
            mario.x_speed = 5
    elif event.key == pygame.K_UP:
            mario.jump(-7)


 # Finaliza Pygame
 pygame.quit()
 sys.exit()
