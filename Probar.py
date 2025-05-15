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

p_1 = Player(img_hero, 5, win_height - 80, 20, 60, 60)

villains = sprite.Group()
for i in range(0, 7):
    p_enemy = Enemy(img_enemy, randint(50, win_width - 100), -70, randint(3,5), 70, 100)
    villains.add(p_enemy)

bullets = sprite.Group()
players = sprite.Group()
players.add(p_1)
attacks = sprite.Group()

while run:
    time.delay(50)
    window.blit(bg_game, (0, 0))  # Redibuja el fondo al inicio de cada frame

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                p_1.fire()

    p_1.update()
    p_1.reset()
    villains.update()
    villains.draw(window)

    for villain in villains:
        if randint(1, 600) < 3:
            villain.attack()
    
    if randint(0, 1000) < 2 and lives < 5:
        p_1.life()
    

    attacks.update()
    attacks.draw(window)
    bullets.update()
    bullets.draw(window)
    extra_lives.update()
    extra_lives.draw(window)
    vidas_animadas()
    window.blit(game_font.render("Puntaje: " + str(score), 1, (255,255,255)), (10, 20))
    window.blit(game_font.render("Record: " + str(best_score), 1, (255,255,255)), (win_width - 275, 20))


    vidas = sprite.groupcollide(players, extra_lives, False, True)
    for v in vidas:
        lives += 1
        

    collides = sprite.groupcollide(villains, bullets, True, True)
    for c in collides:
        p_enemy = Enemy(img_enemy, randint(50, win_width - 100), -70, randint(1,5), 70, 100)
        villains.add(p_enemy)
        score += 1

    deads = sprite.groupcollide(players, villains, False, True)
    for d in deads:
        p_enemy = Enemy(img_enemy, randint(50, win_width - 50), -70, randint(3,5), 70, 100)
        villains.add(p_enemy)
        lives -= 1        
        sonido_explosion.play()

    explosions = sprite.groupcollide(players, attacks, False, True)
    for e in explosions:
        lives -= 1
        sonido_explosion.play()

    if lives <= min_lives:
        mixer.music.stop()
        window.blit(bg_game, (0, 0))
        draw.rect(window, (150, 0, 0), start_button)  # Botón verde

        text_start = font_button.render("JUGAR", True, (255, 255, 255))
        text_rect = text_start.get_rect(center=start_button.center)
        window.blit(text_start, text_rect)
        villains.empty()
        players.empty()
        bullets.empty()
        display.update()
        best_score = score
        
        for e in event.get():
            if e.type == QUIT:
                waiting = False
                run = False
            elif e.type == MOUSEBUTTONDOWN:
                if start_button.collidepoint(e.pos):
                    waiting = False
                    run = True
                    lives = 5
                    mixer.music.play(-1)
                    score = 0
                    
                    for i in range(10):
                        p_enemy = Enemy(img_enemy, randint(50, win_width - 100), -70, randint(3,5), 70, 100)
                        villains.add(p_enemy)

                
                    p_1 = Player(img_hero, 5, win_height - 80, 20, 60, 60)
                    players.add(p_1)

                    


    display.update()
