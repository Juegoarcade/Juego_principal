#Funciones importadas
from pygame import*
from random import randint

#Pantalla
win_height = 700
win_width = 1200
window = display.set_mode((win_width, win_height))
display.set_caption("SpaceX")

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
        
        
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 60:
            self.rect.x += self.speed

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
