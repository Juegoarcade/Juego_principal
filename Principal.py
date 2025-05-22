# Código completo con bloques en lugar de plataformas

from random import randint
from pygame import *

# --- Assets ---
bala_disparo = "bl2.png"
bala_enemigo = "bl.png"
bowser_img = "bw.jpg"
llave_img = "ll.png"
mario_img = "mr.jpg"
princesa_img = "pp.jpg"
fondo_general = "fn.jpg"
fondo_victoria = "fv.jpeg"
fondo_derrota = "fd.jpeg"
castillo_img = "castle.png"
bloque = "bloque.jpg"

# --- Music ---
mixer.init()
mixer_music.load("musica_fondo.mp3")
mixer_music.play(-1)

m_victoria = mixer.Sound("victoria.mp3")
m_derrota = mixer.Sound("derrota.mp3")

# --- Game Settings ---
win_width = 1000
win_height = 700
player_speed = 5
gravity = 0.5
jump_power = -10
left_bound = 300
right_bound = 700
shift = 0
tecla_e = False

# --- Window ---
window = display.set_mode((win_width, win_height))
display.set_caption("Mario's Adventure")

# --- Groups ---
barriers = sprite.Group()
bullets = sprite.Group()
enemy_bullets = sprite.Group()
bala_disparo_princesa = sprite.Group()
keys = sprite.Group()
all_sprites = sprite.Group()

# --- Flags ---
has_key = False
princesa_libre = False
derrota = False
victory = False

# --- Classes ---
class Player(sprite.Sprite):
    def __init__(self, image_path, x, y, h, w):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (w, h))
        self.rect = self.image.get_rect(x=x, y=y)
        self.x_speed = 0
        self.y_speed = 0
        self.can_jump = True
        self.on_ground = False

    def update(self):
        self.rect.x += self.x_speed
        platforms_hit = sprite.spritecollide(self, barriers, False)
        for p in platforms_hit:
            if self.x_speed > 0:
                self.rect.right = p.rect.left
            elif self.x_speed < 0:
                self.rect.left = p.rect.right
        self.y_speed += gravity
        self.rect.y += self.y_speed
        platforms_hit = sprite.spritecollide(self, barriers, False)
        self.on_ground = False
        for p in platforms_hit:
            if self.y_speed > 0:
                self.rect.bottom = p.rect.top
                self.y_speed = 0
                self.can_jump = True
                self.on_ground = True
            elif self.y_speed < 0:
                self.rect.top = p.rect.bottom
                self.y_speed = 0

    def jump(self, jump_power):
        if self.can_jump:
            self.y_speed = jump_power
            self.can_jump = False

    def fire(self):
        bullet = Bullet(bala_disparo, self.rect.centerx, self.rect.centery, 10, 20, 20)
        bullets.add(bullet)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(sprite.Sprite):
    def __init__(self, img, x, y, h, w, can_shoot=False):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect(x=x, y=y)
        self.can_shoot = can_shoot
        self.shoot_cooldown = 1
        self.health = 5

    def update(self):
        if self.can_shoot:
            self.shoot_cooldown -= 1
            if self.shoot_cooldown <= 0:
                self.shoot()
                self.shoot_cooldown = 270

    def shoot(self):
        if randint(-1,1)>0:
            bullet = EnemyBullet(bala_enemigo, self.rect.left, win_height - 140, -3, 40, 30)
        else:
            bullet = EnemyBullet(bala_enemigo, self.rect.left, 280, -3, 40, 30)    
        enemy_bullets.add(bullet)

class Bullet(sprite.Sprite):
    def __init__(self, img, x, y, speed, h, w):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0 or self.rect.left > win_width:
            self.kill()
        for platform in barriers:
            if self.rect.colliderect(platform.rect):
                self.kill()

class EnemyBullet(sprite.Sprite):
    def __init__(self, img, x, y, speed, h, w):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right < 0:
            self.kill()

class Platform(sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(bloque), (w, h))
        self.rect = self.image.get_rect(x=x, y=y)

class Key(sprite.Sprite):
    def __init__(self, path, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(path), (w, h))
        self.rect = self.image.get_rect(x=x, y=y)

# --- World Setup ---
ground = Platform(0, win_height - 60, 8000, 60)
ground.image.set_alpha(0)
barriers.add(ground)

platform_data = [
    (500, 530, 200, 20),  # bajo1
    (750, 530, 150, 20),  # bajo2
    (950, 530, 150, 20),  # bajo3
    (700, 410, 150, 20),  # medio1
    (900, 380, 150, 20),  # medio2
    (1100, 380, 150, 20), # medio3
    (1100, 480, 150, 20), # bajo4
    (1500, 380, 150, 20), # medio4
    (1700, 530, 150, 20), # bajo5
    (1900, 480, 200, 20), # bajo6
    #(2100, 430, 100, 20), # bajo7
    #(2500, 480, 200, 20), # bajo8
    (2700, 380, 100, 20), # medio5
    (700, 410, 20, 100), # muro0
    (1000, 280, 20, 100), # muro1
    (1265, 280, 20, 100), # muro2
    (1200, 400, 20, 80), # muro3
    (1600, 280, 20, 100), # muro4
    (1900, 280, 20, 100), # muro5
    (2200, 250, 20, 100), # muro6
]
for x, y, w, h in platform_data:
    barriers.add(Platform(x, y, w, h))

