import pygame


pygame.init()
# ==================== the screen surface ===================
screen = pygame.display.set_mode((400, 400)) # window
width, height = screen.get_size()
clock = pygame.time.Clock()

# ============== the player (a little surface) ==============
square = pygame.Surface((20, 20))
square.fill((255, 0, 0))

w, h = 100, 100 # inital position of the player (square)
# directions
right, left, up, down = 0, 0, 0, 0
speed = 5


right_pressed=False
left_pressed=False
up_pressed=False
down_pressed=False
# Infinite loop ======== Game loop ========================
while True:
    if left and w > 0:
        w -= speed
    if right and w < width - 20:
        w += speed
    if up and h > 0 and right and w < width - 20:
        h -= speed
    if up and h > 0:
        h -= speed
    if down and h < width - 20:
        h += speed
        #combo buttons
    if up and h > 0 and right and w < width - 20:
        h -= speed
    if down and h < width - 20 and right and w < width - 20:
        h += speed

    screen.fill(0) # clear screen
    screen.blit(square, (w, h))
    # close button
    if pygame.event.get(pygame.QUIT):
        break
    for event in pygame.event.get():
        # key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT :
                right_pressed = True
            if event.key == pygame.K_LEFT:
                left_pressed = True
            if event.key == pygame.K_UP:
                up_pressed = True
            if event.key == pygame.K_DOWN:
                down_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed=False
            if event.key == pygame.K_LEFT:
                left_pressed=False
            if event.key == pygame.K_UP:
                up_pressed=False
            if event.key == pygame.K_DOWN:
                down_pressed=False
        if up_pressed:
            up=1
        if right_pressed:
            right=1
        if left_pressed:
            left=1
        if down_pressed:
            down=1
        if not up_pressed:
            up=0
        if not right_pressed:
            right=0
        if not left_pressed:
            left=0
        if not down_pressed:
            down=0
    clock.tick(60)
    pygame.display.update()

pygame.quit()