#Iker
win_width = 800

# Shift de fondo y velocidad actual
shift = 0
speed = 0

# Límites de movimiento del personaje (cuando el fondo empieza a moverse)
left_bound = win_width / 40
right_bound = win_width - 8 * left_bound


2. Evento de teclado (en tu loop principal, dentro del ciclo for event in pygame.event.get():)


    


3. Actualizar movimiento del fondo y del personaje (en el bucle principal del juego, después de procesar los eventos)
if (robin.rect.x > right_bound and robin.x_speed > 0) or (robin.rect.x < left_bound and robin.x_speed < 0):
    shift -= robin.x_speed  # mover el fondo en sentido opuesto
    for s in all_sprites:  # mover todos los objetos
        s.rect.x -= robin.x_speed
else:
    robin.rect.x += robin.x_speed  # si no cruzó los límites, el personaje se mueve normalmente


    4. Actualizar fondo (scroll infinito)
local_shift = shift % win_width

window.blit(background_picture, (local_shift, 0))
if local_shift != 0:
    window.blit(background_picture, (local_shift - win_width, 0))

5. Dibujar sprites y actualizar pantalla (al final del ciclo principal)

# Dibujar todos los objetos
all_sprites.draw(window)

# Actualizar la pantalla
pygame.display.update()
