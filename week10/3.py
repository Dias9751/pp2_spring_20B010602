''' 
if event.type == pygame.MOUSEBUTTONDOWN:
    event.dict['pos']
'''
# circle game
import random

import pygame

pygame.init()

size = width, height = (700, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('PyGame Rectangle example')

clock = pygame.time.Clock()  # FPS

color = None
is_true = True

x = 100
y = 100

speed = 20

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
           y -= speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_true = not is_true

    if(not is_true): color = (255, 0, 0)
    else: color = (0, 0, 255)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]: y -= speed
    if pressed[pygame.K_DOWN]: y += speed
    if pressed[pygame.K_LEFT]: x -= speed
    if pressed[pygame.K_RIGHT]: x += speed

    screen.fill((0,0,0))

    if x > width-25:
        x = width-25
    if x < 25:
        x = 25
    if y > height-25:
        y = height-25
    if y < 25:
        y = 25

    pygame.draw.circle(screen, color, [x, y], 25, 25)
    clock.tick(30)
    pygame.display.update()