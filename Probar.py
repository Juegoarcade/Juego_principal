From pygame import *

bala_enemigo = "bl.png"
bala_disparo = "bl2.png"
bowser = "bw.jpg"
llave = "ll.png"
mario_arma = "mrp.png"
mario_img = "mr.jpg"
princesa = "pp.jpg"  # Corregido el nombre del archivo
estrella = "str.png"
fondo_general = "fn.jpg"
fondo_victoria = "fv.jpeg"
fondo_derrota = "fd.jpeg"

win_width = 1000
win_height = 700
player_speed = 5
gravity = 0.5

window = display.set_mode((win_width, win_height))
display.set_caption("Mario's Adventure")

barriers = sprite.Group()
bullets = sprite.Group()


class Player(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_height, player_width):
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.speed = player_speed
        self.rect.y = player_y
        self.direction_x = randint(-2, 2)
        self.x_speed = 0
        self.y_speed = 0
        self.width = player_width
        self.height = player_height
        self.stands_on = False
        self.can_jump = True  # Nuevo atributo para controlar el salto

    def update(self):
        self.rect.x += self.x_speed
        # Añadir límites horizontales
        if self.rect.left < 0:
            self.rect.left = 0
            self.x_speed = 0  # Detener el movimiento al llegar al límite
        elif self.rect.right > win_width:
            self.rect.right = win_width
            self.x_speed = 0  # Detener el movimiento al llegar al límite

        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)

        # Aplicar gravedad solo si no está en una plataforma
        if not self.stands_on:
            self.gravitate()
        self.rect.y += self.y_speed

        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed >= 0:
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom and self.y_speed > 0:  # Añadida condición self.y_speed > 0
                    self.rect.bottom = p.rect.top
                    self.y_speed = 0
                    self.stands_on = p
                    self.can_jump = True  # Restablecer la capacidad de saltar
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)
                self.stands_on = False  # Importante para que no se quede pegado al techo

        # Si no está en ninguna plataforma, no está "stands_on"
        if not platforms_touched:
            self.stands_on = False

    def gravitate(self):
        self.y_speed += gravity

    def jump(self, y):
        if self.can_jump:  # Usar el atributo can_jump
            self.y_speed = y
            self.can_jump = False  # Desactivar el salto hasta que toque el suelo

    def fire(self):
        if len(bullets) < 2:
            bullet = Bullet(bala_disparo, self.rect.centerx, self.rect.top, 10, 20, 40)
            bullets.add(bullet)
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Enemy(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_height, player_width):
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.speed = 2
        self.rect.y = player_y
        self.direction_x = randint(-2, 2)
        self.speed_x = 0.05
        self.width = player_width
        self.height = player_height

    def update(self):
        if self.rect.x < (win_width - self.width) and self.rect.x > 0:
            if randint(0, 100) < 50:
                self.rect.x += self.speed * self.direction_x
            else:
                self.rect.y += self.speed * self.direction_x
            if self.rect.left < 0:
                self.direction_x = 1
            elif self.rect.right > win_width:
                self.direction_x = -1
        elif self.rect.x >= (win_width - self.width):
            self.direction_x = -1
            self.rect.x += self.speed * self.direction_x
        elif self.rect.x <= 0:
            self.direction_x = 1
            self.rect.x += self.speed * self.direction_x
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_height, player_width):
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.speed = player_speed
        self.rect.y = player_y
        self.direction_x = randint(-2, 2)
        self.x_speed = 0.05
        self.width = player_width
        self.height = player_height

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > (win_width - self.width):
            self.kill()


mario = Player(mario_img, 100, win_height - 100, 70, 40)
princesa = Player(princesa, 30, 100, 70, 40)
bowser = Enemy(bowser, 700, win_height - 100, 70, 40)


class Platform(sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.image = Surface([width, height])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


platform1 = Platform(0, win_height - 30, win_width, 30)
platform2 = Platform(200, win_height - 150, 150, 20)
platform3 = Platform(500, win_height - 250, 100, 20)


barriers.add(platform1, platform2, platform3)
enemy_group = sprite.Group()
enemy_group.add(bowser)

run = True

# Game loop
while run:
    time.delay(50)
    for event in event.get():
        if event.type == QUIT:
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                mario.fire()
            elif event.key == K_LEFT:
                mario.x_speed = -5
            elif event.key == K_RIGHT:
                mario.x_speed = 5
            elif event.key == K_UP:
                mario.jump(-7)

    
    mario.update()
    princesa.update()
    bowser.update()
    bullets.update()


    
    window.blit(fondo, (0, 0))
    barriers.draw(window)
    bowser.reset()
    mario.reset() 
    bullets.draw(window)
    display.update()