key = Key(llave_img, 1200, win_height - 460, 40, 40)
keys.add(key)
all_sprites.add(key) 
mario = Player(mario_img, 100, win_height - 150, 70, 40)
princesa = Player(princesa_img, 2000, win_height - 130 , 50, 40)
bowser = Enemy(bowser_img, 2500, win_height - 220 , 140, 110, can_shoot=True)






# --- CASTILLO ---
castillo = sprite.Sprite()
castillo.image = transform.scale(image.load(castillo_img), (400, 400))
castillo.rect = castillo.image.get_rect(x=2200, y=win_height - 470)
all_sprites.add(castillo)

all_sprites.add(mario, princesa, bowser)
all_sprites.add(*barriers)
enemy_group = sprite.Group(bowser)

# --- Game Loop ---
run = True
while run:
    time.delay(10)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE and not princesa_libre:
                mario.fire()
            elif e.key == K_LEFT or e.key == K_a:
                mario.x_speed = -player_speed
            elif e.key == K_RIGHT or e.key == K_d:
                mario.x_speed = player_speed
            elif e.key == K_UP or e.key == K_w:
                mario.jump(-11.5)
            elif e.key == K_e:  # Detectamos cuando presionamos la tecla E
                tecla_e = True
        elif e.type == KEYUP:
            if e.key in (K_LEFT, K_RIGHT, K_a, K_d):
                mario.x_speed = 0
            elif e.key == K_e:  # Detectamos cuando dejamos de presionar E
                tecla_e = False


    # Desplazamiento con límites y suavizado
    if mario.rect.x > right_bound and mario.x_speed > 0 or mario.rect.x < left_bound and mario.x_speed < 0:
        if mario.x_speed > 0:
            shift -= mario.x_speed - 2
        else:
            shift -= mario.x_speed + 2

        for obj in all_sprites:
            if obj != mario:
                obj.rect.x -= mario.x_speed - 2
        for obj in bullets:
            obj.rect.x -= mario.x_speed - 2
        for obj in enemy_bullets:
            obj.rect.x -= mario.x_speed - 2
        for obj in barriers:
            obj.rect.x -= mario.x_speed - 2
        for obj in enemy_group:
            obj.rect.x -= mario.x_speed - 2
        
        key.rect.x -= mario.x_speed - 2
        
    if mario.rect.x > right_bound:
        mario.rect.x = right_bound
    elif mario.rect.x < left_bound:
        mario.rect.x = left_bound

    for bullet in bullets:
        for enemy in enemy_group:
            if bullet.rect.colliderect(enemy.rect):
                bullet.kill()
                bowser.health -= 1
                if bowser.health <= 0:
                    enemy_group.remove(bowser)
                    bowser.kill()

    mario.update()
    enemy_group.update()
    bullets.update()
    enemy_bullets.update()


    fondo_img = transform.scale(image.load(fondo_general), (win_width, win_height))
    local_shift = shift % win_width
    window.blit(fondo_img, (local_shift, 0))
    if local_shift != 0:
        window.blit(fondo_img, (local_shift - win_width, 0))



    if sprite.spritecollideany(mario, keys):
        key.kill()
        has_key = True
   
        # Si Mario toca cualquier parte de la jaula, esta desaparece
    if has_key and sprite.collide_rect(mario, princesa):
        princesa_libre = True

          


    if princesa_libre:
        princesa.rect.x += mario.x_speed
        princesa.rect.y = mario.rect.y

        
        if princesa.rect.x > right_bound - 60:
            princesa.rect.x = right_bound - 60
        elif princesa.rect.x < left_bound + 60:
            princesa.rect.x = left_bound + 60

    if sprite.spritecollideany(mario, enemy_group) or sprite.spritecollideany(mario, enemy_bullets) or mario.rect.y > win_height:
        mixer_music.stop()
        mixer.Sound.play(m_derrota)
        while mixer.get_busy():
            time.delay(100)
        derrota = True

    if princesa_libre and abs(mario.rect.centerx - castillo.rect.centerx) < 10:
        mixer_music.stop()
        mixer.Sound.play(m_victoria)
        while mixer.get_busy():
            time.delay(100)
        victory = True

    window.blit(castillo.image, castillo.rect.topleft)
    barriers.draw(window)
    enemy_group.draw(window)
    bullets.draw(window)
    enemy_bullets.draw(window)
    mario.reset()
    keys.draw(window)
    princesa.reset()
    all_sprites.draw(window)
    display.update()

    if victory:
        win_img = transform.scale(image.load(fondo_victoria), (win_width, win_height))
        window.blit(win_img, (0, 0))
        display.update()
        time.delay(3000)
        run = False
    elif derrota:
        lose_img = transform.scale(image.load(fondo_derrota), (win_width, win_height))
        window.blit(lose_img, (0, 0))
        display.update()
        time.delay(2000)
        run = False
