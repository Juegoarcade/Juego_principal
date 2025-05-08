#Dani
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 60:
            self.rect.x += self.speed
        global xplayer
        xplayer = self.rect.x

    def fire(self):
        if not len(bullets) >= 20:
            bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 5, 20, 40)
            bullets.add(bullet)

    def life(self):
        vida = Life('Vida.png',randint(80, win_width - 80),0,3,80,80)
        extra_lives.add(vida)

class Enemy(GameSprite):
    def update(self):
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(50, win_width - 50)
            global lives
            lives -= 1
        else:
            self.rect.y += self.speed
            self.rect.x += self.direction_x

            if randint(0,500) < 5:
                self.direction_x *= -1

            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > win_width - 50:
                self.rect.x = win_width - 50
    
    def attack(self):
        if not len(attacks) >= 5:
            attack = Bomb(img_bomb, self.rect.centerx, self.rect.top, 8, 40, 40)
            attacks.add(attack)

class Bomb(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.kill()

class Life(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.kill()

class Bullet(GameSprite):
    def update(self):
        if self.rect.y < 0:
            self.kill()
        else:
            self.rect.y -= self.speed
