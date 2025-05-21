# Funciones importadas
from pygame import *
import pygame
import sys
from random import randint

# Rutas de imágenes
bala_enemigo = "bl.png"
bala_disparo = "bl2.png"
bowser_img = "bw.jpg"
llave = "ll.png"
mario_arma = "mrp.png"
mario_img = "mr.jpg"
princesa_img = "pp.jpg"
estrella = "str.png"
fondo_general = "fn.jpg"
fondo_victoria = "fv.jpeg"
fondo_derrota = "fd.jpeg"

# Configuración de pantalla
win_width = 1000
win_height = 700
player_speed = 5
world_limit = 2800  # límite del mundo para la cámara

# Inicialización
pygame.init()
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Mario Adventure")
clock = pygame.time.Clock()

# Clase Plataforma
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(150, 75, 0)):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

# Clase Jugador
class Player(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_height, player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.x_speed = 0
        self.y_speed = 0
        self.width = player_width
        self.height = player_height
        self.stands_on = False
        self.facing_right = True

    def update(self):
        if self.x_speed > 0:
            self.facing_right = True
        elif self.x_speed < 0:
            self.facing_right = False

        self.rect.x += self.x_speed
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        for p in platforms_touched:
            if self.x_speed > 0:
                self.rect.right = p.rect.left
            elif self.x_speed < 0:
                self.rect.left = p.rect.right

        self.gravitate()
        self.rect.y += self.y_speed
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        self.stands_on = False
        for p in platforms_touched:
            if self.y_speed > 0:
                self.rect.bottom = p.rect.top
                self.y_speed = 0
                self.stands_on = True
            elif self.y_speed < 0:
                self.rect.top = p.rect.bottom
                self.y_speed = 0

    def gravitate(self):
        self.y_speed += 0.5

    def jump(self, y):
        if self.stands_on:
            self.y_speed = y

    def fire(self):
        if len(bullets) < 5:
            direction = 1 if self.facing_right else -1
            bullet = Bullet(bala_disparo, self.rect.centerx, self.rect.centery, direction * 10, 10, 20)
            bullets.add(bullet)

# Clase Enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_height, player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.health = 5

    def update(self):
        pass

# Clase Bala
class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_height, player_width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.speed = player_speed
        self.rect.y = player_y

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0 or self.rect.left > world_limit:
            self.kill()
        for platform in barriers:
            if self.rect.colliderect(platform.rect):
                self.kill()

# Instancias de personajes
mario = Player(mario_img, 100, 100, 70, 40)
princesa = Player(princesa_img, 2300, 400, 70, 40)
bowser = Enemy(bowser_img, 500, 610, 120, 90)
bowser2 = Enemy(bowser_img, 1750, 390, 120, 90)

# Grupos
bullets = pygame.sprite.Group()
barriers = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies.add(bowser, bowser2)

# Plataformas
platform_data = [
    (0, 680, 3000, 20),
    (100, 600, 300, 20), (450, 600, 150, 20), (650, 600, 150, 20),
    (500, 450, 200, 20), (750, 450, 150, 20), (950, 450, 150, 20),
    (300, 300, 150, 20), (500, 300, 150, 20), (700, 300, 150, 20),
    (900, 300, 150, 20), (1100, 300, 150, 20),
    (900, 550, 200, 20), (1100, 400, 150, 20), (1300, 600, 200, 20),
    (1500, 300, 150, 20), (1700, 450, 150, 20), (1900, 400, 200, 20),
    (2100, 350, 100, 20), (2300, 500, 200, 20), (2500, 400, 200, 20),
    (2700, 300, 100, 20),
    (800, 580, 20, 100), (1200, 580, 20, 100), (1600, 580, 20, 100),
    (2000, 580, 20, 100), (2400, 580, 20, 100), (2800, 580, 20, 100),
    (1000, 200, 20, 100), (1300, 200, 20, 100), (1600, 200, 20, 100),
    (1900, 200, 20, 100), (2200, 200, 20, 100)
]

for x, y, w, h in platform_data:
    barriers.add(Platform(x, y, w, h))

# Llave y estrella
llave_sprite = pygame.sprite.Sprite()
llave_sprite.image = transform.scale(image.load(llave), (40, 40))
llave_sprite.rect = llave_sprite.image.get_rect(topleft=(1800, 360))

estrella_sprite = pygame.sprite.Sprite()
estrella_sprite.image = transform.scale(image.load(estrella), (40, 40))
estrella_sprite.rect = estrella_sprite.image.get_rect(topleft=(600, 400))

# Fondo
background = transform.scale(image.load(fondo_general), (3000, win_height))

# Estados del juego
tiene_llave = False
camera_x = 0
run = True

# Bucle principal
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mario.fire()
            elif event.key == pygame.K_LEFT:
                mario.x_speed = -player_speed
            elif event.key == pygame.K_RIGHT:
                mario.x_speed = player_speed
            elif event.key == pygame.K_UP:
                mario.jump(-11)
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                mario.x_speed = 0

    mario.update()
    bullets.update()
    enemies.update()

    if mario.rect.centerx - camera_x > win_width - 300 and camera_x < world_limit - win_width:
        camera_x += player_speed
    elif mario.rect.centerx - camera_x < 300 and camera_x > 0:
        camera_x -= player_speed

    screen.blit(background, (-camera_x, 0))
    for platform in barriers:
        screen.blit(platform.image, (platform.rect.x - camera_x, platform.rect.y))
    for enemy in enemies:
        screen.blit(enemy.image, (enemy.rect.x - camera_x, enemy.rect.y))

    screen.blit(mario.image, (mario.rect.x - camera_x, mario.rect.y))
    if tiene_llave:
        screen.blit(princesa.image, (princesa.rect.x - camera_x, princesa.rect.y))
    screen.blit(llave_sprite.image, (llave_sprite.rect.x - camera_x, llave_sprite.rect.y))
    screen.blit(estrella_sprite.image, (estrella_sprite.rect.x - camera_x, estrella_sprite.rect.y))
    for bullet in bullets:
        screen.blit(bullet.image, (bullet.rect.x - camera_x, bullet.rect.y))

    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                bullet.kill()
                enemy.health -= 1
                if enemy.health <= 0:
                    enemies.remove(enemy)

    if mario.rect.colliderect(llave_sprite.rect):
        tiene_llave = True

    if tiene_llave:
        screen.blit(princesa.image, (princesa.rect.x - camera_x, princesa.rect.y))

    if tiene_llave and mario.rect.colliderect(princesa.rect):
        screen.blit(transform.scale(image.load(fondo_victoria), (win_width, win_height)), (0, 0))
        pygame.display.flip()
        pygame.time.delay(3000)
        run = False
        continue

    screen.blit(estrella_sprite.image, (estrella_sprite.rect.x - camera_x, estrella_sprite.rect.y))

    if mario.rect.colliderect(estrella_sprite.rect):
        tiene_estrella = True  # O cualquier lógica que quieras para la estrella

    for enemy in enemies:
        if mario.rect.colliderect(enemy.rect):
            screen.blit(transform.scale(image.load(fondo_derrota), (win_width, win_height)), (0, 0))
            pygame.display.flip()
            pygame.time.delay(3000)
            run = False
            continue

    pygame.display.flip()

# Cierre
pygame.quit()
sys.exit()
