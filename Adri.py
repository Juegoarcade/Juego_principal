#Funciones importadas
from pygame import*
from random import randint

bala_enemigo = "bl.png"
bala_disparo = "bl2.png"
bowser = "bw.jpg"
llave = "ll.png"
mario_arma = "mrp.png"
mario ="mr.jpg"
princesa = "p.jpg"
estrella = "str.png"

win_width = 1000
win_height = 700

#~ciclo principal

run = true

while run = true:

  if 




llave_sprite = pygame.sprite.Sprite()
llave_sprite.image = transform.scale(image.load(llave), (40, 40))
llave_sprite.rect = llave_sprite.image.get_rect(topleft=(1800, 360))

estrella_sprite = pygame.sprite.Sprite()
estrella_sprite.image = transform.scale(image.load(estrella), (40, 40))
estrella_sprite.rect = estrella_sprite.image.get_rect(topleft=(600, 400))



tiene_llave = False



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
