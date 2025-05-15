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


run = true

while run == true:
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
      mario.x_speed = -5
    elif event.key == pygame.K_RIGHT:
      mario.x_speed = 5
    elif event.key == pygame.K_UP:
      mario.jump(-7)
