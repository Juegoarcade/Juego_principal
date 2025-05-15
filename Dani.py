#Dani
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

    def gravitate(self):
        self.y_speed += 0.25

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
