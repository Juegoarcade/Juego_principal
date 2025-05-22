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







 for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                bullet.kill()
                enemy.health -= 1
                if enemy.health <= 0:
                    enemies.remove(enemy)


def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0 or self.rect.left > world_limit:
            self.kill()
        for platform in barriers:
            if self.rect.colliderect(platform.rect):
                self.kill()



