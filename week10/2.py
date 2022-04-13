import pygame  # CLOCK
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'min': RADIUS - 55, 'hour': RADIUS - 100, 'digit': RADIUS - 30}
RADIUS_ARK = RADIUS + 8

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))  # for hours, minute



def blitRotate(surf, image, pos, originPos, angle):

    # от оси к центру
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    # от оси к центру в повернутом виде
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # повернуть центр фото
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # пулучить повернутое фото
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    # повернуть и залить фото
    surf.blit(rotated_image, rotated_image_rect)


def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

image = pygame.image.load('images/first.png')
w, h = image.get_size()

img = pygame.image.load('images/second.png')
w1, h1 = img.get_size()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    surface.fill((0, 0, 0))
    # время
    t = datetime.now()
    hour = ((t.hour % 12) * 5 + t.minute // 12) % 60
    h2 = t.hour
    minute = t.minute
    # цифры
    pygame.draw.circle(surface, (19, 161, 11), (H_WIDTH, H_HEIGHT), RADIUS)
    for digit, pos in clock60.items():
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pygame.draw.circle(surface, pygame.Color('gainsboro'), get_clock_pos(clock60, digit, 'digit'), radius, 7)
    # стрелка
    """pygame.draw.line(surface, pygame.Color('orange'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, hour, 'hour'), 15)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 7)
"""
    pos = (surface.get_width()/2, surface.get_height()/2)
    blitRotate(surface, image, pos, (w/2, h/2), 360-h2*30-minute*0.5)

    blitRotate(surface, img, pos, (w1/2, h1/2), 360-minute*6+43)
    pygame.display.flip()
    clock.tick(20)